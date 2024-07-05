# try bloğu bir kod bloğunu hatalara karşı test eder
# except bloğu hatayı ele almanızı sağlar
# else bloğu, hata olmadığında kodu çalıştırmanızı sağlar
# finally bloğu, try- ve except bloklarının sonucundan bağımsız olarak kodu çalıştırmanızı sağlar.

try:
  print(x)
except:
  print("An exception occurred")


# else anahtar sözcüğünü, herhangi bir hata oluşmadığında çalıştırılacak bir kod bloğu tanımlamak için kullanabilirsiniz
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# finally try blogu dogru olsun ya da olmasın kod sonunda calıstırılır
x = 1
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



# raise metodu ile ne tür bir hata oluşturulacağını ve kullanıcıya yazdırılacak metni tanımlayabilirsiniz.
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
