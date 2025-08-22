import httpx


response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())

data ={
    "userId": 1,
    "title": "New feature",
    "completed": False
  }

response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
print(response.status_code)
print(response.json())