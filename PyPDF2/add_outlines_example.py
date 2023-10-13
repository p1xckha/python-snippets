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
        ("1 Adding Outlines",   2),
        ("2 Installing PyPDF2", 3),
        ("3 Using add outline item",    4),
        ("4 Viewing Outlines",  5),
        ("5 All Set!",  6),
        ("6 section 8", 7),
        ("7 section 9", 8),
        ("8 section 10",        9),
        ("9 section 11",        10),
        ("10 section 12",       11),
        ("11 section 13",       12),
        ("12 section 14",       13),
        ("13 section 15",       14),
        ("14 section 16",       15),
        ("15 section 17",       16),
        ("16 section 18",       17),
        ("17 section 19",       18),
        ("18 section 20",       19),
        ("19 section 21",       20),
        ("20 section 22",       21),
        ("21 section 23",       22),
        ("22 section 24",       23),
        ("23 section 25",       24),
        ("24 section 26",       25),
        ("25 section 27",       26),
        ("26 section 28",       27),
        ("27 section 29",       28),
        ("28 section 30",       29),
        ("29 Conclusion",       30)
    ]

    input_pdf = "add_outlines_sample.pdf" # you can download from https://github.com/p1xckha/python-snippets/tree/main/PyPDF2
    output_pdf = "sample_output.pdf"
    
    add_outline_to_pdf(input_pdf, output_pdf, outline_items)


