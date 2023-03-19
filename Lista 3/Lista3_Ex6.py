numA = int(input("Digite o primeiro numero: "))
numB = int(input("Digite o segundo numero: "))

if (numA%numB == 0):
    print("{} é divisivel por {}".format(numA, numB))
else:
    print("{} não é divisivel por {}".format(numA, numB))