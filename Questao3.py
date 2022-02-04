salario = float(input('Informe o salário: '))

if salario > 1250:
    aumento1 = salario * 10 / 100
    salario_maior = salario + aumento1
    print('O valor do aumento é:', aumento1)
    print('O novo salário é de:', salario_maior)
elif salario <= 1250:
    aumento2 = salario * 15 / 100
    menor = salario + aumento2
    print('O valor do aumento é:', aumento2)
    print('O novo salário é de:', menor)

