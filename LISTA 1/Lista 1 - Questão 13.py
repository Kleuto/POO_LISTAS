sensor1 = float(input("Digite a temperatura do sensor 1: "))
sensor2 = float(input("Digite a temperatura do sensor 2: "))
sensor3 = float(input("Digite a temperatura do sensor 3: "))

temperatura_media = (sensor1 + sensor2 + sensor3) / 3

print(f"A temperatura média é: {temperatura_media:.2f} °C")