import psycopg

conexao = psycopg.connect('postgresql://postgres:postgres@localhost/biblioteca')

cursor = conexao.cursor()

'''todos_livros = cursor.execute('select * from livros')

print(todos_livros.fetchall())'''

