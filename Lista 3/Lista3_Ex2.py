num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("{} (num1) é maior que {} (num2)".format(num1, num2))
elif num1 < num2:
    print("{}(num2) é maior que {}(num1)".format(num2, num1))
else:
    print("{}(num1) e {}(num2) são iguais".format(num1, num2))