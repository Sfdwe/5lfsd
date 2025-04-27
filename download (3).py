import random
import json
import string

def generate_user_data():
    """Генерирует случайные данные пользователя и сохраняет их в JSON-файл."""

    first_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    last_names = ["Smith", "Jones", "Williams", "Brown", "Davis"]

    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 65) 