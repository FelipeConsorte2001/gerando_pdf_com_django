import io
from django.http import FileResponse
from django.views.generic import View
from reportlab.pdfgen import canvas

class IndexView(View):

    def get(self, request, *args, **kwargs):
        # Cria um arquivo para gerar PDF
        buffer = io.BytesIO()

        # criar o arquivo em PDF
        pdf = canvas.Canvas(buffer)

        # Inserre coisas no PDF
        pdf.drawString(100, 100, 'Geek University')

        # Quando acabamos de inserir as coisas no PDF
        pdf.showPage()
        pdf.save()

        buffer.seek(0)
        # Faz o dowload do arquivo em PDF GERADO
        # return FileResponse(buffer, as_attachment=True, filename='relatorio.pdf')

        # Abre direto no navegador
        return FileResponse(buffer, filename='relatorio.pdf')
