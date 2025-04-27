import random
import math
import statistics

def calculate_statistics():
    """Генерирует список случайных чисел и вычисляет статистику."""

    random_numbers = [random.randint(1, 100) for _ in range(100)]

    mean = statistics.mean(random_numbers)
    median = statistics.median(random_numbers)
    stdev = statistics.stdev(random_numbers)
    sqrt_sum = round(math.sqrt(sum(random_numbers)), 2)

    print(f"Среднее: {mean:.2f}, Медиана: {median:.1f}, "
          f"Стандартное отклонение: {stdev:.2f}, Корень из суммы: {sqrt_sum}")


# Вызываем функцию для выполнения расчетов и вывода результатов
calculate_statistics()

