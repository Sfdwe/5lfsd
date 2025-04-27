import random
import datetime
import array

def generate_random_dates(num_dates=10, years_ago=5):
    """Генерирует массив случайных дат."""
    today = datetime.date.today()
    dates = []
    for _ in range(num_dates):
        days_ago = random.randint(0, 365 * years_ago) # До 5 лет назад
        random_date = today - datetime.timedelta(days=days_ago)
        dates.append(random_date)
    return array.array('i', [int(date.strftime("%Y%m%d")) for date in dates]) # Массив целых чисел

def calculate_date_differences(dates):
    """Вычисляет разницу между соседними датами."""
    for i in range(len(dates) - 1):
        date1_str = str(dates[i])
        date2_str = str(dates[i+1])
        date1 = datetime.datetime.strptime(date1_str, "%Y%m%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y%m%d").date()
        difference = abs(date2 - date1).days
        print(f"Разница между {date1.strftime('%Y-%m-%d')} и {date2.strftime('%Y-%m-%d')}: {difference} дней")



# Генерируем массив случайных дат
random_dates = generate_random_dates()

# Вычисляем и выводим разницу между датами
calculate_date_differences(random_dates)

