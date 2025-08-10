import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "CharlieB@gmail.com",
    "password": "pass123"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Status Code:", login_response.status_code)
print("Login response:", login_response_data)


# Формируем headers для передачи токена
headers = {
    "Authorization": f'Bearer {login_response_data["token"]["accessToken"]}'
}


# Выполняем запрос на получение пользователя
user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_me_response_data = user_me_response.json()

# Выводим данные пользователя
print("Status Code:", user_me_response.status_code)
print("User data:", user_me_response_data)

