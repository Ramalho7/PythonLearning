import requests
requests.post('https://ntfy.sh/testPyAuto', 'Hello, world!')

requests.post('https://ntfy.sh/testPyAuto', 'The rent is too high!', 
headers={'Title':'Important: Read this!', 'Tags': 'warning,neutral_face', 'Priority':'5'})