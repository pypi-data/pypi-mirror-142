"""Stream type classes for tap-megaphone."""

import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union

from tap_megaphone.client import megaphoneStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class NetworksStream(megaphoneStream):
    """Define custom stream."""

    name = "networks"
    path = "/networks"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "networks.schema.json"
    url_base = "https://cms.megaphone.fm/api/organizations/a0ad16ac-dec1-11e8-bc53-273addf660d7"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"network_id": record["id"]}


class PodcastsStream(NetworksStream):
    """Define custom stream."""

    name = "podcasts"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "podcasts.schema.json"
    parent_stream_type = NetworksStream
    url_base = "https://cms.megaphone.fm/api/networks/{network_id}"
    path = "/podcasts"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"podcast_id": record["id"], "network_id": record["networkId"]}


class EpisodesStream(PodcastsStream):
    """Define custom stream."""

    name = "episodes"
    # path = "/episodes?"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "episodes.schema.json"
    parent_stream_type = PodcastsStream
    path = "/podcasts/{podcast_id}/episodes?"

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        self.logger.info("starting sleep")
        time.sleep(1)
        self.logger.info("ending sleep")

        params = super().get_url_params(context, next_page_token)
        return params


class CampaignsStream(megaphoneStream):
    """Define custom stream."""

    name = "campaigns"
    path = "/campaigns"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "campaigns.schema.json"
    url_base = "https://cms.megaphone.fm/api/organizations/a0ad16ac-dec1-11e8-bc53-273addf660d7"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"campaign_id": record["id"]}


class CampaignOrdersStream(CampaignsStream):
    """Define custom stream."""

    name = "campaign_orders"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "campaign_orders.schema.json"
    parent_stream_type = CampaignsStream
    path = "/campaigns/{campaign_id}/orders"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""

        return {"order_id": record["id"], "campaign_id": record.get("campaignId", "x")}


class PromoOrdersStream(megaphoneStream):
    """Define custom stream."""

    name = "promo_orders"
    path = "/promos"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "promo_orders.schema.json"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"promo_id": record["id"]}


class CampaignOrderAdvertisementsStream(CampaignOrdersStream):
    """Define custom stream."""

    name = "campaign_order_advertisements"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "campaign_order_advertisements.schema.json"
    parent_stream_type = CampaignOrdersStream
    path = "/campaigns/{campaign_id}/orders/{order_id}/advertisements"


class PromoOrderAdvertisementsStream(PromoOrdersStream):
    """Define custom stream."""

    name = "promo_order_advertisements"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "promo_order_advertisements.schema.json"
    parent_stream_type = PromoOrdersStream
    path = "/promos/{promo_id}/advertisements"


class AgenciesStream(megaphoneStream):
    """Define custom stream."""

    name = "agencies"
    path = "/agencies"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "agencies.schema.json"


class AdvertisersStream(megaphoneStream):
    """Define custom stream."""

    name = "advertisers"
    path = "/advertisers"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "advertisers.schema.json"


class DevicesStream(megaphoneStream):
    """Define custom stream."""

    name = "devices"
    path = "/"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "devices.schema.json"
    url_base = "https://cms.megaphone.fm/api/targeting/devices"


class NielsenSegmentsStream(megaphoneStream):
    """Define custom stream."""

    name = "nielsen_segments"
    path = "/"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "nielsen_segments.schema.json"
    url_base = "https://cms.megaphone.fm/api/targeting/nielsen_segments"


class CountriesStream(megaphoneStream):
    """Define custom stream."""

    name = "countries"
    path = "/countries"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "countries.schema.json"
    url_base = "https://cms.megaphone.fm/api/targeting/geo"


class RegionsStream(megaphoneStream):
    """Define custom stream."""

    name = "regions"
    path = "/regions"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "regions.schema.json"
    url_base = "https://cms.megaphone.fm/api/targeting/geo"


class DMAsStream(megaphoneStream):
    """Define custom stream."""

    name = "dmas"
    path = "/dmas"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "dmas.schema.json"
    url_base = "https://cms.megaphone.fm/api/targeting/geo"


class AdvertiserCategoriesStream(megaphoneStream):
    """Define custom stream."""

    name = "advertiser_categories"
    path = "/categories"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "advertiser_categories.schema.json"
    url_base = "https://cms.megaphone.fm/api/targeting"


class IABAdvertiserCategoriesStream(megaphoneStream):
    """Define custom stream."""

    name = "iab_advertiser_categories"
    path = "/iab_categories"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "iab_advertiser_categories.schema.json"
    url_base = "https://cms.megaphone.fm/api/targeting"


class OrganizationTagsStream(megaphoneStream):
    """Define custom stream."""

    name = "organization_tags"
    path = "/tags"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "organization_tags.schema.json"
