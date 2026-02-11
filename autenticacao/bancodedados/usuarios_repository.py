from bancodedados.conexao import cursor, con
from bcrypt import hashpw, gensalt, checkpw

def cadastrar(nome, email, senha):
    senha_hash = hashpw(str.encode(senha), gensalt())
    result = cursor.execute('INSERT INTO usuarios (nome, email, senha) values (%s, %s, %s) returning *', (nome, email, senha_hash.decode()))
    con.commit()
    usuario = result.fetchone()
    return{
        'id': usuario[0],
        'nome': usuario[1],
        'email': usuario[2],
        'senha': usuario[3]
    }

def buscar_email(email):
    result = cursor.execute('SELECT * FROM usuarios where email = %s', (email,))
    usuario = result.fetchone()

    if usuario == None:
        return None
    
    return {
        'id': usuario[0],
        'nome': usuario[1],
        'email': usuario[2],
        'senha': usuario[3]
    }
