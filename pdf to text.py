import PyPDF2
pdffileobj = open('a8d049f7-39db-4e3f-bab6-bba95c6acd2a.pdf', 'rb')
pdfreader = PyPDF2.PdfReader(pdffileobj)
x = len(pdfreader.pages)
with open('out.txt', 'w', encoding='utf-8') as f:
    for i in range(x):
        pageobj = pdfreader.pages[i]
        text = pageobj.extract_text()
        f.write(text)
