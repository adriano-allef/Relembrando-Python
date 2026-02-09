'''Sua Missão (O Algoritmo de Busca)
Você precisa criar um script que percorra essa base e encontre apenas o que é relevante para responder a uma pergunta sobre a empresa.

Requisitos:

Crie uma lista vazia chamada documentos_relevantes.

Defina uma variável termo_busca = "cezcom".

Faça um loop for em base_de_conhecimento.

A Lógica (O Pulo do Gato): Verifique se o termo_busca está dentro do conteudo do documento.

Dica de Sênior: O texto no banco está com "Cezcom" (maiúsculo) e sua busca está "cezcom" (minúsculo). Lembre-se de normalizar (usar .lower()) antes de comparar, senão a busca falha!

Se encontrar, adicione (append) o dicionário inteiro na lista documentos_relevantes.

No final, imprima: "Foram encontrados X documentos sobre 'cezcom'".

Consegue codar isso? Esse exercício prova que você sabe manipular Dicionários dentro de Listas (o padrão JSON universal).'''

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

#lista vazia
documento_relevantes = []

termo_busca = "cezcom"

'''print(base_de_conhecimento[0]["conteudo"])
print(base_de_conhecimento[0]["conteudo"].split())'''

for doc in base_de_conhecimento:
    if termo_busca in doc["conteudo"].lower():
        documento_relevantes.append(doc)

print(documento_relevantes)