weather_data = {
    'Istanbul': {'temperature': 20, 'condition': 'Cloudy'},
    'Ankara': {'temperature': 18, 'condition': 'Sunny'},
    'Izmir': {'temperature': 25, 'condition': 'Rainy'}
}


class Weather:

    def __init__(self, city_name, temperature, condition):
        self.city_name = city_name
        self.temperature = temperature
        self.condition = condition

    def get_weather(city: str):

        values = weather_data.get(city)
        print(city, values["temperature"], "derece ve", values["condition"])

    def add_weather(city, temperature, condition):
        weather_data[city] = {
            "temperature": temperature,
            "condition": condition
        }




while True:
    islem = input("(s)orgula --- (e)kle --- (c)ıkıs")

    if islem == "s":
        get_city = input("sehir gir: ")
        Weather.get_weather(get_city)

    elif islem == "e":

        add_city = input("eklemek istediginiz sehir adi: ")
        city_temperature = input("sehrin sıcaklık derecesi: ")
        city_condition = input("durum: ")

        Weather.add_weather(add_city, city_temperature, city_condition)

    elif islem == "c":
        print("program sonlanıyor")
        break

    else:
        print("hatalı islem")

