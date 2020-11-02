import PyPDF2 as pdf

f = open('Working_Business_Proposal.pdf','rb')
pdf_data = pdf.PdfFileReader(f)
print(pdf_data.numPages)

#Get first page
page_one = pdf_data.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)
f.close()