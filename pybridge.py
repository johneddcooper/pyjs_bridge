import requests
import json
from subprocess import Popen
import os
path_to_jsbridge = os.path.join('./jsbridge.js')

jsbridge_url = "http://localhost:3000"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

class PyBridge:

    # Core functions
    def _start_jsbridge(self):
        self.jsbridge_process = Popen(["node",path_to_jsbridge])

    def _stop_jsbridge(self):
        requests.post(jsbridge_url+"/stop")
        self.jsbridge_process.kill()

    # Sample functions
    def msg_jsbridge(self, msg):
        data = {"msg": msg}
        return requests.post(jsbridge_url, data=json.dumps(data), headers=headers)    
    
    # Counter example functions
    def set_counter(self, value):
        data = {"msg": value}
        return requests.post(jsbridge_url+'/counter/set', data=json.dumps(data), headers=headers)

    def increment_counter(self):
        return requests.post(jsbridge_url+'/counter/increment')

    def get_counter(self):
        return requests.get(jsbridge_url+'/counter')