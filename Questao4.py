
distancia = int(input('Informe a dintância a ser percorrida em km:'))

if distancia <= 200:
    preco = distancia * 0.50
    print('O preço total da passagem é de:', preco)
else:
    preco = distancia * 0.45
    print('O preço total da passagem é de:', preco)

