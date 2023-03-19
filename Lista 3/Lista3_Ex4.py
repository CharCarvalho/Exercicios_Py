time1 = str(input("Digite o nome do primeiro time: "))
gol1 = int(input("Digite quantos gols o time 1 fez: "))
time2 = str(input("Digite o nome do segundo time: "))
gol2 = int(input("Digite quantos gols o time 2 fez: "))

if gol1 > gol2:
    print("O time {} venceu do time {}".format(time1, time2))
elif gol1 < gol2:
    print("O time {} venceu do time {}".format(time2, time1))
else:
    print("O time {} empatou com o time {}".format(time1, time2))

    