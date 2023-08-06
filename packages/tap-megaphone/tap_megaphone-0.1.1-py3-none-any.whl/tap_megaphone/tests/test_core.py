"""Tests standard tap features using the built-in SDK tests library."""

import os

from singer_sdk.helpers._util import read_json_file
from singer_sdk.testing import get_standard_tap_tests

from tap_megaphone.tap import Tapmegaphone

CONFIG_PATH = ".secrets/config.json"

if os.getenv("CI"):  # true when running a GitHub Actions workflow
    SAMPLE_CONFIG = {
        "auth_token": os.getenv("TAP_MEGAPHONE_AUTH_TOKEN"),
        "organization_id": os.getenv("TAP_MEGAPHONE_ORGANIZATION_ID"),
    }
else:
    SAMPLE_CONFIG = read_json_file(CONFIG_PATH)

# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(Tapmegaphone, config=SAMPLE_CONFIG)
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
