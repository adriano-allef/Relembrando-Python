import json

resposta_api = '{"id": "chatcmpl-123", "mensagem": "O RAG conecta dados externos à LLM", "tokens": 15}'

dados_convertidos = json.loads(resposta_api)

print(f'A IA disse: {dados_convertidos["mensagem"]}')

tokens = dados_convertidos["tokens"]

print(tokens)

if tokens > 10:
    print('Custo Alto')