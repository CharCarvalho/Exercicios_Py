dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))

if (0 < dia <= 31) and (0<mes<=12) and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 ):
    print("A data {}/{} está correta!".format(dia, mes))
elif (0 < dia <= 30) and (0<mes<=12) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("A data {}/{} está correta!".format(dia, mes))
elif (0 < dia <= 28) and (mes == 2):
    print("O formato para o mês de fevereiro está válido! {}/{}".format(dia, mes))
elif (dia == 29) and (mes == 2):
    print("Esse formato só é valido para anos bissextos!")
else:
    print("Não é um formato válido!")