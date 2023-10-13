from PyPDF2 import PdfReader, PdfWriter

def add_outline_to_pdf(input_pdf, output_pdf, outline_items):
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    # Add pages from the input PDF to the output PDF
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        pdf_writer.add_page(page)

    # Add the outlines to the output PDF
    for title, page_number in outline_items:
        pdf_writer.add_outline_item(title, page_number)

    # Write the modified PDF to the output file
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)


if __name__ == "__main__":
    # page starts at 0
    outline_items = [
        ("0", 0),
        ("1 Adding Outlines ", 1),
        ("2 Installing PyPDF2 ", 2),
        ("3 Using add outline item ", 3),
        ("4 Viewing Outlines ", 4),
        ("5 All Set! ", 5),
        ("6 Useful commands ", 6),
        ("7 awk output ", 7),
        ("8 section 10 ", 8),
        ("9 section 11 ", 9),
        ("10 section 12 ", 10),
        ("11 section 13 ", 11),
        ("12 section 14 ", 12),
        ("13 section 15 ", 13),
        ("14 section 16 ", 14),
        ("15 section 17 ", 15),
        ("16 section 18 ", 16),
        ("17 section 19 ", 17),
        ("18 section 20 ", 18),
        ("19 section 21 ", 19),
        ("20 section 22 ", 20),
        ("21 section 23 ", 21),
        ("22 section 24 ", 22),
        ("23 section 25 ", 23),
        ("24 section 26 ", 24),
        ("25 section 27 ", 25),
        ("26 section 28 ", 26),
        ("27 section 29 ", 27),
        ("28 section 30 ", 28),
        ("29 Conclusion ", 29),

    ]

    input_pdf = "add_outlines_sample.pdf" # you can download from https://github.com/p1xckha/python-snippets/tree/main/PyPDF2
    output_pdf = "add_outlines_sample_output.pdf"
    
    add_outline_to_pdf(input_pdf, output_pdf, outline_items)


