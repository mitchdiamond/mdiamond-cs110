from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("8084 N Ridge Loop E, Eagle Mountain, UT 84005") == "Eagle Mountain"

def test_extract_state():
    assert extract_state("8084 N Ridge Loop E, Eagle Mountain, UT 84005") == "UT"

def test_extract_zipcode():
    assert extract_zipcode("8084 N Ridge Loop E, Eagle Mountain, UT 84005") == "84005"


pytest.main(["-v", "--tb=line", "-rN", __file__])