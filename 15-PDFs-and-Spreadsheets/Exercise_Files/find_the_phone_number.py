import PyPDF2 as pdf
import re 
import csv
# get the link 

f = open('Find_the_Phone_Number.pdf','rb')
reader = pdf.PdfFileReader(f)

text = ""

for num in range(reader.numPages):
	page = reader.getPage(num)
	text = text + page.extractText()

#print(text)
pattern = r'\d{3}.\d{3}.\d{4}'
matches = ""

for res in re.finditer(pattern,text):
	matches = matches + res.group()
print(matches)
f.close()