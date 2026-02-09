'''3. Exercícios Rápidos (Valendo a Vaga!)
Vamos treinar apenas esses métodos agora. Resolva aí no caderno:

Exercício A: Limpeza de Prompt (Strings)
Você recebeu um prompt sujo de um usuário: " Quero saber sobre RAG... ".

Remova os espaços extras.

Troque "..." por nada (string vazia "") para limpar a pontuação.

Converta tudo para minúsculo para padronizar.'''

prompt = " Quero saber sobre RAG... "

remover_espacos_srip = prompt.strip()
print(remover_espacos_srip)

tirar_3_pontos_replace = prompt.replace("...", "")
print(tirar_3_pontos_replace)

minusculo_lower = prompt.lower()
print(minusculo_lower)

resolucao = prompt.replace("...", "").strip().lower()
print(resolucao)


'''Exercício B: Histórico de Chat (Listas)
Você tem um histórico de conversa: historico = ["Oi", "Tudo bem?", "Como funciona o RAG?"].

O usuário mandou uma nova mensagem: "Obrigado". Adicione ela na lista.

A lista ficou muito grande! Remova a primeira mensagem ("Oi") para economizar tokens. (Dica: pop(0) remove pelo índice).

Conte quantas mensagens sobraram usando len().'''

historico = ["Oi", "Tudo bem?", "Como funciona o RAG?"]

historico.append("Obrigado")
print(historico)

historico.pop(0)
print(historico)

contar_mensagens = len(historico)
print(f'A lista tem {contar_mensagens} mensagens.')