from flask import render_template, request, redirect, flash
import model.estoque 
import model.mercadorias 
def registrar_rotas(app):
    localizacoes = (
    [f"Corredor {letra}" for letra in "ABCDEF"]
    + [f"Banca {numero}" for numero in range(1,11)]
    + ["Geladeira", "Banca Padaria", "Balcão Peixe"]
    + [f"Gondola {numero}" for numero in range(1,9)]
    + [f"Deposito {letra}" for letra in "ABCD"]
    + ["Câmara Fria"]
    )
    @app.route("/estoque")
    def estoque():
        lista = model.estoque.listar()
        return render_template("estoque.html", lista=lista)

    @app.route("/estoque/novo")
    def estoque_novo():
        mercadorias=model.mercadorias.listar()
        return render_template( "estoque_novo.html",
            mercadorias=mercadorias,
            localizacoes=localizacoes
        )
    @app.route("/estoque/inserir",methods=["POST"])
    def estoque_inserir():
        id_m=request.form["id_mercadoria"]
        q_atual=request.form["quantidade_atual"]
        q_minima=request.form["quantidade_minima"]
        local=request.form["localizacao_corredor"]
        lote=request.form["lote"]
        u=request.form["usuario_atualizacao"]
        model.estoque.inserir(id_m,q_atual,q_minima,local,lote,u)
        flash("Estoque cadastrado com sucesso!")
        return redirect("/estoque")

