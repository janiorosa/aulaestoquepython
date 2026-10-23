from model.conexao import obter_conexao

def listar():
    sql = """SELECT * FROM controlemerc.estoque"""
    
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql) 
            return cursor.fetchall()

def inserir(id_m,q_atual,q_minima,local,lote,u):
    sql = """INSERT INTO controlemerc.estoque (id_mercadoria,
    quantidade_atual, quantidade_minima, localizacao,
    lote, usuario_atualizacao)VALUES(%s,%s,%s,%s,%s,%s)"""
    with obter_conexao() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql,(id_m,q_atual,q_minima,local,lote,u))
        conexao.commit()
