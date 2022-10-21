import psycopg2
from create_dataframes import freq_categorias

conn = psycopg2.connect(
    database="avd",
    user='root',
    password='root',
    host='localhost',
    port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute('drop table if exists FREQ_CATEGORIAS')

sql = '''CREATE TABLE FREQ_CATEGORIAS(Categoria varchar(50),Frequencia int)'''

cursor.execute(sql)

# importar csv
data = freq_categorias()

# # converter data para sql 
# data.to_sql('FREQ_CATEGORIAS', conn, if_exists='replace', index=False)

cursor.execute("insert into FREQ_CATEGORIAS values ('teste',3)")
# # fetching all rows
cursor.execute('select * from FREQ_CATEGORIAS')
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()
