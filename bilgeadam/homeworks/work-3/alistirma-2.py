print("cıkmak için q ya basın")

while True:
    islem = input("cümle giriniz ya da cıkmak için q ya basın: ").lower().strip("!.,:")

    if islem == "q":
        print("program sonlanıyor..")
        break
    else:
        if islem == islem[::-1]:
            print("palindrom")
        else:
            print("palindrom değil")