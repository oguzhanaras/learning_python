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





class RocketNotReadyError(Exception):
    pass


def personnel_check(crew: list):   # Personel kontrol
    try:
        # Ekip üyelerinin isimlerini yazdıracağız.
        print("Kaptanın Adı:", crew[0])
        print("Pilotun Adı:", crew[1])
        print("Teknisyenin Adı", crew[2])
        print("Navigatörün Adı:", crew[3])    # Burada hata verecek ekip eksik
    except IndexError as e:
        raise RocketNotReadyError("Ekip eksik") from e


def fuel_check(level: int):
    try:
        print(level / 0)     # Yakıt seviyesi hesaplama hatası
    except ZeroDivisionError as e:
        raise RocketNotReadyError("Yakıt göstergesinde sorun var.")


check_list = [personnel_check(["Salim", "Ezgi", "Aras", "Deniz"]), fuel_check(100)]

for check in check_list:
    try:
        check
    except RocketNotReadyError as f:
        print(f"Roket hazır değil hatası: {f}, nedeni: {f.__cause__}")
