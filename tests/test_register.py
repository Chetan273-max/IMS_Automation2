import pytest
from parser.sip_parser import parse_sip_file

@pytest.fixture
def sip_headers():
    return parse_sip_file("data/sip_register.txt")

def test_call_id_present(sip_headers):
    assert "Call-ID" in sip_headers

def test_contact_present(sip_headers):
    assert "Contact" in sip_headers

def test_expires_value(sip_headers):
    assert sip_headers["Expires"] == "3600"
