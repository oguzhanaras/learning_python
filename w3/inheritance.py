# parent class
class Person:
    def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

    def printname(self):
      print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

# child

# init__() işlevini eklediğinizde, alt sınıf artık ebeveynin __init__() işlevini miras almayacaktır.

# Ebeveynin __init__() işlevinin kalıtımını korumak için, ebeveynin __init__() işlevine bir çağrı ekleyin:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


# Python ayrıca, alt sınıfın ebeveyninden tüm yöntemleri ve özellikleri miras almasını sağlayacak bir super() işlevine sahiptir:
class Student(Person):
    def __init__(self, fname, lname, edu):
        super().__init__(fname, lname)
        self.egitim = edu

    def printedu(self):
        print(self.egitim)


x = Student("Mike", "Olsen", "w3")
x.printname()
x.printedu()

# Alt sınıfa, üst sınıftaki bir işlevle aynı ada sahip bir yöntem eklerseniz, üst yöntemin kalıtımı geçersiz kılınacaktır.