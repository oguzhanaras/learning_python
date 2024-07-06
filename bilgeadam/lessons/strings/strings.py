# string len
my_string = "Hello World"
x = len(my_string)
print(x)



# string concatenation
first = "aras"
sec = "oguz"


# string addition
sentence = first + " " + sec
print(sentence)

# % operator
sentence = "%s, %s"% (first, sec)
print(sentence)

# .format() string method
sentence = "{}, {}".format(first, sec)
print(sentence)

a = "bilgeAdam"
b = "kursu"
c = "python"

sentence = "{0} {2} {1}".format(a, b, c)
print(sentence)


# f string
sentence = f"{a} {b} {c}"
print(sentence)


# string multiplication
letter = "7"
print(letter * 3)
print(int(letter * 3) + 3)


# string indexxing and slicing

# indexing
word = "BilgeAdam"
       #012345678
       #987654321
print(len(word))

print(word[0])
print(word[-9])


print(word[-len(word)])

# slicing
word = "BilgeAdam"
print(word[0:5]) #start:stop
print(word[5:]) #5 ten basla sonuna kadar git
print(word[5:10]) # hata vermez
print(word[-3:-1])

print(word[2:-2:2]) #3. parametre aadımlama saglar start:stop:step
print(word[-1:-5:-1])


# in not operator
word = "BilgeAdam"
print("B" in word)
print("Bilge" in word)
print("z" not in word)


# escape
txt = "hello\nWorld"
print(txt)

txt = "hello\bWorld"
print(txt)

txt = "hello\tWorld"
print(txt)