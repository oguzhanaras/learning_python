# Student isimli bir sınıf oluşturalım.
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}({self.age})"

    def get_gpa(self):
        return self.gpa


s1 = Student("Deniz", 24, 3.23)
s2 = Student("Oguzhan", 25, 2.13)
s3 = Student("Yunus", 33, 1.00)
s4 = Student("Ezgi", 24, 3.36)

print(s1)
str(s1)
repr(s1)

# Instructor isimli bir sınıf oluşturalım
class Instructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name}({self.age})"


i1 = Instructor("Salim", 37)
i2 = Instructor("Mehmet", 39)

# Course isimli bir sınıf oluşturalım.
class Course:
    def __init__(self, name, instructor, capacity):
        self.name = name
        self.instructor = instructor
        self.capacity = capacity
        self.students = []

    def empty_seats(self):
        return self.capacity - len(self.students)

    def add_student(self, student):
        if (len(self.students) < self.capacity) and isinstance(student, Student):
            self.students.append(student)
            return True
        return False

    def remove_student(self, student):
        self.students.remove(student)

    def get_average_grade(self):
        total_grade = 0
        if self.students:
            for student in self.students:
                total_grade += student.get_gpa()
            return round(total_grade / len(self.students), 2)
        return "No students added"


python1 = Course("Python", i1, 3)

python1.name
python1.capacity
python1.students

python1.add_student(s1)
python1.add_student(s2)
python1.add_student(s3)
python1.empty_seats()

python1.add_student(s4)
python1.students

python1.remove_student(s2)
python1.empty_seats()
python1.add_student(s4)
python1.students

python1.get_average_grade()

java = Course("Java", i2, 2)
java.empty_seats()

java.add_student(s1)
java.add_student(s2)
java.add_student(s4)

java.get_average_grade()

math = Course("Mathematics", "John Nash", 4)
math.add_student("Ahmet")
math.add_student("Mehmet")
math.students
math.get_average_grade()