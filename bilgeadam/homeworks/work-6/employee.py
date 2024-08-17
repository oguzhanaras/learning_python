class Employee:

    def __init__(self, name, position, salary, years_of_service):

        self.name = name
        self.position = position
        self.salary = salary
        self.years_of_service = years_of_service

    def promote(self, new_position, new_salary):

        self.position = new_position
        self.salary = new_salary

    def update_years_of_service(self, new_year):

        self.years_of_service += new_year

    def __str__(self):
        return f"{self.name} adlı calısan {self.position} konumunda {self.years_of_service} yıl boyunca {self.salary} maaşla calısmıstır"


emp1 = Employee("ali", "engineer", 100_000, 3)

print(emp1)

emp1.promote("senior engineer", 200_000)

print(emp1)

emp1.update_years_of_service(1)

print(emp1)