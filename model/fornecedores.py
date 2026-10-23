from model.conexao import obter_conexao

def listar():
    sql="""
    SELECT * FROM 
    controlemerc.fornecedores
    """
    with obter_conexao() as conexao:
        with conexao.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

def inserir(nome_fantasia,razao_social,cnpj,telefone,email,cidade,estado):
    sql="""INSERT INTO controlemerc.fornecedores 
    (nome_fantasia,razao_social,cnpj,telefone,email,cidade,estado)
    VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql,(nome_fantasia,razao_social,cnpj,telefone,email,cidade,estado))
        conexao.commit()
