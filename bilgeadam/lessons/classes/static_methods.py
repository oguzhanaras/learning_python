# static method sınıfa ya da örneklere ait olmayan genel amaçlı fonksiyonlardır
# bunlar sınıfın veya örneklerin durumuna erişim gerektirmez ve genel yardımcı fonksiyonlardır

class Mathematics:

    @staticmethod
    def add5(number):
        return number + 5

    @staticmethod
    def sub5(number):
        return number - 5


x = 10

print(Mathematics.add5(x))

