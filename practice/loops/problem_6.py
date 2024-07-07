# We have not specifically learned how to solve the problem here in our lessons. Here, try to use logic and list comprehension to try to assign only even numbers to a list of numbers from 1 to 100.
my_list = [x for x in range(1, 101) if x % 2 == 0]
print(my_list)