from model.conexao import obter_conexao

def listar():
    sql=""" SELECT V.*, M.nome_produto
        FROM controlemerc.vendas V 
        JOIN controlemerc.mercadorias M 
            ON M.id_mercadoria = V.id_mercadoria 
        ORDER BY v.data_venda DESC 
        """
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
            
def inserir(id_m,quant,preco,desconto,vendedor,canal,forma):
    sql=""" INSERT INTO controlemerc.vendas (id_mercadoria,
        quantidade_vendida,preco_unitario_praticado,
        desconto_aplicado,usuario_vendedor,canal_venda,
        forma_pagamento) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql,(id_m,quant,preco,desconto,
                               vendedor,canal,forma))
        conexao.commit()

def relatorio(data_inicial, data_final):
    sql = """
        SELECT
            forn,
            produto,
            quantidade_vendida,
            preco,
            desconto_aplicado,
            data_venda,
            canal_venda,
            pagto
        FROM controlemerc.view_rel_vendas
        WHERE (%s = '' OR DATE(data_venda) >= %s)
          AND (%s = '' OR DATE(data_venda) <= %s)
        ORDER BY data_venda DESC
    """

    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (
                data_inicial,
                data_inicial,
                data_final,
                data_final
            ))
            return cursor.fetchall()

