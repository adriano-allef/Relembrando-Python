'''arquivo = open('conceito_RAG.txt', encoding='utf-8')
print(arquivo.read())
arquivo.close()'''

with open('conceito_RAG.txt', 'r', encoding='utf-8') as arquivo:
    linha = arquivo.readline()
    while linha:
        print(linha)
        linha = arquivo.readline()

with open('conceito_RAG.txt', 'a', encoding='utf-8') as arquivo:
    texto = arquivo.write('\nProximo passo: MCP.')
    


