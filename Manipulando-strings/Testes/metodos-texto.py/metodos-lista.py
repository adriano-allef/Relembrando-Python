import sys

# Força a saída (print) e entrada (input) a usar UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

lista = ['abacaxi', 'batata', 'arroz', 'feijão']
print(lista)

adicionar_final = lista.append('tomate')
print(lista)

remover_ultimo = lista.pop()
print(lista)

contar_itens = len(lista)

if contar_itens == 0:
    print('A lista tem 0 itens!'),

elif contar_itens == 1:
    print('a lista tem 1 item!'),

else: print('A lista contém', contar_itens, 'itens"')

achar_posicao = lista.index('arroz')
print(achar_posicao)