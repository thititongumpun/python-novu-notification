import pytest
from payload import Payload


def test_payload():
    payload = Payload(timesheet="Clean DB")
    assert payload.timesheet == "Clean DB"
