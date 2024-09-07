import re

with open("students.txt", encoding="utf-8") as file:
    text = file.read()

pattern = r"...-...-..-.."

matches = re.findall(pattern, text)
print(matches)

# re.finditer() paternin metindeki tüm eşleşmeleri için bir iter olusturur
for match in re.finditer(pattern, text):
    print(match)
