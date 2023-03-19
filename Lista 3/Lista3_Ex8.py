idade = int(input("Digite a idade do nadador: "))

if (5 <= idade <= 7):
    print("Infantil")
elif (8 <= idade <= 10):
    print("Juvenil")
elif (11 <= idade <= 15):
    print("Adolescente")
elif (16 <= idade <= 30):
    print("Adulto")
elif (30 < idade):
    print("Senior")
else: 
    print("Muito nova para nadar!")