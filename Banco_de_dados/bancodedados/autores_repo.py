from bancodedados.conexao import cursor

def listar_todos():
    result = cursor.execute('select * from autores')
    autores = result.fetchall()

    lista = []

    for autor in autores:
        lista.append({
            'id': autor[0],
            'nome': autor[1]
        })
    return lista

print(listar_todos())


