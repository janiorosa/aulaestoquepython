from model.conexao import obter_conexao

def listar():
    sql=""" SELECT M.*, F.nome_fantasia 
    FROM controlemerc.mercadorias M
    JOIN controlemerc.fornecedores F 
        ON M.id_fornecedor=F.id_fornecedor
    ORDER BY M.nome_produto
    """
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql) 
            return cursor.fetchall()

def inserir(produto,cat,preco,venda,cb,idf):
    sql="""INSERT INTO controlemerc.mercadorias(nome_produto,
    categoria,preco_custo,preco_venda_sugerido,codigo_barras,
    id_fornecedor) VALUES (%s,%s,%s,%s,%s,%s)"""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql,(produto,cat,preco,venda,cb,idf))
        conexao.commit()
