from flask import render_template
from flask import request
from flask import redirect 
import model.fornecedores 
def registrar_rotas(app):
    @app.route("/fornecedores")
    def listar_fornecedores():
        lista=model.fornecedores.listar()
        return render_template(
            "fornecedores.html",
            lista_fornecedores=lista
        )

    @app.route("/fornecedores/novo")
    def novo_fornecedor():
        return render_template("fornecedor_form.html")
    
    @app.route("/fornecedores/inserir", methods=["POST"])
    def inserir_fornecedor():
        nome_fantasia=request.form["nome_fantasia"]
        razao_social=request.form["razao_social"]
        cnpj=request.form["cnpj"]
        telefone = request.form["telefone"]
        email=request.form["email"]
        cidade=request.form["cidade"]
        estado=request.form["estado"]
        
        model.fornecedores.inserir( nome_fantasia,
            razao_social, cnpj, telefone, email, 
            cidade, estado )
            
        return redirect("/fornecedores")
    