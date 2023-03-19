dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))
verifica = False

if ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 400 == 0) and (ano % 100 == 0)):
    verifica = True
else:
    verifica = False


if (0 < dia <= 31) and (0<mes<=12) and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 ):
    print("A data {}/{}/{} está correta!".format(dia, mes, ano))
elif (0 < dia <= 30) and (0<mes<=12) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("A data {}/{}/{} está correta!".format(dia, mes, ano))
elif (0 < dia <= 28) and (mes == 2):
    print("O formato para o mês de fevereiro está válido! {}/{}/{}".format(dia, mes, ano))
elif (dia == 29) and (mes == 2) and (verifica == True):
    print("O formato {}/{}/{} só é valido para anos bissextos!".format(dia, mes, ano))
else:
    print("Não é um formato válido!")