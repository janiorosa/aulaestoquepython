from flask import render_template, request
import model.vendas

def registrar_rotas(app):
    @app.route("/relatorio/relvendas")
    def gerar_relvendas_html():
        data_inicial=request.args.get("data_inicial","")
        data_final=request.args.get("data_final","")
        
        dadosvendas=model.vendas.relatorio(data_inicial,
            data_final)
            
        return render_template("relvendashtml.html",
            dados=dadosvendas,
            data_inicial=data_inicial,
            data_final=data_final
        )