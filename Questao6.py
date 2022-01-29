
valor = float(input('Digite o valor total da casa:'))
salario = float(input('Digite o salário:'))
anos= int(input('Digite a quantidade de tempo em anos:'))
meses = anos* 12
prestacao = valor / meses

if prestacao >= salario * 30 / 100:
    print('Empréstimo não pode ser completado pois excede o limte de 30% do salário do interessado. Refaça o processo com uma quantidade maior de tempo')
else:
    print('O valor de cada parcela é', prestacao,2, 'e o número de parcelas ficou em', meses)
