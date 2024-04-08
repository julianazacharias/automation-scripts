import fitz
import tabula
#pip install openpyxl

def extract_text_from_pdf():
    with fitz.open("students.pdf") as pdf:
        text = ''
        for page in pdf:
            text = text + page.get_text()
        
        return print(text)
    
def extract_table_from_pdf_to_csv():   
    table = tabula.read_pdf('weather.pdf', pages=1)
    print(type(table[0]))
    table[0].to_csv('output.csv', index=None)

def extract_table_from_pdf_to_excel():   
    table = tabula.read_pdf('table_and_text.pdf', pages=1)
    table[0].to_excel('output.xlsx', index=None)