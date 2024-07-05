username = input("Enter username:")
print("Username is: " + username)


# simple login system
ad = "admin"
pas = "123"

username = input("enter username")
password = input("enter password")

try:
    if username == ad and password == pas:
        print("giris basarılı")
    else:
        raise False
except:
    print("bilgiler hatalı")
else:
    print("hosgeldiniz")
finally:
    print("program is over")
