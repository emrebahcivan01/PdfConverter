from pdf2docx import Converter

pdf_path = "sql-case.pdf"
docx_path = "sample.docx"

cv = Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()
