import psycopg

con = psycopg.connect('postgresql://postgres:postgres@localhost/autenticacao')

cursor = con.cursor()