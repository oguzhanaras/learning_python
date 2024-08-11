from enum import Enum

class WeekDay(Enum):
    MONDAY = 1  # constant variable
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

issubclass(WeekDay, Enum)

print(WeekDay.MONDAY.name)
print(WeekDay.MONDAY.value)

# enum uyeleri degistirilemezler
WeekDay.MONDAY = 9 # errror cant reassign


class Season(Enum):
    WINTER, SPRING, SUMMER, FALL = range(1, 5)


print(Season.SPRING.name)
print(Season.SPRING.value)
