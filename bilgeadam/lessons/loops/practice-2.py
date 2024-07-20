# Verilen uçuş verileri
# Uçuş kodu, Havayolu, Kalkış Havalimanı, Varış Havalimanı, Kalkış Zamanı, Varış Zamanı, Süre (dakika), Mesafe (mil)
flight_data = [
    {'flight_number': 'TK101', 'airline': 'Turkish Airlines', 'departure_airport': 'IST', 'arrival_airport': 'JFK', 'departure_time': '2023-10-01 08:00', 'arrival_time': '2023-10-01 18:10', 'duration': 610, 'distance': 4328},
    {'flight_number': 'LH202', 'airline': 'Lufthansa', 'departure_airport': 'FRA', 'arrival_airport': 'LAX', 'departure_time': '2023-10-01 09:30', 'arrival_time': '2023-10-01 22:50', 'duration': 800, 'distance': 5033},
    {'flight_number': 'BA303', 'airline': 'British Airways', 'departure_airport': 'LHR', 'arrival_airport': 'SFO', 'departure_time': '2023-10-01 11:15', 'arrival_time': '2023-10-01 22:15', 'duration': 660, 'distance': 4652},
    {'flight_number': 'AF404', 'airline': 'Air France', 'departure_airport': 'CDG', 'arrival_airport': 'JFK', 'departure_time': '2023-10-01 10:45', 'arrival_time': '2023-10-01 19:31', 'duration': 526, 'distance': 3150},
    {'flight_number': 'EK505', 'airline': 'Emirates', 'departure_airport': 'DXB', 'arrival_airport': 'LHR', 'departure_time': '2023-10-01 07:30', 'arrival_time': '2023-10-01 15:13', 'duration': 463, 'distance': 2969},
    {'flight_number': 'DL606', 'airline': 'Delta Air Lines', 'departure_airport': 'ATL', 'arrival_airport': 'JFK', 'departure_time': '2023-10-01 12:30', 'arrival_time': '2023-10-01 14:00', 'duration': 90, 'distance': 660},
    {'flight_number': 'UA707', 'airline': 'United Airlines', 'departure_airport': 'ORD', 'arrival_airport': 'LAX', 'departure_time': '2023-10-01 13:15', 'arrival_time': '2023-10-01 17:25', 'duration': 250, 'distance': 1513},
    {'flight_number': 'SQ808', 'airline': 'Singapore Airlines', 'departure_airport': 'SIN', 'arrival_airport': 'JFK', 'departure_time': '2023-10-01 11:30', 'arrival_time': '2023-10-02 06:30', 'duration': 1140, 'distance': 8283},
    {'flight_number': 'QF909', 'airline': 'Qantas', 'departure_airport': 'SYD', 'arrival_airport': 'LAX', 'departure_time': '2023-10-01 14:00', 'arrival_time': '2023-10-01 18:30', 'duration': 900, 'distance': 6513},
    {'flight_number': 'AA101', 'airline': 'American Airlines', 'departure_airport': 'JFK', 'arrival_airport': 'LHR', 'departure_time': '2023-10-01 15:00', 'arrival_time': '2023-10-01 21:00', 'duration': 360, 'distance': 2991},
]

new_list = [round(i["distance"] / (i["duration"] / 60), 2) for i in flight_data]
print(new_list)

def min_duration(mydict):
    return mydict["duration"]

print("en kısa ucus: ", min(flight_data, key=min_duration))

# 3. Los Angeles Airport (LAX)'a yapılan seferlerin toplam mesafesini (distance) hesaplatın.
toplam = 0
for i in flight_data:
    if i["arrival_airport"] == "LAX":
        toplam += i["distance"]
print(toplam)