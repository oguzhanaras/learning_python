#Elinizde uzunca bir string olsun.
#Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

my_str = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

while True:
    islem = input("aramak istediginiz karakteri girin ya da cıkmak icin quit yazın")

    if islem == "quit":
        print("bye")
        break
    else:
        print(my_str.lower().count(islem))

