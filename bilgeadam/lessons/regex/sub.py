import re

text = "Python çok popüler bir dildir. Python nesne yönelimli bir programdır."

result = re.sub(r"Python", "Java", text)

print(result)