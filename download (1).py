import random
import pathlib
import os

def generate_random_filenames(directory, num_files=10, filename_length=8):
    """
    Создает указанное количество случайных имен файлов в заданной директории.

    Args:
        directory: Путь к директории, где будут созданы файлы.
        num_files: Количество файлов для создания (по умолчанию 10).
        filename_length: Длина имени файла (по умолчанию 8).
    """

    chars = "abcdefghijklmnopqrstuvwxyz0123456789" # Символы для имени файла

    # Создаем директорию, если она не существует
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)


    created_files = []
    for _ in range(num_files):
        random_filename = ''.join(random.choice(chars) for _ in range(filename_length)) + ".txt"
        filepath = os.path.join(directory, random_filename) # или pathlib.Path(directory) / random_filename
        with open(filepath, 'w') as f: # Создаем пустой файл
            pass
        created_files.append(filepath)

    # Выводим список созданных файлов и их абсолютные пути
    for file in created_files:
        print(os.path.abspath(file)) # или pathlib.Path(file).resolve()


# Пример использования:
directory = "random_files" # Директория для создания файлов
generate_random_filenames(directory)
