import time
from pybridge import PyBridge
import pytest

@pytest.fixture()
def pyjsbridge():
    bridge = PyBridge()
    bridge._start_jsbridge()
    time.sleep(0.1)
    yield bridge
    time.sleep(0.1)
    bridge._stop_jsbridge()
    time.sleep(0.1)

def test_can_start_stop_jsbridge_process():
    pyb = PyBridge()
    pyb._start_jsbridge()
    #time.sleep(0.1)
    assert pyb.jsbridge_process != None
    pyb._stop_jsbridge()
    #time.sleep(0.2)
    assert pyb.jsbridge_process.poll() != None
    assert pyb.jsbridge_process.returncode == 0
    #time.sleep(0.1)

def test_jsbridge_echos_JSON_on_root_post(pyjsbridge):
    r = pyjsbridge.msg_jsbridge("MsgString")
    assert r.status_code == 200
    assert r.json() == {"msg": "MsgString"}
