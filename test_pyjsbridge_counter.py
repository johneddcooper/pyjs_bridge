import time
from pybridge import PyBridge
import pytest
import json

@pytest.fixture()
def pyjsbridge():
    bridge = PyBridge()
    bridge._start_jsbridge()
    #time.sleep(0.1)
    yield bridge
    #time.sleep(0.1)
    bridge._stop_jsbridge()
    #time.sleep(0.1)

def test_set_counter_with_int_returns_int(pyjsbridge):
    r = pyjsbridge.set_counter(3)
    assert r.status_code == 200
    assert r.json().get('msg') == 3

def test_set_counter_with_valid_string_returns_int(pyjsbridge):
    r = pyjsbridge.set_counter('3')
    assert r.status_code == 200
    assert r.json().get('msg') == 3

def test_set_counter_with_invalid_string_returns_error(pyjsbridge):
    r = pyjsbridge.set_counter('three')
    assert r.status_code == 500
    assert r.json().get('error') == 'NaN'

def test_set_counter_with_low_float_returns_rounded_down_int(pyjsbridge):
    r = pyjsbridge.set_counter(3.2)
    assert r.status_code == 200
    assert r.json().get('msg') == 3

def test_set_counter_with_high_float_returns_rounded_down_int(pyjsbridge):
    r = pyjsbridge.set_counter(3.99)
    assert r.status_code == 200
    assert r.json().get('msg') == 3

def test_set_counter_is_zero_on_init(pyjsbridge):
    r = pyjsbridge.get_counter()
    assert r.status_code == 200
    assert r.json().get('msg') == 0

def test_single_increment_counter_is_one_after_init(pyjsbridge):
    r1 = pyjsbridge.get_counter()
    assert r1.json().get('msg') == 0 
    r2 = pyjsbridge.increment_counter()
    assert r2.status_code == 200
    assert r2.json().get('msg') == 1

def test_single_increment_counter_is_correct_after_set(pyjsbridge):
    r1 = pyjsbridge.set_counter(18)
    assert r1.json().get('msg') == 18 
    r2 = pyjsbridge.increment_counter()
    assert r2.status_code == 200
    assert r2.json().get('msg') == 19

def test_multiple_increment_counter_is_correct_after_init(pyjsbridge):
    for i in range(100):
        r = pyjsbridge.increment_counter()
    assert r.status_code == 200
    assert r.json().get('msg') == 100