import csv
import PyPDF2
import re

f = open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\15-PDFs-and"
         r"-Spreadsheets\Exercise_Files\find_the_link.csv", "r")

csv_data = csv.reader(f)

data_lines = list(csv_data)

for lines in data_lines:
    print(lines)
print('\n\n')


print('The length is: ', len(data_lines))
print("The weith is: ", len(data_lines[0]))

link = []

for num in range(len(data_lines)):
    link.append(data_lines[num][num])

print(link)

link = ''.join(link)
print(link)
num = 0

for lines in data_lines:
    print(lines[num])
    num +=1

print("\n\n")
link = ''.join(link)
print(link)
f.close()

link =''
for row_num, f in enumerate(data_lines):
    link += f[row_num]
print(link)


# PDF PROBLEM
print('\n\n\n\n')

f = open(r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\15-PDFs-and"
         r"-Spreadsheets\Exercise_Files\Find_the_Phone_Number.pdf", "rb")

pdf = PyPDF2.PdfFileReader(f)
print("Number of pages: ", pdf.numPages)

# As we don't know what's the real pattern, we will start searching for a 3 digits pattern
pattern = r"\d{3}"

all_text = ''
other = ''

for n in range(pdf.numPages):

    page = pdf.getPage(n)
    all_text += page.extractText()

print(all_text)
# With re.search all we'll only find the first match.
number = re.findall(pattern, all_text)
print(number)
# With findall we will find avery match, but it will only return the number, and if we want to be sure if the match
# is the number we are searching for, we can search it with finditer that shows us the index position of the number
# in the text



number = re.finditer(pattern, all_text)
print(number)

for n in number:
    print(n)
print('\n\n')
print
print(all_text[41794:41797])
print('Sowing more text')
print(all_text[41794-20:41797+20])

# Now we can update our pattern to get only the phone number
pattern = r"\d{3}.\d{3}.\d{4}"

number = re.search(pattern, all_text)

print("The number is: ", number)
