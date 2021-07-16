from PyPDF2 import PdfFileReader
path="bankst.pdf"
f=open(path,'rb')
pdf=PdfFileReader(f)
page=pdf.getPage(0)
print(page.extractText())
tra=pdf.getNamedDestinations('Customer ID')

print(tra)
f.close()