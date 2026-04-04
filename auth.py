import requests
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('user', 'pass')
a = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
print(a.json())

from requests.auth import HTTPDigestAuth
url = 'https://httpbin.org/digest-auth/auth/user/pass'
a = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
print(a.json())

import requests
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('user', 'pass')
requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)


import requests

bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IktpcmlsbCBNdWhhbm92IiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.BPhyM2rdyaeQOQg7NyLqxYX5yaVjee9KtwF8z22BJ2g"

headers = {"Authorization": f"Bearer {bearer_token}"}

response = requests.get("https://httpbin.org/headers", headers=headers)

print(response.json())



from requests.auth import HTTPDigestAuth
url = 'https://httpbin.org/digest-auth/auth/user/pass'
requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
