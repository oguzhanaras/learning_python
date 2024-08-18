import datetime


class Person:
    """
    Bir kişiyi temsil eden bir sınıf. Tam ad, doğum tarihi gibi özelliklere sahiptir.
    Metotlar:
        get_fullname(): Kişinin tam adını döndürür.
        get_lastname(): Kişinin soyadını döndürür.
        set_birthday(year, month, day): Kişinin doğum tarihini ayarlar.
        get_age(): Kişinin yaşını gün ya da yıl cinsinden döndürür.
        __lt__(other: Person): Kişilerin soyadlarını alfabetik sıraya göre karşılaştırır.
        __str__(): Kişinin tam adını bir string olarak döndürür.
        __repr(): Kişinin soyadı ve yaşını bir string olarak döndürür.
        __len__(): Kişinin adında kaç kelime olduğunu döndürür.
    """
    def __init__(self, fullname, birthday=None):
        self.fullname = fullname
        self.birthday = birthday
        self.lastname = self.fullname.split(" ")[-1]

    def get_fullname(self):
        """Kişinin tam adını döndürür"""
        return self.fullname

    def get_lastname(self):
        """Kişinin soyadını döndürür"""
        return  self.lastname

    def set_birthday(self, year, month, day):
        """Kişinin doğum tarihini kaydeder"""
        self.birthday = datetime.date(year, month, day)
        print(f"Doğum tarihi ayarlandı: {self.birthday.strftime('%Y-%m-%d')}")

    def get_age(self):
        """Kişinin yaşını döndürür."""
        if self.birthday is not None:
            return datetime.date.today().year - self.birthday.year

    def __str__(self):
        return self.fullname

    def __repr__(self):
        return f"{self.lastname}({self.get_age()})"

    def __len__(self):
        """Kişilerin adında (soyadı hariç) kaç kelime olduğunu döndürür"""
        return len(self.fullname.split(" ")) - 1

    def __lt__(self, other):
        """Kişilerin soyadlarını alfabetik olarak karşılaştırır"""
        return self.lastname < other.lastname


person1 = Person("Nazım Hikmet Ran")
person2 = Person("Cevat Şakir Kabaağaçlı", datetime.date(1890, 4, 17))
person3 = Person("Ajda Pekkan")

person1.set_birthday(1902, 1, 15)

print(person1)
str(person1)
person1.__str__()

repr(person1)
person1.__repr__()

person1.get_fullname()
person1.get_lastname()
person1.get_age()

len(person1)
len(person2)
len(person3)

person1.__lt__(person2)   # "Ran" < "Kabaağaçlı"
print(person1 < person2)

print(person3 < person1)   # "Pekkan" < "Ran"