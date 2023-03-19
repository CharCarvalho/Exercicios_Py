num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
opera = str(input("Escolha entre +-*/: "))

if (opera == "+"):
    print("A soma entre {} e {} é {}".format(num1, num2, num1+num2))
elif (opera == "-"):
    print("A subtração entre {} e {} é {}".format(num1, num2, num1-num2))
elif (opera == "*"):
    print("A multiplicação entre {} e {} é {}".format(num1, num2, num1*num2))
elif ((opera == "/") and (num2 != 0)):
    print("A divisão entre {} e {} é {}".format(num1, num2, num1/num2))
else:
    print("Não é possível dividir por 0")