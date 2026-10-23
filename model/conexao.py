import psycopg
from psycopg.rows import dict_row 

def obter_conexao():
    return psycopg.connect(
        host="10.90.24.54",
        port=5432,
        dbname="aula",
        user="aula",
        password="aula",
        row_factory=dict_row
    )
