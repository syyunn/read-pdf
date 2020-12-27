import PyPDF2
import modules.constants as const

pdf = open(const.pdf, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf)
pages = pdf_reader.getNumPages()

text = ''
for page in range(pages):
    text += pdf_reader.getPage(page).extractText()

print(len(text.split(' ')))
print(text.replace('\n', ' '))
if __name__ == "__main__":
    pass
