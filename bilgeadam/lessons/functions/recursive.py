def myfunc2():
    return 'hello'


def myfunc1(name):
    combined = myfunc2() + " " + name
    return combined

print(myfunc1("John"))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

factorial(5)

# Çalışan-ast ilişkisini tanımlayan sözlük
import time    # time Python Standard Library

calisan_hiyerarsi1 = {
    'CEO': ['CTO', 'CFO', 'CMO'],
    'CTO': ['Dev1', 'Dev2'],
    'CFO': ['Acc1', 'Acc2', 'Acc3'],
    'Dev1': ['Intern1', 'Intern2', 'Intern3', 'Intern4']
}

calisan_hiyerarsi2 = {
    'CEO': ['CTO', 'CFO'],
    'CTO': ['Dev1', 'Dev2', 'Dev3'],
    'CFO': ['Acc1', 'Acc2', 'Acc3'],
    'Dev1': ['Intern1', 'Intern2', 'Intern3', 'Intern4'],
    'Dev2': ['Intern1', 'Intern2', 'Intern3', 'Intern4']
}

def toplam_ast(hiyerarsi: dict, calisan: str):
    """
    Bir hiyerarşik düzende bir çalışanın toplam astlarını hesaplar
    :param hiyerarsi: sözlük tipinde hiyerarşi verisi
    :param calisan: string tipinde çalışan kodu
    :return: toplam ast sayısını integer olarak döndürür
    """
    toplam = 0    # Toplam ast sayısını tutmak için
    if calisan not in hiyerarsi:
        return 0

    astlar = hiyerarsi[calisan]   # astların listesi
    toplam += len(astlar)
    print(f"{calisan} kişisinin {toplam} alt çalışanı vardır")
    time.sleep(1)
    for ast in astlar:
        ast_sayi = toplam_ast(hiyerarsi, ast)
        print(f"{ast} kişisine bakıldı, bu kişinin {ast_sayi} kadar astı vardır.")
        time.sleep(1)
        toplam += ast_sayi
        time.sleep(1)

    return toplam


toplam_ast(calisan_hiyerarsi1, "CEO")
toplam_ast(calisan_hiyerarsi1, "CTO")

toplam_ast(calisan_hiyerarsi2, "CTO")


