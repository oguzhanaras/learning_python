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

minecraft = 0
tetris = 0
amongus = 0
valorant = 0
callofduty = 0
fifa = 0

for key, value in user_data.items():
    for item in value.items():
        print(item[0])
        if item[0] == "Minecraft":
            minecraft += item[1]
        elif item[0] == "Among Us":
            amongus += item[1]
        elif item[0] == "Valorant":
            valorant += item[1]
        elif item[0] == "FIFA":
            fifa += item[1]
        elif item[0] == "Tetris":
            tetris += item[1]
        else:
            callofduty += item[1]

print(f"minecraft: {minecraft}, tetris: {tetris}, amongus: {amongus}, valorant: {valorant}, fifa: {fifa}, "
      f"callofduty: {callofduty}")
print(f"toplam oyun saati: {fifa + amongus + valorant + callofduty + tetris}")