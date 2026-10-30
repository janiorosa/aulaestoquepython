
import model.estoque

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
    @app.route("/relatorio/estoque")
    def pagina_rel_estoque():
        return render_template("rel_estoque.html")


    # Geração do relatório em PDF
    @app.route("/relatorio/estoque/pdf")
    def gerar_rel_estoque():

        fornecedor = request.args.get("fornecedor", "").strip()

        # Consulta realizada pelo model
        dados = model.estoque.relatorio(fornecedor)

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
            Paragraph("RELATÓRIO DE ESTOQUE", estilos["Title"])
        )

        elementos.append(Spacer(1, 15))

        elementos.append(
            Paragraph(
                f"Fornecedor: {fornecedor if fornecedor else 'Todos'}",
                estilos["Normal"]
            )
        )

        elementos.append(Spacer(1, 15))

        # Cabeçalho da tabela
        tabela_dados = [[
            "Fornecedor",
            "Produto",
            "ID Mercadoria",
            "Qtd. Atual",
            "Qtd. Mínima",
            "Localização",
            "Lote"
        ]]

        # Inclusão dos registros
        for linha in dados:

            tabela_dados.append([
                str(linha["nome_fantasia"] or ""),
                str(linha["nome_produto"] or ""),
                str(linha["id_mercadoria"] or ""),
                str(linha["quantidade_atual"] or ""),
                str(linha["quantidade_minima"] or ""),
                str(linha["localizacao"] or ""),
                str(linha["lote"] or "")
            ])            

        if not dados:
            tabela_dados.append([
                "Nenhum registro encontrado", "", "", "", "", "", ""
            ])

        tabela = Table(
            tabela_dados,
            repeatRows=1,
            colWidths=[
                3.5 * cm,
                4 * cm,
                2.2 * cm,
                2 * cm,
                2 * cm,
                3 * cm,
                2.5 * cm
            ]
        )

        tabela.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0),
             colors.HexColor("#34495e")),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

            ("FONTSIZE", (0, 0), (-1, -1), 8),

            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

            ("ROWBACKGROUNDS", (0, 1), (-1, -1),
             [colors.white, colors.HexColor("#ecf0f1")]),

            ("TOPPADDING", (0, 0), (-1, -1), 6),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))

        elementos.append(tabela)

        documento.build(elementos)

        buffer.seek(0)

        resposta = make_response(buffer.getvalue())

        resposta.headers["Content-Type"] = "application/pdf"

        resposta.headers["Content-Disposition"] = (
            "inline; filename=relatorio_estoque.pdf"
        )

        return resposta
