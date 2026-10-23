from flask import render_template,request,redirect
import model.mercadorias
import model.fornecedores

def registrar_rotas(app):
    @app.route("/mercadorias")
    def listar_mercadorias():
        lista_mercadorias=model.mercadorias.listar()
        return render_template (
           "mercadorias.html",
           lista=lista_mercadorias
        )
        
    @app.route("/mercadorias/nova")
    def nova_mercadoria():
        lista_fornecedores=model.fornecedores.listar()
        return render_template(
            "mercadoria_form.html",
            lista=lista_fornecedores
        )

    @app.route("/mercadorias/inserir",methods=["POST"])
    def inserir_mercadoria():
        nome_produto=request.form["nome_produto"]
        categoria=request.form["categoria"]
        preco_custo=request.form["preco_custo"]
        preco_venda=request.form["preco_venda"]
        codigo_barras=request.form["codigo_barras"]
        id_fornecedor=request.form["id_fornecedor"]
        model.mercadorias.inserir(nome_produto,categoria,
            preco_custo,preco_venda,codigo_barras,
            id_fornecedor
        )
        return redirect("/mercadorias")
            
        