thisset = {"apple", "banana", "mango"}
thisset.remove("apple")

print(thisset)

# remove farklı yol
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# Bir öğeyi kaldırmak için pop() yöntemini de kullanabilirsiniz, ancak bu yöntem rastgele bir öğeyi kaldırır
# pop sildiği öğeyi geri döndürür
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(thisset)
print("kaldırılan oge: ", x)

# clear metodu kümeyi temizler
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# del metodu komple kümeyi siler
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) # silindiği için hata döndürür