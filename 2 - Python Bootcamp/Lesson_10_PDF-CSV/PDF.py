import PyPDF2

f = open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\15-PDFs-and"
         r"-Spreadsheets\working_Business_Proposal.pdf", "rb")  # rb = read binary

pdf_reader = PyPDF2.PdfFileReader(f)

print("The number of pages are: ", pdf_reader.numPages)

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)

f.close()



f = open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\15-PDFs-and"
         r"-Spreadsheets\working_Business_Proposal.pdf", "rb")

pdf_reader = PyPDF2.PdfFileReader(f)

first_page = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()
print('\n')
print(type(first_page))

pdf_writer.addPage(first_page)

pdf_output = open("Some_Brandnew_Doc.pdf", "wb")

pdf_writer.write(pdf_output)
f.close()  # File I read
pdf_output.close()  # File I wrote


f = open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\15-PDFs-and"
         r"-Spreadsheets\working_Business_Proposal.pdf", "rb")

pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):

    page = pdf_reader.getPage(num)

    pdf_text.append(page.extractText())


print(pdf_text[3])


