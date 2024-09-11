import re

text = """
Hello,
Here are some email addresses you can contact:
1. m.kemal@example.com
2. jane_smith1234@gmail.com
3. info@mycompany.com
4. M_JORDAN@NBA.GOV
5. info2@turkiye.gov.tr
6. contact@mymail.c
7. trabzon@61.com
"""

pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}\.*[a-zA-Z]*"

matches = re.findall(pattern, text)

print(matches)