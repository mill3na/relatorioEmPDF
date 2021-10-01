from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import os


def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')

nomeDoRelatorio = "Relatório de medição Auralize.pdf"
yPrimeiroTexto = 700

pdf = canvas.Canvas('RelatorioAuralize.pdf')
#drawMyRuler(pdf) #this is to guide you about page spacing
pdf.setTitle('Relatorio de medição Auralize')
pdf.drawImage('auralize.png', 240, 720, 120, 100)
pdf.setFont('Times-Roman', 16)
pdf.drawCentredString(300, 690, 'Relatorio de medição Auralize')
# (x, y) inicial, (x, y) final. Para alterar as alturas, mude somente os x
pdf.line(30, 610, 550, 610)
pdf.setFontSize(14)
from reportlab.platypus import Paragraph
p = Paragraph('Dados da medição')
# incluindo o parágrafo no pdf: onde será incluso, largura e altura
p.wrapOn(pdf, 400, 100)
p.drawOn(pdf, 100, 620)

from reportlab.platypus import Table
tempo = '39s'
tabelaDadosDaMedicao = Table([
    ['Tipo de som medido: ', 'contínuo ou intermitente'],
    ['Ponderação', 'A, slow'],
    ['Tempo de medição  ', tempo],
    ['RLAEQ  ', 90],
    ['RLAMAX  ', 120],
    ['RLNC  ', 110]
])
tabelaDadosDaMedicao.wrapOn(pdf, 0, 0)
tabelaDadosDaMedicao.drawOn(pdf, 95, 500) #530

pdf.line(30, 440, 550, 440)

p = Paragraph('Legislação aplicável')
# incluindo o parágrafo no pdf: onde será incluso, largura e altura
p.wrapOn(pdf, 400, 100)
p.drawOn(pdf, 100, 450) #490

tabelaLegislacaoAplicavel = Table([
     ['Legislação 1  ', 'Local'],
     ['Legislação 2  ', "Local 2"],
     ['Legislação 3', 'Local 3'],
     ['NBR 10 151', 'Nacional']
 ])
tabelaLegislacaoAplicavel.wrapOn(pdf, 0, 0)
tabelaLegislacaoAplicavel.drawOn(pdf, 95, 360)


pdf.line(30, 260, 550, 260)

p = Paragraph('Recomendações segundo a OMS')
# incluindo o parágrafo no pdf: onde será incluso, largura e altura
p.wrapOn(pdf, 400, 100)
p.drawOn(pdf, 100, 270)

p = Paragraph('bla bla bla')
# incluindo o parágrafo no pdf: onde será incluso, largura e altura
p.wrapOn(pdf, 400, 100)
p.drawOn(pdf, 100, 230)
pdf.save()
