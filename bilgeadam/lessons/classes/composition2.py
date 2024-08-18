##### COMPOSITION (KOMPOZİSYON) #####
# Bir sınıfın, başka sınıflardan oluşturulan nesneleri içermesi ve bu nesneler üzerinden
# işlemler gerçekleştirilmesidir.

class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        lines.append(f"{self.city}, {self.state}, {self.zipcode}")
        return "\n".join(lines)


address1 = Address("12 Park St.", "NYC", "New York", "12345")
print(address1)


class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.__salary = salary

        self._address = None

    def set_address(self, address: Address):
        self._address = address

    def __str__(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nSalary: ${self.__salary}\nAddress: {self._address}"


employee1 = Employee(1, "Mark Zuckerberg", 2400)
print(employee1)


employee1.set_address(Address("123 Elm Street", "Jacksonville", "Florida", "23123"))
print(employee1)

employee2 = Employee(2, "Satya Nadella", 1500)
employee2.set_address(address1)
print(employee2)



