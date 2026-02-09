import sys

# Força a saída (print) e entrada (input) a usar UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

frase = '  Essa frase é um  Tes t e!'
print('Frase original:', frase)

metodo_strip = frase.strip()
print (metodo_strip)

metodo_lower = frase.lower()
print (metodo_lower)

metodo_replace = frase.replace("Tes t e", "teste")
print (metodo_replace)

metodo_split = frase.split()
print (metodo_split)

if "teste" in metodo_replace:
    print(True),
else: 
    print(False)

tudo_junto = frase.replace("Tes t e", "teste").strip().lower().replace("essa", "Essa")
print(tudo_junto)