"""Flatten multiple PDFs into one"""

import sys
from PyPDF2 import PdfReader, PdfWriter, PageObject

pdfs = [PdfReader(open(filename, 'rb')) for filename in sys.argv[1:]]
page_count = min(len(pdf.pages) for pdf in pdfs)
writer = PdfWriter()

for i in range(page_count):
    pages = [pdf.pages[i] for pdf in pdfs]
    new_page = PageObject.create_blank_page(None, pages[0].mediabox.width, pages[0].mediabox.height)

    for page in pages:
        new_page.merge_page(page)

    writer.add_page(new_page)

writer.write(sys.stdout.buffer)
