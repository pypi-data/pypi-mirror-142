"""REST client handling, including megaphoneStream base class."""

import urllib.parse
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union

import requests
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

from tap_megaphone.auth import megaphoneAuthenticator

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class megaphoneStream(RESTStream):
    """megaphone stream class."""

    # network_id = stream.config.get("network_id")
    # url_base = f"https://cms.megaphone.fm/api/networks/{network_id}"

    # @property
    # def get_url_base(self) -> str:
    #     """Return the api url"""
    #     if "network_id" in self.config:
    #         network_id = self.config.get("network_id")
    #     url_base = f"https://cms.megaphone.fm/api/networks/{network_id}"
    #     return url_base

    # OR use a dynamic url_base:
    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return (
            "https://cms.megaphone.fm/api/organizations/"
            + self.config["organization_id"]
        )

    records_jsonpath = "$[*]"  # Or override `parse_response`.
    # next_page_token_jsonpath = "$.next_page"  # Or override `get_next_page_token`.

    @property
    def authenticator(self) -> megaphoneAuthenticator:
        """Return a new authenticator object."""
        return megaphoneAuthenticator.create_for_stream(self)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # TODO: If pagination is required, return a token which can be used to get the
        #       next page. If this is the final page, return "None" to end the
        #       pagination loop.
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match
        else:
            # TODO: may want to refactor this later on
            pagination_response = response.headers.get("Link", None)
            if pagination_response and "next" in pagination_response:
                for i in pagination_response.split("rel="):
                    if "next" in i:
                        next_page_index = pagination_response.split("rel=").index(i) - 1
                next_page_token = (
                    pagination_response.split("rel=")[next_page_index]
                    .split("<")[1]
                    .split(">")[0]
                )
                self.logger.info("next page: " + next_page_token)
            else:
                next_page_token = None

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        if next_page_token:
            return urllib.parse.parse_qs(urllib.parse.urlparse(next_page_token).query)
        params: dict = {"per_page": "500"}
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def prepare_request_payload(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # TODO: Delete this method if not needed.
        return row
