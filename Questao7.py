
quantidade = float(input('Digite a quantidade de KWh consumidos:'))
tipo = str(input('Digite o tipo de instalação onde R para residências, I para indústrias e C para comércios:'))

if tipo == 'R' and quantidade <= 500:
    total_r = quantidade * 0.40
    print('O total a ser pago é de:', total_r)
elif tipo == 'R' and quantidade > 500:
    total_r = quantidade * 0.65
    print('O total a ser pago é de:', total_r)
elif tipo == 'C' and quantidade <= 1000:
    total_c = quantidade * 0.55
    print('O total a ser pago é de:', total_c)
elif tipo == 'C' and quantidade > 1000:
    total_c = quantidade * 0.60
    print('O total a ser pago é de:', total_c)
elif tipo == 'I' and quantidade <= 5000:
    total_i = quantidade * 0.55
    print('O total a ser pago é de:', total_i)
elif tipo == 'I' and quantidade > 5000:
    total_i = quantidade * 0.60
    print('O total a ser pago é de:', total_i)

    
