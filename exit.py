# import os
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
#
# def generate_pdf(bill_text, file_name):
#     # Create a new PDF file
#     c = canvas.Canvas(file_name, pagesize=letter)
#
#     # Set font and font size
#     c.setFont("Helvetica", 12)
#
#     # Split the bill_text into lines based on newline characters
#     lines = bill_text.split("\n")
#
#     # Set the starting position for drawing the text
#     x = 50
#     y = 750
#
#     # Loop through each line and draw it on the PDF
#     for line in lines:
#         c.drawString(x, y, line)
#         y -= 20  # Move to the next line
#
#     # Save the PDF file
#     c.save()
#
#     # Open the PDF file with the default PDF viewer on Windows
#     os.startfile(file_name)  # For Windows
#
# # Example usage:
# checkedin = "2023-07-29"
# checkedout = "2023-08-02"
# names = "John Doe"
# price = 100
# num_nights = 4
# totalprice = 400
#
# bill_text = f"Checked-in: {checkedin}\n" \
#             f"Checked-out: {checkedout}\n" \
#             f"Guest Name: {names}\n" \
#             f"Room Price: {price}\n" \
#             f"Total Nights Spend: {num_nights}\n" \
#             f"-----------------------------------------------\n Total Price: {totalprice}\n"
#
# file_name = "bill.pdf"
#
# generate_pdf(bill_text, file_name)
# import mysql.connector
# def connect_db():
#
#     try:
#         connection = mysql.connector.connect(
#         host="midlead-hms.cdmwztzukbhk.us-east-1.rds.amazonaws.com",
#         user="admin",
#         password="18Midlead",
#         database="midleadhms",
#         port=3306,
#
#
#
#     )
#         return connection
#     except mysql.connector.Error as e:
#         print(f"Error connecting to the database: {e}")
#         return None
# #
# connection = connect_db()
# # print(connection)
# cur = connection.cursor()
# cur.execute("SELECT * FROM guests")
# rows = cur.fetchall()
#
# for row in rows:
#     print(row)
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.platypus import Frame, PageTemplate


def generate_bill(data, filename="invoice.pdf"):
    # Get the data from the 'data' argument
    guest_name = data.get('guest_name', '')
    guest_address = data.get('guest_address', '')
    guest_phone = data.get('guest_phone', '')
    room_type = data.get('room_type', '')
    room_price = data.get('room_price', '')
    num_nights_spend = data.get('num_nights_spend', '')
    total_price = data.get('total_price', '')
    cgst = data.get('cgst', '')
    sgst = data.get('sgst', '')
    grand_total = data.get('grand_total', '')
    styles = getSampleStyleSheet()
    header_style = styles["Heading1"]
    normal_style = styles["Normal"]
    # Create a PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)

    # Prepare the content for the PDF
    content = []
    # Add the top-left content (Invoice To) to the PDF
    invoice_to_table = Table([
        [Paragraph("<b>Invoice To:</b>", normal_style), "", "", "", Paragraph("<b>Invoice No:</b>", normal_style),
         123],
        [guest_name, "", "", "", "", ""],
        [guest_address, "", "", "", "", ""],
        [guest_phone, "", "", "", "", ""],
    ], colWidths=[120, 160, 60, 60, 80, 80], rowHeights=[20] * 4, hAlign="LEFT")
    invoice_to_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (0, -1), "TOP"),  # Align "Invoice To:" to the top
    ]))
    content.append(invoice_to_table)

    # ... (rest of the content creation)

    # Create a PageTemplate and Frame to add content to specific positions
    page_template = PageTemplate(frames=[Frame(30, 100, 550, 500)])  # Adjust the position and size as needed
    doc.addPageTemplates(page_template)

    # Build the PDF document with the content
    doc.build(content)

    # Use PyPDF2 to merge the generated PDF with the existing "bill.pdf" as a template
    existing_pdf_file = "bill.pdf"
    output_file = "merged_invoice.pdf"

    with open(existing_pdf_file, "rb") as existing_pdf:
        pdf_reader = PyPDF2.PdfReader(existing_pdf)
        pdf_writer = PyPDF2.PdfWriter()

        # Extract the first page of the existing PDF as a template
        existing_pdf_first_page = pdf_reader.pages[0]

        # Add the modified page (generated content) to the new PDF
        with open(filename, "rb") as generated_pdf:
            pdf_reader_generated = PyPDF2.PdfReader(generated_pdf)
            generated_pdf_first_page = pdf_reader_generated.pages[0]
            existing_pdf_first_page.merge_page(generated_pdf_first_page)
            pdf_writer.add_page(existing_pdf_first_page)

        # Save the merged PDF to the output file
        with open(output_file, "wb") as output:
            pdf_writer.write(output)


# Example usage:
data = {
    "guest_name": "John Doe",
    "guest_address": "123 Main St",
    "guest_phone": "555-1234",
    "room_type": "Deluxe Room",
    "room_price": 2000,
    "num_nights_spend": 3,
    "total_price": 6000,
    "cgst": 5,
    "sgst": 5,
    "grand_total": 6600,
}

generate_bill(data, filename="invoice.pdf")
