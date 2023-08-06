"""megaphone tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_megaphone.streams import (
    AdvertiserCategoriesStream,
    AdvertisersStream,
    AgenciesStream,
    CampaignOrderAdvertisementsStream,
    CampaignOrdersStream,
    CampaignsStream,
    CountriesStream,
    DevicesStream,
    DMAsStream,
    EpisodesStream,
    NetworksStream,
    NielsenSegmentsStream,
    OrganizationTagsStream,
    PodcastsStream,
    PromoOrderAdvertisementsStream,
    PromoOrdersStream,
    RegionsStream,
)

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    NetworksStream,
    PodcastsStream,
    EpisodesStream,
    CampaignsStream,
    CampaignOrdersStream,
    PromoOrdersStream,
    # CampaignOrderAdvertisementsStream,
    PromoOrderAdvertisementsStream,
    AgenciesStream,
    AdvertisersStream,
    DevicesStream,
    NielsenSegmentsStream,
    CountriesStream,
    RegionsStream,
    DMAsStream,
    AdvertiserCategoriesStream,
    OrganizationTagsStream,
]


class Tapmegaphone(Tap):
    """megaphone tap class."""

    name = "tap-megaphone"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("auth_token", th.StringType, required=True),
        th.Property("organization_id", th.StringType, required=True),
        th.Property("metrics_log_level", th.StringType, required=False),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
