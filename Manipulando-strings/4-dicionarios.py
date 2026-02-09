'''Sua Missão (Use o caderno):

Acesse e imprima o valor da chave "modelo".

A temperatura está alta. Altere o valor da chave "temperatura" para 0.5.

Adicione um novo plugin na lista de plugins: "analise_dados". (Lembre-se: o valor da chave "plugins" é uma lista, então você pode usar .append() nela!).

Desafio Extra: Use uma f-string para imprimir: "O modelo gpt-4 está rodando com temperatura 0.5".

Esse exercício mistura tudo: Dicionário, Lista, Atribuição e F-String. Consegue?'''

config_ia = {
    "modelo": "gpt-4",
    "temperatura": 0.7,
    "max_tokens": 2048,
    "plugins": ["busca_web", "calculadora"]
}

print(config_ia["modelo"])

config_ia["temperatura"] = 0.5
print(config_ia["temperatura"])

config_ia["plugins"].append("analise_dados")
print(config_ia)

print(f'O modelo {config_ia["modelo"]} esta rodando com temperatuda {config_ia["temperatura"]}')

'''🎯 Desafio de Entrevista (Iteração)
Volte ao seu código. A lista config_ia["plugins"] agora tem 3 itens (busca_web, calculadora, analise_dados).

Tarefa: Escreva um loop for que percorra essa lista de plugins.

Para cada plugin, imprima: "Ativando plugin: [NOME]".

Lógica Extra: Se o nome do plugin for "calculadora", imprima uma linha extra abaixo dizendo: "--- AVISO: Uso limitado de CPU ---".

Dica: Lembre-se que config_ia["plugins"] é a lista que você vai percorrer.

Consegue montar essa estrutura sem usar chaves {} e acertando a indentação?'''

for item in config_ia["plugins"]:

    print(f'* Ativando plugin {item}')

    if item == "calculadora":
        print('--- AVISO: Uso limitado de CPU ---')