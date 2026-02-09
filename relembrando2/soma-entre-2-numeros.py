n1 = int( input ('Digite o primeiro número: ') )
n2 = int ( input ('Digite o segundo número: ') )
soma = n1 + n2
print(f'A soma entre {n1} e {n2} é: {soma}') #metodo mais moderno de formatação de string, a partir do python 3.6
print('A soma entre {} e {} é: {}'.format(n1, n2, soma)) #metodo mais antigo de formatação de string, a partir do python 2.6 