matches = {
 'Barcelona_Real_Madrid': (3, 2),
 'RealMadrid_ManchesterUnited': (1, 1),
 'ManchesterUnited_Barcelona': (2, 2)
}
team_points = {
 'Barcelona': 0,
 'RealMadrid': 0,
 'ManchesterUnited': 0
}


for key, value in matches.items():
    if value[0] > value[1]:
        team = key.split("_")[0]
        team_points[team] += 3
    elif value[0] == value[1]:
        team = key.split("_")
        team_points[team[0]] += 1
        team_points[team[1]] += 1
    else:
        team = key.split("_")[1]
        team_points[team] += 3