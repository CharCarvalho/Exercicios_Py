sal_i = float(input("Digite o salário inicialmente: "))
sal_d = float(input("Digite o salário depois do aumento: "))

aum = sal_d - sal_i
porc = (aum/sal_i)*100

print("O percentual de aumento foi de {}%".format(porc))
