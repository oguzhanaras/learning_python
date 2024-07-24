def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        deger = 1
        for i in range(1, n + 1):
            deger *= i
        return deger

while True:
    islem = input("faktoriyelini almak istediğiniz sayı girin ya da cıkmak için q basın")
    if islem == 'q':
        print("program sonlanıyor")
        break
    else:
        print(factorial(int(islem)))
