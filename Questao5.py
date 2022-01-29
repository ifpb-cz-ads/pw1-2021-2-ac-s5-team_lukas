PrimeiroNum = int(input('Digite o primeiro número:'))
SegundoNum = int(input('Digite o segundo número:'))
Operacao = str(input('Informe o símbolo do tipo de operação: adição (+), subtração (-), multiplicação (*) e divisão (/):'))

if Operacao == '+':
    Resultado = PrimeiroNum + SegundoNum
    print('O tipo de operação escolhida foi adição e o resultado é:', Resultado)
elif Operacao == '-':
    Resultado = PrimeiroNum - SegundoNum
    print('O tipo de operação escolhida foi subtração e o resultado é:', Resultado)
elif Operacao == '*':
    Resultado = PrimeiroNum * SegundoNum
    print('O tipo de operação escolhida foi multiplicação e o resultado é:', Resultado)
elif Operacao == '/':
    Resultado = PrimeiroNum / SegundoNum
    print('O tipo de operação escolhida foi divisão e o resultado é:', Resultado)
