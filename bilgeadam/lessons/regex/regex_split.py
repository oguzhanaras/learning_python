import re

with open("students.txt", encoding="utf-8") as file:
    text = file.read()

lines = re.split(r"\n+", text)
print(lines)

my_dict = {}

for line in lines:
    line_list = line.split(": ")
    my_dict[line_list[0]] = line_list[1]

print(my_dict)