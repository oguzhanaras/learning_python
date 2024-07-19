liste = ["345", "sadas", "324a", "14", "kemal"]

try:
    for i in liste:
        if i.isdigit():
            print(i)
except:
    print("error")
finally:
    print("finally")