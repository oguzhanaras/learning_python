# pop metodu belirtilen keyi kaldırır
thisdict = {
    "adi": "aras",
    "yas": 29
}

thisdict.pop("yas")
print(thisdict)

#popitem son eklenen uyeyi kaldırır
thisdict = {
    "adi": "aras",
    "yas": 33
}

thisdict["sonekle"] = "sonuncu"
print(thisdict)
thisdict.popitem()
print(thisdict)


# del ile belirtilen anahtar ogesini ya da tamamını silebilir
thisdict = {
    "adi": "aras",
    "yas": 33
}

del thisdict["yas"]
print(thisdict)

del thisdict
print(thisdict)  # dict silindigi icin hata doner

# clear metodu dict i temizler
thisdict = {
    "name": "aras",
    "age": 66,
    "edu": "bilgeadam"
}

thisdict.clear()
print(thisdict) # dict silinmediği için boş dict ogesi doner