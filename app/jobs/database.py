import psycopg2
from sqlalchemy import create_engine
from create_dataframes import freq_categorias

conn_string = 'postgres://postgres:pass@127.0.0.1/TESTE'

db = create_engine(conn_string)
conn = db.connect()
conn1 = psycopg2.connect(
	database="TESTE",
user='postgres',
password='pass',
host='127.0.0.1',
port= '5432'
)

conn1.autocommit = True
cursor = conn1.cursor()

cursor.execute('drop table if exists TESTE_TABLE')

sql = '''CREATE TABLE TESTE_TABLE(id int ,
Categoria char(50),Frequencia int);'''

cursor.execute(sql)

# importar csv
data = freq_categorias()

# converter data para sql
data.to_sql('frequencia_categorias', conn, if_exists= 'replace')

# fetching all rows
sql1='''select * from frequencia_categorias;'''
cursor.execute(sql1)
for i in cursor.fetchall():
	print(i)

conn1.commit()
conn1.close()

