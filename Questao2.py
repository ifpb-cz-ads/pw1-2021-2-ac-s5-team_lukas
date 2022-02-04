numero1 = int(input('Informe o primeiro valor: '))
numero2 = int(input('Informe o segundo valor: '))
numero3 = int(input('Informe o terceiro valor: '))

def maior(numero1, numero2, numero3):
    if (numero1 > numero2) and (numero1 > numero3):
        maiorNumero = numero1
    elif (numero2 > numero1) and (numero2 > numero3):
        maiorNumero = numero2
    else:
        maiorNumero = numero3
    print("O maior número é: ", maiorNumero)

def menor(numero1, numero2, numero3):
    if (numero1 < numero2) and (numero1 < numero3):
        menorNumero = numero1
    elif (numero2 < numero1) and (numero2 < numero3):
        menorNumero = numero2
    else:
        menorNumero = numero3
    print("O menor número é: ", menorNumero)
    
maior(numero1, numero2, numero3)
menor(numero1, numero2, numero3)

