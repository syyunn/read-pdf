import PyPDF2
import modules.constants as const
import modules._longformers as longformers


def read_pdf(path):
    pdf = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf)
    pages = pdf_reader.getNumPages()

    text = ''
    for page in range(pages):
        text += pdf_reader.getPage(page).extractText()

    text = text.replace('\n', ' ')
    print(len(text.split(' ')))
    return text

text = read_pdf(const.pdf)
entity = const.pdf.split('/')[-1].split('-')[0]
# question = f"How does {entity} think about Section 232 Tariff on Steel products?" # 'How does Acenta Steel Limited think about Section 232 Tariff on Steel products?' ' there are dozens of different  steel products'
# question = f"What does {entity} insist about Section 232 or additional tariff on steel products?"
# question = f"What is the {entity}'s political stance over Section 232 or additional tariff on steel products?"
# question = "How does the speaker think about additional tariff on steel products?"
question = f"What does {entity} recommend?"
answer = longformers.question_over_context(question=question, context=text)

if __name__ == "__main__":
    pass
