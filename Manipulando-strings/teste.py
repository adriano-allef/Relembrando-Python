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

erros_encontrados = []

for doc in base_de_conhecimento:
    conteudo = doc['conteudo']
    
    # 1. Print dentro do loop para ver passando um por um
    print(f"Analisando: {conteudo}")

    # 2. Lógica correta do OU
    # Note que converti tudo pra minúsculo pra garantir
    if 'erro' in conteudo.lower() or '404' in conteudo:
        print("-> ACHEI UM ERRO AQUI!")
        erros_encontrados.append(doc['id'])

print("----------------")
print(f"IDs com erro: {erros_encontrados}")