import random
import datetime
import array

def generate_random_dates(num_dates=10, years_ago=5):
    """Генерирует массив случайных дат."""
    today = datetime.date.today()
    dates = []
    for _ in range(num_dates):
        days_ago = random.randint(0, 365 * years_ago) 