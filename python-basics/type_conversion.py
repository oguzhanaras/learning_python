# tip dönüşümleri

# int()

# float to int
x = 5.5
print(type(x))

y = int(x)
print(type(y))


# bool to int
x = True
y = int(x)
print(y, type(y))  #true 1 false 0 a eşittir


# str to int
x = "5"
y = int(x)
print(y, type(y))

# float


# int to float
x = 5
y = float(x)
print(y, type(y))


# bool to float
x = True
y = float(x)
print(y, type(y))


# bool
# 0 false uretir onun dısındaki değerler true doner
x = 1
y = bool(x)
print(y, type(y))

x =-5
y = bool(x)
print(y, type(y))


x = 0
y = bool(x)
print(y, type(y))

# str to bool
# içi boş olan stringler false dondurur diğerleri true
x = ""
y = bool(x)
print(y, type(y))


x = "aras"
y = bool(x)
print(y, type(y))