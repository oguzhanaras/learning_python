class TimeInterval:
    def __init__(self, hours, minutes, seconds):
        if not all(isinstance(i, int) for i in [hours, minutes, seconds]):
            raise TypeError("Hours, minutes, and seconds must be integers.")
        if hours < 0 or minutes < 0 or minutes >= 60 or seconds < 0 or seconds >= 60:
            raise ValueError("Invalid time value provided.")

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def to_minutes(self):
        return self.hours * 60 + self.minutes + self.seconds / 60

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Operand must be of type TimeInterval.")

        total_seconds = self.to_seconds() + other.to_seconds()
        return TimeInterval.from_seconds(total_seconds)

    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Operand must be of type TimeInterval.")

        total_seconds = self.to_seconds() - other.to_seconds()
        if total_seconds < 0:
            raise ValueError("Resulting time interval cannot be negative.")

        return TimeInterval.from_seconds(total_seconds)

    def __mul__(self, value):
        if not isinstance(value, int):
            raise TypeError("Multiplier must be an integer.")

        total_seconds = self.to_seconds() * value
        return TimeInterval.from_seconds(total_seconds)

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)


# Örnek kullanım:
t1 = TimeInterval(2, 45, 30)
t2 = TimeInterval(1, 20, 45)
print("TimeInterval 1:", t1)
print("TimeInterval 2:", t2)

# Toplama
t3 = t1 + t2
print("Toplam:", t3)

# Çıkarma
t4 = t1 - t2
print("Fark:", t4)

# Çarpma
t5 = t1 * 2
print("Çarpım:", t5)

# Karşılaştırma
print("t1 t2'den büyük mü?", t1 > t2)
print("t1 ve t2 eşit mi?", t1 == t2)

# Saniye ve dakika cinsinden dönüşüm
print("t1'in saniye cinsinden değeri:", t1.to_seconds())
print("t1'in dakika cinsinden değeri:", t1.to_minutes())
