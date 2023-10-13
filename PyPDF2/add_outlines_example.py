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
    outline_items = [
        ("1 Adding Outlines ", 3),
        ("2 Installing PyPDF2 ", 4),
        ("3 Using add outline item ", 5),
        ("4 Viewing Outlines ", 6),
        ("5 All Set! ", 7),
        ("6 Useful commands ", 8),
        ("7 awk output ", 9),
        ("8 section 10 ", 10),
        ("9 section 11 ", 11),
        ("10 section 12 ", 12),
        ("11 section 13 ", 13),
        ("12 section 14 ", 14),
        ("13 section 15 ", 15),
        ("14 section 16 ", 16),
        ("15 section 17 ", 17),
        ("16 section 18 ", 18),
        ("17 section 19 ", 19),
        ("18 section 20 ", 20),
        ("19 section 21 ", 21),
        ("20 section 22 ", 22),
        ("21 section 23 ", 23),
        ("22 section 24 ", 24),
        ("23 section 25 ", 25),
        ("24 section 26 ", 26),
        ("25 section 27 ", 27),
        ("26 section 28 ", 28),
        ("27 section 29 ", 29),
        ("28 section 30 ", 30),
        ("29 Conclusion ", 31),

    ]

    input_pdf = "add_outlines_sample.pdf" # you can download from https://github.com/p1xckha/python-snippets/tree/main/PyPDF2
    output_pdf = "add_outlines_sample_output.pdf"
    
    add_outline_to_pdf(input_pdf, output_pdf, outline_items)


