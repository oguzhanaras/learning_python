user_data = {
    'John': {'Minecraft': 120, 'Among Us': 45, 'Valorant': 90},
    'Emily': {'Minecraft': 55, 'Tetris': 90, 'Call of Duty': 80},
    'Peter': {'Tetris': 100, 'Among Us': 30, 'FIFA': 75},
    'Sophie': {'Among Us': 50, 'Minecraft': 70, 'FIFA': 60},
    'Mike': {'Tetris': 110, 'Minecraft': 30, 'Call of Duty': 70},
    'Sara': {'FIFA': 45, 'Minecraft': 40, 'Among Us': 35},
    'Alex': {'Call of Duty': 100, 'Valorant': 70, 'FIFA': 80},
    'Natalie': {'Tetris': 45, 'FIFA': 50, 'Minecraft': 30},
    'Chris': {'Call of Duty': 60, 'Valorant': 75, 'Among Us': 50},
    'Isabella': {'Tetris': 35, 'Minecraft': 60, 'FIFA': 45}
}

info = {
    "minecraft": {
        "sure": 0,
        "kisi": 0
    },
    "tetris": {
        "sure": 0,
        "kisi": 0
    },
    "amongus": {
        "sure": 0,
        "kisi": 0
    },
    "valorant": {
        "sure": 0,
        "kisi": 0
    },
    "callofduty": {
        "sure": 0,
        "kisi": 0
    },
    "fifa": {
        "sure": 0,
        "kisi": 0
    }
}
toplam = 0

for key, value in user_data.items():
    for item in value.items():
        if item[0] == "Minecraft":
            info["minecraft"]["sure"] += item[1]
            info["minecraft"]["kisi"] += 1
            toplam += item[1]

        elif item[0] == "Among Us":
            info["amongus"]["sure"] += item[1]
            info["amongus"]["kisi"] += 1
            toplam += item[1]

        elif item[0] == "Valorant":
            info["valorant"]["sure"] += item[1]
            info["valorant"]["kisi"] += 1
            toplam += item[1]

        elif item[0] == "FIFA":
            info["fifa"]["sure"] += item[1]
            info["fifa"]["kisi"] += 1
            toplam += item[1]

        elif item[0] == "Tetris":
            info["tetris"]["sure"] += item[1]
            info["tetris"]["kisi"] += 1
            toplam += item[1]
        else:
            info["callofduty"]["sure"] += item[1]
            info["callofduty"]["kisi"] += 1
            toplam += item[1]

a = 0
b = ""
for key, value in info.items():
    if value["sure"] > a:
        a = value["sure"]
        b = key

print(f"minecraft: {info["minecraft"]["sure"]}, tetris: {info["tetris"]["sure"]}, amongus: {info["amongus"]["sure"]},"
      f" valorant: {info["valorant"]["sure"]}, fifa: {info["fifa"]["sure"]}, "
      f"callofduty: {info["callofduty"]["sure"]}")

print(f"toplam oyun saati: {toplam}")
print(f"en cok oynanan oyun {b}, saati: {a}")
