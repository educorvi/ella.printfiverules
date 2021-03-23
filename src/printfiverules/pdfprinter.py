from .s143 import create_pdf as s143_pdf

class PdfPrinter(object):
    def s143(self, data):
        pdf = s143_pdf(data)
        return pdf