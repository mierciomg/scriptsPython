n1 = int(input('informe um numero'))
n2 = int(input('informe outro número'))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisaoExata = n1 // n2
restoDaDivisao = n1 % n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
print('A subtração entre {} e {} é igual a {}'.format(n1, n2, subtracao))
print('A multiplicação {} e {} é igual a {}'.format(n1, n2, multiplicacao))
print('A divisão {} e {} é igual a {}'.format(n1, n2, divisao))
print('{} elevado a {} é igual a {}'.format(n1, n2, potencia))
print('A divisão exata de {} por {} é igual a {}'.format(n1, n2, divisaoExata))
print('O resto da divisão de {} por {} é igual a {}'.format(n1, n2, restoDaDivisao))