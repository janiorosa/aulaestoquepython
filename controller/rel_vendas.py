
import model.vendas

from flask import render_template, request, make_response
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


def registrar_rotas(app):

    # Página com o formulário de filtros
    @app.route("/relatorio/vendas")
    def pagina_rel_vendas():
        return render_template("rel_vendas.html")


    # Geração do relatório em PDF
    @app.route("/relatorio/vendas/pdf")
    def gerar_rel_vendas():

        data_inicial = request.args.get("data_inicial", "")
        data_final = request.args.get("data_final", "")

        # Consulta realizada pelo model
        dados = model.vendas.relatorio(
            data_inicial,
            data_final
        )

        # Preparação do PDF
        buffer = BytesIO()

        documento = SimpleDocTemplate(
            buffer,
            pagesize=landscape(A4),
            rightMargin=1 * cm,
            leftMargin=1 * cm,
            topMargin=1.5 * cm,
            bottomMargin=1.5 * cm
        )

        elementos = []
        estilos = getSampleStyleSheet()

        elementos.append(
            Paragraph("RELATÓRIO DE VENDAS", estilos["Title"])
        )

        elementos.append(Spacer(1, 15))

        periodo = (
            f"Período: {data_inicial if data_inicial else 'Início'} "
            f"até {data_final if data_final else 'Atual'}"
        )

        elementos.append(
            Paragraph(periodo, estilos["Normal"])
        )

        elementos.append(Spacer(1, 15))

        # Cabeçalho da tabela
        tabela_dados = [[
            "Fornecedor",
            "Produto",
            "Quantidade",
            "Preço",
            "Desconto",
            "Data da Venda",
            "Canal",
            "Pagamento"
        ]]

        # Inclusão dos registros
        for linha in dados:

            tabela_dados.append([
                str(linha["forn"] or ""),
                str(linha["produto"] or ""),
                str(linha["quantidade_vendida"] or ""),
                str(linha["preco"] or ""),
                str(linha["desconto_aplicado"] or ""),
                str(linha["data_venda"] or ""),
                str(linha["canal_venda"] or ""),
                str(linha["pagto"] or "")
            ])

        if not dados:
            tabela_dados.append([
                "Nenhum registro encontrado",
                "", "", "", "", "", "", ""
            ])

        tabela = Table(
            tabela_dados,
            repeatRows=1,
            colWidths=[
                3 * cm,
                3.5 * cm,
                2 * cm,
                2 * cm,
                2 * cm,
                2.5 * cm,
                2.5 * cm,
                2.5 * cm
            ]
        )

        tabela.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0),
             colors.HexColor("#2874a6")),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

            ("FONTSIZE", (0, 0), (-1, -1), 8),

            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ("ROWBACKGROUNDS", (0, 1), (-1, -1),
             [colors.white, colors.HexColor("#ebf5fb")]),

            ("TOPPADDING", (0, 0), (-1, -1), 6),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))

        elementos.append(tabela)

        documento.build(elementos)

        buffer.seek(0)

        resposta = make_response(buffer.getvalue())

        resposta.headers["Content-Type"] = "application/pdf"

        resposta.headers["Content-Disposition"] = (
            "inline; filename=relatorio_vendas.pdf"
        )

        return resposta
