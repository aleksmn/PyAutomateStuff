import PyPDF2
import os


def getAllTextFromPdf(path_to_pdf):
    """Get all text from PDF file"""
    
    pdfFile = open(path_to_pdf, 'rb')
    reader = PyPDF2.PdfFileReader(pdfFile)
    allText = ''
    for pageNum in range(reader.numPages):
        allText += reader.getPage(pageNum).extractText()

    return allText

def combine2PdfFiles(path_to_pdf1, path_to_pdf2, path_to_output_pdf):
    """Combine two PDFs together"""

    pdfFile1 = open(path_to_pdf1, 'rb')
    pdfFile2 = open(path_to_pdf2, 'rb')
    reader1 = PyPDF2.PdfFileReader(pdfFile1)
    reader2 = PyPDF2.PdfFileReader(pdfFile2)

    writer = PyPDF2.PdfFileWriter()
    for pageNum in range(reader1.numPages):
        writer.addPage(reader1.getPage(pageNum))

    for pageNum in range(reader2.numPages):
        writer.addPage(reader2.getPage(pageNum))

    outputFile = open(path_to_output_pdf, 'wb')
    writer.write(outputFile)
    outputFile.close()
    pdfFile1.close()
    pdfFile2.close()



# print(os.listdir('pdf'))

text = getAllTextFromPdf('pdf/meetingminutes1.pdf')
#print(text[:2000])
    
combine2PdfFiles('pdf/meetingminutes1.pdf', 'pdf/meetingminutes2.pdf','pdf/combinedpdf.pdf')
