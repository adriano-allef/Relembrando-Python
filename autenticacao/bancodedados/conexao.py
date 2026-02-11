import psycopg

con = psycopg.conect('postgresql://postgres:postgres @localhost/autenticacao')

cursor = con.cursor()