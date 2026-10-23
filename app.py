from flask import render_template 
from flask import request 
from flask import redirect
from flask import Flask 

from controller.fornecedores import registrar_rotas as registrar_fornecedores
from controller.mercadorias import registrar_rotas as registrar_mercadorias
from controller.vendas import registrar_rotas as registrar_vendas
from controller.estoque import registrar_rotas as registrar_estoque
app=Flask(__name__)
app.secret_key="alkjoqiuwer02198"

@app.route("/")
def inicio():
    return render_template("index.html")

registrar_fornecedores(app)
registrar_mercadorias(app)
registrar_vendas(app)
registrar_estoque(app)
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
