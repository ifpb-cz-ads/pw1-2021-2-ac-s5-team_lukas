velocidade = int(input('Informe a velocidade em km/h:'))


if velocidade > 80:
    print('Velocidade acima do permitido. O condutor foi multado')
    print('O valor da multa será de:', (velocidade - 80) * 5)
else:
    print('Velocidade dentro do limite')
