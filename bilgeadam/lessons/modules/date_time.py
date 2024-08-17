import datetime

# datetime CONSTANTS
datetime.MINYEAR
datetime.MAXYEAR
datetime.UTC

# Mevcut zamanı yazdırmak (Current Time)
now = datetime.datetime.now()
print(now)  # YYYY-MM-DD HH:MM:SS

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.tzinfo)
print(now.timestamp())


# Bugünün tarihi
current_date = datetime.date.today()
print(current_date)

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Attributes of datetime module
print(dir(datetime))

# From timestamp to date
date_object = datetime.date.fromtimestamp(1723881755)
print(date_object)

# From timestamp to datetime
dt_object = datetime.datetime.fromtimestamp(1723881755)
print(dt_object)

# datetime time
a = datetime.time()
print(a)
print(type(a))

b = datetime.time(6, 30)
print(b)

c = datetime.time(hour=6, minute=30, second=55, microsecond=234567)
print(c)

print(c.hour, c.minute)

# İki zaman (date/datetime) örneği arasındaki zaman farkı
first_dt = datetime.datetime(1991, 1, 10, 18)
second_dt = datetime.datetime.now()

print(f"Yunus's birth: {first_dt}")
print(f"Now: {second_dt}")

age = second_dt - first_dt
print(age)
age.days
print(type(age))

print(age.total_seconds())

# strftime() format codes
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
now = datetime.datetime.now()
print(now)

# Tarih formatları
format1 = "%Y-%m-%d %H:%M:%S"
print(now.strftime(format1))

format2 = "%d/%m/%Y %H:%M"
print(now.strftime(format2))

format3 = "%d %B %Y %I:%M %p"
print(now.strftime(format3))


