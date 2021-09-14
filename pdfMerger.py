import sys
import PyPDF2

input=sys.argv[1:]

def pdfMerger(pdf_list):
    merger=PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
pdfMerger(input)