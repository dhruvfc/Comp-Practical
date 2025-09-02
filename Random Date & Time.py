import random as r

def random_datetime():
    day = r.randint(1, 31)
    month = r.randint(1, 12)
    year = r.randint(2000, 2025)
    hour = r.randint(0, 23)
    minute = r.randint(0, 59)
    second = r.randint(0, 59)
    return day, month, year, hour, minute, second

def find_dayofweek(star_day,date):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    start = days.index(star_day.capitalize())
    day = (start + (date - 1)) % 7
    return days[day]

d,m,y,h,mins,sec = random_datetime()
print(f"Random Date & Time: {d:02d}-{m:02d}-{y}-{h:02d}:{mins:02d}:{sec:02d}")
start_day = input(f"What was the day on 01-{m:02d}-{y}?")
actual_day = find_dayofweek(start_day, d)
print(f"Day of the week for {d:02d}-{m:02d}-{y}: {actual_day}")
