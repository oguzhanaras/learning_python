import requests


try:
    size = input("qr kodun buyuklugunu giriniz: ")
    data = input("qr kod oluşturacagınız url giriniz: ")
    url = f"http://api.qrserver.com/v1/create-qr-code/?data={data}&size={size}x{size}"

    res = requests.get(url)

    with open("myQR.png", "wb") as qr:
        qr.write(res.content)
except Exception as e:
    print("error", e)
else:
    print("request succes")