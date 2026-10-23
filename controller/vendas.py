from flask import render_template,request,redirect

import model.vendas 
import model.mercadorias

def registrar_rotas(app):
    
    @app.route("/vendas")
    def listar_vendas():
        lista_vendas = model.vendas.listar()
        return render_template( "vendas.html", lista=lista_vendas)
    
    @app.route("/vendas/nova")
    def nova_venda():
        lista_merc=model.mercadorias.listar()
        return render_template("venda_nova.html",lista=lista_merc)
        
    @app.route("/vendas/gravar",methods=["POST"])
    def gravar_venda():
        id_merc=request.form["id_mercadoria"]
        quant=request.form["quantidade"]
        preco=request.form["preco_unitario"]
        desconto=request.form["desconto"]
        usuario=request.form["usuario"]
        canal_venda=request.form["canal_venda"]
        forma_pagto=request.form["forma_pagamento"]
        
        model.vendas.inserir(id_merc,quant,preco,desconto,
            usuario,canal_venda,forma_pagto)
            
        return redirect("/vendas")
        
        
        