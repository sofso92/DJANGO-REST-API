import requests

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" # http://127.0.0.1:8000/


get_response = requests.get(endpoint, params={"abc": 123}, json={"query":"Hello World"}) # HTTP Request
# print(get_response.text) # print raw text response
# print(get_response.status_code) 

print(get_response.json()) # print json response
# print(get_response.status_code) 