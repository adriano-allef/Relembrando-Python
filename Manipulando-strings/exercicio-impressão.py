'''Desafios:

Imprima o título do segundo documento ("Receita de Bolo").

Imprima o conteúdo do terceiro documento ("Bem-vindo à Cezcom!").

Imprima o ID do primeiro documento (101).'''

base_de_conhecimento = [
    {"id": 101, "titulo": "Política de IA", "conteudo": "A Cezcom utiliza GPT-4."},
    {"id": 102, "titulo": "Receita de Bolo", "conteudo": "Farinha e açúcar."},
    {"id": 103, "titulo": "Onboarding", "conteudo": "Bem-vindo à Cezcom!"}
]

print(base_de_conhecimento[1]["titulo"])
print(base_de_conhecimento[2]["conteudo"])
print(base_de_conhecimento[1]["id"])