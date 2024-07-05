thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 1986

print(thisdict)


# update ile var olan veriyi guncelleyebiliriz
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({"year": 2020})

print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# eger veri yoksa yebi veri ekler
thisdict.update({"okey": 10})

print(thisdict)