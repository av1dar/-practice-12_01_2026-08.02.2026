import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status code:", response.status_code)
print("Headers:", response.headers)
print("Body:", response.json())

data = {"title": "foo", "body": "bar", "userId": 1}
post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print("POST status:", post_response.status_code)
print("POST response:", post_response.json())
