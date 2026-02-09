'''🎯 Desafio de Entrevista (Encapsulamento)
Vamos juntar tudo o que você aprendeu até agora numa função utilitária.

Cenário: A Cezcom precisa de uma função padronizada para contar tokens (de forma simplificada) antes de enviar para a API da OpenAI, para não estourar o orçamento.

Sua Missão:

Crie uma função chamada estimar_custo.

Ela deve receber um argumento: texto.

Dentro dela:

Limpe o texto (strip).

Divida o texto em palavras (use .split(), que cria uma lista).

Conte quantas palavras tem (use len()).

Multiplique esse número por 0.05 (custo fictício por palavra).

Retorne o valor final.

Depois de criar a função, chame ela:

Python

custo = estimar_custo("  Inteligência Artificial na Cezcom  ")
print(f"Custo estimado: R$ {custo}")
Consegue montar essa estrutura def? Manda o código!'''



def estimar_custo(texto_recebido):
    # 1. Limpa e quebra em lista. GUARDE ISSO numa variável.
    lista_palavras = texto_recebido.strip().split()
    
    # 2. Conta quantos itens tem na LISTA (não no texto)
    qtd_palavras = len(lista_palavras)
    
    # 3. Calcula o preço
    valor_final = qtd_palavras * 0.05
    
    # 4. Entrega o valor calculado
    return valor_final

# Testando
custo = estimar_custo("  Inteligência Artificial na Cezcom  ")
print(f"Custo estimado: R$ {custo}")


frases = [
    "  O que é RAG? ", 
    "Python é legal", 
    "  Cezcom contrata  "
]

custo_total = 0

for frase in frases:
    
    # 1. Chame a função estimar_custo para a frase atual
    resultado = estimar_custo(frase)
    # 2. Some o resultado na variável custo_total (acumulador)
    custo_total = resultado + custo_total

print(f"Custo total do lote: R$ {custo_total}")