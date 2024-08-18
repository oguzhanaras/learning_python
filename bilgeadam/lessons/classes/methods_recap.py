# Örnek Metotları (Instance Methods)
# - Bir sınıftan türetilen örneğe ait metotlardır.
# - Bu metot çağrıldığında o örneğe özgü işlemleri gerçekleştirir.
# - Birinci parametresi 'self'tir.

# Sınıf Metotları (Class Methods)
# - Sınıfın kendisine ait (örneğe ait değil) metotlardır.
# - Bu metot çağrıldığında sınıf seviyesinde işlemler gerçekleştirilir.
# - @classmethod dekoratörü kullanılır ve ilk parametre 'cls'tir.

# Statik Metotlar (Static Methods)
# - Ne sınıfın kendisine ne de sınıf örneklerine ait olan metotlardır.
# - Bu metotlar genellikle yardımcı fonksiyonlar olarak kullanılır.
# - @staticmethod decoratörü ile tanımlanır ve ilk parametresi yoktur.

# Özel Metotlar (Special Methods, Magic Methods, Dunder Methods)
# - Çift alt çizgi (double underscore) '__' ile başlayıp biten metotlardır.
# - Çeşitli işlemleri özelleştirmek için kullanılırlar.
# - __init__ metodu sınıfın yapıcı (constructor) metodudur ve bir örnek oluşturulduğu zaman otomatik çağrılır.
# - __str__, __len__, __getitem__ gibi özel metotlar, sınıfın string temsilini döndürmek, uzunluğunu hesaplamak
#   veya indeksleme yapmak gibi işlemleri özelleştirmek için kullanılır.

class Car:
    number_of_cars = 0  # class attribute

    def __init__(self, make, model, year, speed):    # constructor method
        self.make = make       # instance attribute
        self.model = model
        self.year = year
        self.speed = speed
        Car.number_of_cars += 1

    def increase_speed(self, increment):    # instance method
        self.speed += increment

    def decrease_speed(self, decrement):     # instance method
        self.speed = max(0, self.speed - decrement)

    @classmethod
    def get_number_of_cars(cls):   # class method
        return cls.number_of_cars

    @staticmethod
    def safe_speed(speed):    # static method
        return speed <= 82

    def __str__(self):       # special method, string temsili
        return f"{self.make}-{self.model}"

    def __repr__(self):      # special temsili, repr temsili, geliştiriciler için
        return f"{self.make}-{self.model}({self.year})"


car1 = Car("Ford", "Bronco", 2024, 135)
car2 = Car("Porsche", "Taycan", 2023, 155)

# Instance methods
car1.increase_speed(30)
print(car1.speed)
car2.decrease_speed(10)
print(car2.speed)

# Class Methods
Car.get_number_of_cars()
car1.get_number_of_cars()
car2.get_number_of_cars()

# Static Methods
car1.safe_speed(100)
car2.safe_speed(80)
Car.safe_speed(77)

# Special Methods
print(car1)
repr(car2)

# Class attribute
print(car1.number_of_cars)
print(Car.number_of_cars)

# Instance Attributes
print(car1.speed)
print(car2.speed)




