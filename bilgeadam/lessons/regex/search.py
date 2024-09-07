import re

text = "Ofisin telefon numarası 312-444-44-44."


# re.search ile bir ifade aranacak ve bir match nesnesi dondurulecektir
match = re.search("...-...-..-..", text)
print(match)

# match nesnesine ait span metodu start ve end indejskerini tuple olarak dondurur
print(match.span())

# match ornegine ait start ve end metodları
print(f"Start: {match.start()}, End: {match.end()}")

# match ornegine ait string ozelligi (attr) aramanın yapıldıgı metni saklar
print(match.string)

# match ornegine ait grup() metodu if eşleşme var ise eşleşen substr dondurur
print(match.group())