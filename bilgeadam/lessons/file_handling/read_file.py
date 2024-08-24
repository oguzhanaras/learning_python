import os
os.getcwd()
os.chdir("bilgeadam/lessons/file_handling")
os.getcwd()

# open() fonksiyonu
file = open("numbers.txt")
print(type(file))
print(file)
# read() metodu
file.read()
file.close()

file = open("numbers.txt", "rt")
file.read(5)
file.close()

# readline() metodu
file = open("numbers.txt")
file.readline().strip()
file.readline().strip()
file.readline().strip()
file.close()

# for loop
file = open("numbers.txt")
for x in file:
    print(x.strip())


#dosya yolu
file = open("new_folder/pi.txt")
file.read()

for line in file:
    print(line.strip(), end="")