import PyPDF2 as pdf

f = open('Working_Business_Proposal.pdf','rb')
reader = pdf.PdfFileReader(f)

total_pages = reader.numPages

pdf_new = open('duplicate_pdf.pdf','wb')
writer = pdf.PdfFileWriter()

for num in range(total_pages):
	page = reader.getPage(num)
	writer.addPage(page)
	writer.write(pdf_new)
f.close()
pdf_new.close()


