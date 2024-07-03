# input
name = input("adını gir: ")
surname = input("soyadını gir: ")

print("your name is: " + name + surname)

numerator = input("pay gir: ")
denominator = input("payda gir: ")

result = int(numerator) / int(denominator)

print(result, type(result))


# unicode
prompt = "unicode değerini istediğiniz karakter giriniz:"
character = input(prompt)
unicode_value = ord(character)
print(character, unicode_value, type(unicode_value))


# chr
prompt = "unicode değerini istediğiniz karakter giriniz:"
character = int(input(prompt))
unicode_value = chr(character)
print(f"unicode value: {unicode_value} - character: {character}")