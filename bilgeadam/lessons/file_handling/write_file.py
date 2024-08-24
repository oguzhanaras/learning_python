import os
os.getcwd()
os.chdir("bilgeadam/lessons/file_handling")
os.getcwd()

file_name = "programming.txt"

with open(file_name, mode="w", encoding="utf-8") as file:
    file.write("programlamayı cok seviyorum")
    file.write("python benim hayatım")