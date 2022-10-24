import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from create_dataframes import freq_categorias, is_local


conn_string = 'postgresql://root:root@127.0.0.1:5432/avd'

try:
    freq = freq_categorias()
    locais = is_local()

    db = create_engine(conn_string)

    freq.to_sql('freq_categorias', db,
                if_exists='replace', index=False)
    locais.to_sql('fornecedores_locais', db,
                  if_exists='replace', index=False)

    conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    cursor = conn.cursor()
    sql1 = '''select * from freq_categorias;'''
    cursor.execute(sql1)
    for i in cursor.fetchall():
        print(i)

    cursor.execute('''select * from fornecedores_locais;''')
    for i in cursor.fetchall():
        print(i)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
