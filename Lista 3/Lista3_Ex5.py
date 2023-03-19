nome = str(input("Digite o nome do funcionário: "))
uteis = int(input("Digite a quantidade de dias uteis: "))
horas_t = int(input("Quantidade de horas trabalhadas por dia: "))
pag_hora = int(input("Pagamento por horas: "))
salario = (uteis*8*pag_hora)
valor_extra = 0
salario_b = 0

if horas_t > 8:
    valor_extra = (horas_t - 8)*(uteis)*(pag_hora*0.5)
    salario_b = salario + valor_extra
    print("O/A {} trabalhou {} hora a mais por dia e vai receber o bonus de R${}, sendo o salario final de {}".format(nome, horas_t -8, valor_extra, salario_b))
else:
    print("O/A {} não trabalhou hora extra, portanto o salário foi de {}".format(nome, salario))

