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

    chars = "abcdefghijklmnopqrstuvwxyz0123456789" 