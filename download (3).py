import random
import json
import string

def generate_user_data():
    """Генерирует случайные данные пользователя и сохраняет их в JSON-файл."""

    first_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    last_names = ["Smith", "Jones", "Williams", "Brown", "Davis"]

    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(18, 65) # Возраст от 18 до 65 лет
    email = f"{name.lower().replace(' ', '.')}{random.randint(100, 999)}@example.com"


    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))

    user_data = {
        "name": name,
        "age": age,
        "email": email,
        "password": password
    }

    with open("user_data.json", "w") as f:
        json.dump(user_data, f, indent=4)

    return user_data


def read_user_data(filename="user_data.json"):
    """Читает данные пользователя из JSON-файла и выводит их на экран."""
    try:
        with open(filename, "r") as f:
            user_data = json.load(f)
            print(json.dumps(user_data, indent=4)) # Выводим с отступами для удобства
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON из файла {filename}.")


# Генерируем и сохраняем данные пользователя
generate_user_data()

# Читаем и выводим данные пользователя из файла
read_user_data()
