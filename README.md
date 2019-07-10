# PyJS_Bridge
Allows running and interacting with Node JS runtimes using requests and an express API.

## Dependencies
python 3.*
requests 2.*
node 8.*
express 4.*
pytest * (for testing only)

## Setup

`pipenv install`
`yarn install`

## Tests
`pipenv shell`
`pytest test_pyjsbridge.py`

## Usage
One way to extend this method is to, for each desired behavior, implement a method in PyBridge.py and an associated url hook in JSBridge.js. From your python program, create an instance of PyBridge, start the bridge, send commands through it using method calls, and close the bridge when finished. 

### Example Usage of PyJS_Bridge to interact with a Counter.js module.
See the source code for details of this implementation. 

`# main.py
from pybridge import PyBridge
import json

bridge = PyBridge()
bridge._start_jsbridge()

r = pyjsbridge.get_counter()
assert r.json().get('msg') == 0 

r = pyjsbridge.set_counter(23)
assert r.json().get('msg') == 23 

for i in range(100):
    r = pyjsbridge.increment_counter()
assert r.json().get('msg') == 123

bridge._stop_jsbridge() `

### A detailed walkthrough can be found at [learningautomaton.ca](https://learningautomaton.ca/2019/07/pyjsbridge/).
