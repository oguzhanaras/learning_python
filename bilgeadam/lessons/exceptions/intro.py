# Exceptions, bir program çalışırken ortaya çıkan beklenmedik hataları ifade eder.
# Bu hatalar, programınızın akışını sekteye uğratabilir.
# Python'da, try ... except yapıları kullanarak hataları yakalayabiliriz.
# Bu sayede program hata oluştuğunda nasıl davranması gerektiğini bilecektir.

try:
    print(10 / 0)
except ZeroDivisionError:
    # Bu kod bloğu ZeroDivisionError hatası meydana gelirse çalışır
    print("Sıfıra bölme yapılamaz!")


try:
    print(10 / 0)
except:
    # Bu kod bloğu herhangi bir hata oluşursa çalışır
    print("Sıfıra bölme yapılamaz!")


# named attributes
try:
    x = int(input("Bir sayı giriniz:"))
    print(f"{x} sayısının karesi {x ** 2}")
except ValueError as e:
    print(e)
    print(e.args)


# chained exceptions
try:
    try:
        y = int(input("Bir sayı giriniz:"))
        print(f"{y} sayısının karesi {y ** 2}")
    except ValueError as e:
        print(y ** 2)
except NameError as e:
    print(f"Hata: {e}")


# implicit_chaining (dolaylı zincirleme)
try:
    a = [1, 2]
    print(a[4])   # IndexError
    x = 1 / 0
except IndexError as e:
    print("IndexError yakalandı.")
except ZeroDivisionError as e:
    print("ZeroDivisionError yakalandı.")

