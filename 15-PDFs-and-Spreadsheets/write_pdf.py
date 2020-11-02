import PyPDF2 as pdf

f = open('Working_Business_Proposal.pdf','rb')
reader = pdf.PdfFileReader(f)
page_one = reader.getPage(0)
print(page_one.extractText())
with open('New_file.pdf','wb') as pdf_op:
	writer = pdf.PdfFileWriter()
	writer.addPage(page_one)
	writer.write(pdf_op)
f.close()