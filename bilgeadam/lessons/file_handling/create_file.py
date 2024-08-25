import os

os.getcwd()
os.chdir("bilgeadam/lessons/file_handling")
os.getcwd()

f = open("myfile.txt", "x")
f.close()

os.remove("myfile.txt")