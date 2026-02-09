'''Exercício 1: O Filtro de Segurança (Guardrails)
Cenário: A Cezcom não pode permitir que a IA leia documentos confidenciais. Tarefa:

Use a mesma base_de_conhecimento.

Busque por "cezcom".

Regra Adicional: Só adicione na lista se confidencial for False.

No final, imprima a lista. (Deveria vir apenas o documento "Onboarding", pois o "Política de IA" é confidencial).'''

base_de_conhecimento = [
    {
        "id": 101, 
        "titulo": "Política de IA", 
        "conteudo": "A Cezcom utiliza modelos GPT-4 para automação interna.",
        "confidencial": True
    },
    {
        "id": 102, 
        "titulo": "Receita de Bolo", 
        "conteudo": "Misture farinha e açúcar por 10 minutos.",
        "confidencial": False
    },
    {
        "id": 103, 
        "titulo": "Onboarding", 
        "conteudo": "Bem-vindo à Cezcom! Aqui inovamos com RAG e Python.",
        "confidencial": False
    },
    {
        "id": 104, 
        "titulo": "Logs do Servidor", 
        "conteudo": "Erro 404 na API de pagamento.",
        "confidencial": True
    }
]

termo_busca = "cezcom"

documentos_filtrados = []

erros_encontrados =[]

'''for doc in base_de_conhecimento:
    if doc["confidencial"] == False: # perguntar a diferença do in e do ==
        if termo_busca in doc["conteudo"].lower():
            documentos_filtrados.append(doc["conteudo"])

print(documentos_filtrados)

for doc in base_de_conhecimento:
    conteudo = doc['conteudo']
    if "erro" in conteudo.lower() or "404" in conteudo:
        erros_encontrados.append(doc['id'])

print(erros_encontrados)'''

#unindo for
'''Tente reescrever seu código anterior usando apenas um for.

Requisitos:

Percorra base_de_conhecimento.

Use if/elif ou if/if independentes? (Pense: um documento pode ser relevante E ter erro ao mesmo tempo?)

Preencha as duas listas (documentos_filtrados e erros_encontrados) na mesma passada.

Manda o código otimizado!'''

for doc in base_de_conhecimento:
    conteudo = doc['conteudo']
    if "erro" in conteudo.lower() or "404" in conteudo:
        erros_encontrados.append(doc['id'])

    if doc["confidencial"] == False:
        if termo_busca in doc["conteudo"].lower():
            documentos_filtrados.append(doc["conteudo"])

print(documentos_filtrados)

print(erros_encontrados)



