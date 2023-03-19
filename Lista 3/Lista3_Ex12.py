nac1 = float(input("Digite a nota da NAC do primeiro semestre: "))
am1 = float(input("Digite a nota da AM do primeiro semestre: "))
ps1 = float(input("Digite a nota do PS do primeiro semestre: "))

nac2 = float(input("Digite a nota da NAC do segundo semestre: "))
am2 = float(input("Digite a nota da AM do segundo semestre: "))
ps2 = float(input("Digite a nota do PS do segundo semestre: "))

freq = int(input("Digite uma frequencia entre 0 e 100%: "))

media1 = ((nac1*2) + (3*am1) + (5*ps1))/10
media2 = ((nac2*2) + (3*am2) + (5*ps2))/10

mediaf = ((4*media1)+(6*media2))/10

if (mediaf >=6) and (freq > 70):
    print("Alune aprovade!")
elif(4 <= mediaf < 6) and (freq > 70):
    print("Alune está de exame!")
elif(mediaf < 4) and (freq > 70):
    print("Alune reprovade!")
else:
    print("Alune reprovou por falta!")