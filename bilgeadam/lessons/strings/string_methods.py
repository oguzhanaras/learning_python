txt = "hello my uppercase"  # harfleri buyutur
print(txt.upper())

txt = "HELLO MY LOWERCASE" # harfleri kucultur
print(txt.lower())

print(txt.count("e")) #istenilen harfin kaç kere oldugunu dondurur

txt = "HELLO MY LOWERCASE"
print(txt.title()) # bas harfleri buyultur diğer harfleri kucultur

print(txt.startswith("H"))

print(txt.endswith("HELLO"))


print(txt.find("M")) # istenilen harfin indexinin dondurur yoksa -1 dondurur

print(txt.index("O")) # istenilen harfin indexini dondurur yoksa error


# split belirtilen karakter ile stryi böler ve geriye liste olarak dondurur
print("txt merhaba aras".split(" "))



# strip str baş ve sonunda belirtilen ifadeyi kırpar
name = "  BilgeAdam  "
print(name.strip())