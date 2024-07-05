# JSON, veri depolamak ve değiş tokuş etmek için kullanılan bir sözdizimidir.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Elinizde bir Python nesnesi varsa, json.dumps() yöntemini kullanarak bunu bir JSON dizesine dönüştürebilirsiniz.
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)