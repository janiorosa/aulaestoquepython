from flask import render_template
from conexao import obter_conexao
import model.estoque 

def registrar_rotas(app):
    
    @app.route("/relatorio/relestoque")
    def gerar_relestoque_html():
        dadosestoque = model.estoque.relatorio()
        return render_template("relestoquehtml.html",
            dados=dadosestoque)
