import pytest
from airscraper import AirScraper

VIEW_PROTECTED = "https://airtable.com/shr5nH7C01vm95E1Z"
VIEW_PASS = "123456"
VIEW_UNPROTECTED = "https://airtable.com/shrSodX4SH7WDXeBS"
    
@pytest.fixture
def unprotected_view() -> AirScraper:
    return AirScraper(VIEW_UNPROTECTED)

@pytest.fixture
def protected_view_with_pass() -> AirScraper:
    return AirScraper(VIEW_PROTECTED, password=VIEW_PASS)

def test_protected_no_pass_conn_error():
    with pytest.raises(ConnectionError):
        AirScraper(VIEW_PROTECTED)

def test_protected_pass_verification(protected_view_with_pass:AirScraper):
    assert protected_view_with_pass.is_protected == True

def test_unprotected_pass_verification(unprotected_view:AirScraper):
    assert unprotected_view.is_protected == False

