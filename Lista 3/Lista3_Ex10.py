import math
a = int(input("Digite o coeficiente a, que deve ser diferente de 0: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))

delta = (b**2)-4*a*c
if (a != 0) and (delta >= 0):
    x1 = ((-b) + math.sqrt(delta))/(2*a)
    x2 = ((-b) - math.sqrt(delta))/(2*a)
    print("As raízes reais de {}*x**2+{}*x+{} são iguais a {} e {}".format(a, b, c, x1, x2))
elif (a == 0):
    print("Como a é igual a 0, não configura uma equação de segundo grau!")
else:
    print("Não é possível determinar as raízes reais, pois o delta de valor {} é menor que 0!".format(delta))


