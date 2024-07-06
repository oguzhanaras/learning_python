# kullanıcıdan daire yarıçapı alan ve daire alanı ve çevresşbş hesaplayıp ekrana cıktı veren programı yazdırınız
import math

r = float(input("Enter a r "))

alan = (math.pi * r ** 2)
cevre = 2 * math.pi * r

print(f"alan: {round(alan, 2)}, cevre: {round(cevre)}")