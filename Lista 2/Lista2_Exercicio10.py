dist = float(input("Digite a distância percorrida, em metros: "))
temp = float(input("Digite o tempo percorrido: "))

vel_m = dist/temp
vel_k = (vel_m)*3.6

print("A velocidade média em metros/s é", vel_m, "m/s.")
print("A velocidade média em km/h é", vel_k, "km/h.")