kume = {"aras", "ogrenme", "eleman"}
kume2 = {"aras", "farklı"}

# add kumelere veri ekler
kume.add("eleman")
print(kume)

# clear kumeyi bosaltır fakat silmez
kume.clear()
print(kume)

# copy kumenin bir kopyasını dondurur
x = kume.copy()
print(x)

# difference ortak olamayanlari bir küme olarak dondurur
x = kume - kume2
print(x)

# discard belirtilen ogeyi kaldırır
kume.discard("aras")
print(kume)

# intersectin kesişim olan ogeleri kume olarak dondurur
x = kume.intersection(kume2)
print(x)

# pop kumeden rastgele eleman kaldırır
kume.pop()
print(kume)

# remove belirtilen ogeyi kaldırır
kume.remove("aras")
print(kume)

# union kumelerin birleişimi olan bir kume dondurur
x = kume.union(kume2)
print(x)

# update birleştirir ve gunceller
kume.update(kume2)
print(kume)