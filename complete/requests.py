"""
requestsライブラリについて
・サードパーティ製
・標準ライブラリのurllib.requestと比べて直感的にHTTP requestを扱える
"""

import requests


payload = {'key1': 'value1', 'key2': 'value2'}

# r = requests.get('http://httpbin.org/get', params=payload)
# r = requests.post('http://httpbin.org/post', data=payload)
# r = requests.put('http://httpbin.org/put', data=payload)
# r = requests.delete('http://httpbin.org/delete', data=payload)

# r = requests.delete('http://httpbin.org/delete', data=payload, timeout=0.001)

print(r.status_code)
print(r.text)
print(r.json())
