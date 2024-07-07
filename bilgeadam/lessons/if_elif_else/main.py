# conditional statements

# if
kosul = True

if kosul: # kosul true oldugu için içeriye gireer
    print("This is True")

kosul = False
if kosul:
    print("This is True")
else:
    print("This is False")


age = int(input("Enter your age: "))
if age >= 30:
    print("30 ya da daha buyuksun")
elif age >= 18:
    print("18-30")
else:
    print("18 den kucuksun")