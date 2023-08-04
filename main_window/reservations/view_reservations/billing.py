import tkinter as tk


import PyPDF2

import controller
from pathlib import Path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageTemplate, Frame
from datetime import datetime
import sys
import os


def get_template_path():
    # Get the path to the temporary extraction directory (where the .exe is running from)
    extracted_path = getattr(sys, '_MEIPASS', os.getcwd())

    # Check if "template.pdf" exists in the temporary extraction path
    template_in_extraction = os.path.join(extracted_path, "template.pdf")
    if os.path.isfile(template_in_extraction):
        return template_in_extraction

    # If "template.pdf" doesn't exist in the extraction path, use the current directory
    return "template.pdf"


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def on_checkin_change(event, checkout, checkin, price, total):
    try:
        checkedout = datetime.strptime(checkout.get(), "%Y-%m-%d %H:%M:%S")
        checkedin = datetime.strptime(checkin.get(), "%Y-%m-%d %H:%M:%S")
        # Calculate the difference between the two datetime objects
        night_duration = checkedout - checkedin

        # Get the number of nights as an integer
        num_nights = int(night_duration.days) + 1
        totalprice = int(num_nights) * int(price)
        total.set(totalprice)
        # Process the checkin date and update another entry's value
        # checkin_date_str = checkin.get()
        # You can perform any processing you need here based on the checkin_date_str
        # For example, you can convert it to a different format or calculate something.
        # For demonstration purposes, let's copy the checkin date to the checkout entry.
        # checkout.set(checkin_date_str)
    except ValueError:
        # Handle invalid input if needed
        pass


def grand_total(event, cgst, sgst, total, gtotal):
    if cgst.get() == '' or sgst.get() == '':
        return
    cgst_value = int(cgst.get())
    sgst_value = int(sgst.get())
    total_value = int(total.get())

    # Calculate the grand total
    rtotal = (cgst_value + sgst_value) * total_value // 100 + total_value

    # Set the calculated value to the gtotal variable (assuming gtotal is a StringVar)
    gtotal.set(str(rtotal))
def g_bill(id,root):

    canvass = tk.Canvas(
        root,
        bg="lightgray",
        height=450,
        width=900,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    canvass.place(x=0, y=0)

    # canvas.create_rectangle(
    #     215, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
    # )
    # id = 17
    cursor = controller.connection.cursor(buffered=True)
    cmd = f"select check_in,check_out,r_id,g_id from reservations where id='{id}';"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        checkedin = row[0]
        checkedout = row[1]
        rid = row[2]

        gid = row[3]
    print(gid)
    cmd = f"select name,address,phone from guests where id={gid}"
    cursor.execute(cmd)
    rows = cursor.fetchall()

    for row in rows:
        names = row[0]
        add = row[1]
        phone = row[2]
    cmd = f"select price,room_type from rooms where id={rid}"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        price = row[0]
        roomtype = row[1]
    Gname = tk.StringVar()
    Gname.set(names)
    print(Gname.get())
    gnamel = tk.Label(canvass, text="Guest Name:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    gnamel.place(x=40, y=10)
    gname = tk.Entry(canvass, textvariable=Gname, font=12, fg="black", width=15)  # Use textvariable instead of text
    gname.place(x=170, y=10)
    Gadd = tk.StringVar()
    Gadd.set(add)
    gaddl = tk.Label(canvass, text="Guest Add. :", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    gaddl.place(x=440, y=10)
    gadd = tk.Entry(canvass, textvariable=Gadd, font=12, fg="black", width=15)  # Use textvariable instead of text
    gadd.place(x=580, y=10)
    Rname = tk.StringVar()
    Rname.set(roomtype)
    rnamel = tk.Label(canvass, text="Room Name:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    rnamel.place(x=40, y=60)
    rname = tk.Entry(canvass, textvariable=Rname, font=12, fg="black", width=15)  # Use textvariable instead of text
    rname.place(x=170, y=60)
    Gphone = tk.StringVar()
    Gphone.set(phone)
    gphonel = tk.Label(canvass, text="Phone No:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    gphonel.place(x=440, y=60)
    gphone = tk.Entry(canvass, textvariable=Gphone, font=12, fg="black", width=15)  # Use textvariable instead of text
    gphone.place(x=580, y=60)
    checkin = tk.StringVar()
    checkin.set(checkedin)
    checkinl = tk.Label(canvass, text="Check In:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    checkinl.place(x=40, y=110)
    checkine = tk.Entry(canvass, textvariable=checkin, font=12, fg="black",
                        width=15)  # Use textvariable instead of text
    checkine.place(x=170, y=110)


    checkout = tk.StringVar()
    checkout.set(checkedout)
    checkoutl = tk.Label(canvass, text="Check Out:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    checkoutl.place(x=440, y=110)
    checkoute = tk.Entry(canvass, textvariable=checkout, font=12, fg="black",
                         width=15)  # Use textvariable instead of text
    checkoute.place(x=580, y=110)

    invl = tk.Label(canvass, text="Invoice No:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    invl.place(x=40, y=170)
    inv = tk.Entry(canvass, font=12, fg="black", width=15)  # Use textvariable instead of text
    inv.place(x=170, y=170)
    total = tk.StringVar()
    # Calculate the difference between the two datetime objects
    night_duration = checkedout - checkedin

    # Get the number of nights as an integer
    num_nights = int(night_duration.days) + 1
    totalprice = int(num_nights) * int(price)
    total.set(totalprice)
    totall = tk.Label(canvass, text="Sub Total:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    totall.place(x=440, y=170)
    totale = tk.Entry(canvass, textvariable=total, font=12, fg="black", width=15)  # Use textvariable instead of text
    totale.place(x=580, y=170)
    # checkin.trace("w", lambda *args: calculate_total())  # Call calculate_total whenever checkin changes
    # checkout.trace("w", lambda *args: calculate_total())  # Call calculate_total whenever checkout changes
    checkoute.bind("<FocusOut>", lambda event: on_checkin_change(event,checkout, checkin, price, total))
    checkine.bind("<FocusOut>", lambda event: on_checkin_change(event,checkout, checkin, price, total))

    cgstl = tk.Label(canvass, text="CGST %:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    cgstl.place(x=40, y=230)
    cgst = tk.Entry(canvass, font=12, fg="black", width=15)  # Use textvariable instead of text
    cgst.place(x=170, y=230)
    sgstl = tk.Label(canvass, text="SGST %:", font=(("bold"), 14), fg="black", width=11, bg="lightgray")
    sgstl.place(x=440, y=230)
    sgst = tk.Entry(canvass, font=12, fg="black", width=15)  # Use textvariable instead of text
    sgst.place(x=580, y=230)
    grdl = tk.Label(canvass, text="Grand Total:", font=(("bold"), 14), fg="black", width=12, bg="lightgray")
    grdl.place(x=440, y=315)
    gtotal = tk.StringVar()

    grd = tk.Entry(canvass, textvariable=gtotal, font=12, fg="black", width=15)  # Use textvariable instead of text
    grd.place(x=580, y=315)
    cgst.bind("<FocusOut>", lambda event:grand_total(event,cgst,sgst,total,gtotal))
    sgst.bind("<FocusOut>",lambda event:grand_total(event,cgst,sgst,total,gtotal))
    fram = tk.Frame(canvass, bg="black")
    fram.place(x=20, y=290, height=1, width=800)
    genbill = tk.Button(canvass, text="Generate Bill", bg="#006cff", fg="white", font=13, bd=2, relief="ridge",
                        width=15, heigh=1, command=lambda: generate_bill())
    genbill.place(x=350, y=390)

    def generate_bill(

        filename="generated_bill.pdf"
    ):
        # Get the data to insert into the PDF from the GUI elements
        checked_in = checkine.get()
        checked_out = checkoute.get()
        guest_name = gname.get()
        guest_address = gadd.get()
        guest_phone = gphone.get()
        room_type = rname.get()
        room_price = price
        num_nights_spend = int(num_nights) + 1
        total_price = total.get()
        # Define styles for the content
        styles = getSampleStyleSheet()
        header_style = styles["Heading1"]
        normal_style = styles["Normal"]
        # Load the existing PDF file
        existing_pdf_file = "template.pdf"
        # Create a PDF document
        pdf_filename = "generated_bill.pdf"
        # Create a PDF document
        doc = SimpleDocTemplate(filename, pagesize=letter)

        # Prepare the content for the PDF
        content = []
        # Add the top-left content (Invoice To) to the PDF
        # Add the "Invoice To" content to the PDF
        # Add the "Invoice To" content to the PDF
        invoice_to_table = Table([
            [Paragraph("<b>Invoice To:</b>", normal_style), "", "", "", Paragraph("<b>Invoice No:</b>", normal_style),
             inv.get()],
            [guest_name, "", "", "", "", ""],
            [guest_address, "", "", "", "", ""],
            [guest_phone, "", "", "", "", ""],
        ], colWidths=[120, 160, 60, 60, 80, 80], rowHeights=[20] * 4, hAlign="LEFT")
        invoice_to_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (0, -1), "TOP"),  # Align "Invoice To:" to the top
        ]))
        content.append(invoice_to_table)

        content.append(Spacer(1, 30))  # Add spacing before the small table
        # content.append(small_table)
        # # Add the main table content to the PDF
        # # Add the main table content to the PDF
        # main_table_data = [
        #     [" Room Type", " Checked-in"," Checked-out"," Total Nights Spend"," Room Price"," Sub Total"],
        #     [rname.get(),checked_in,checked_out,num_nights_spend,f"Rs {room_price}",f"Rs {total_price}"],
        #
        # ]
        # main_table = Table(main_table_data, colWidths=[110, 100, 100, 100, 60, 60], rowHeights=[20] * 2, hAlign="LEFT")

        main_table_data = [
            [" Room Type: ", rname.get()],
            [" Checked-in: ", checked_in],
            [" Checked-out: ", checked_out],
            [" Total Nights Spend: ", num_nights_spend],
            [" Room Price: ", f"Rs {room_price}"],
            [" Sub Total: ", f"Rs {total_price}"],
        ]
        main_table = Table(main_table_data, colWidths=[120, 160], rowHeights=[20] * 6, hAlign="LEFT")
        main_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ]))
        content.append(main_table)

        # Add the small table for CGST, SGST, and Grand Total on the right side
        small_table_data = [
            [" CGST: ", f"Rs {int(cgst.get()) * int(total.get()) // 100}"],
            [" SGST: ", f"Rs {int(sgst.get()) * int(total.get()) // 100}"],
            [" Grand Total: ", f"Rs {grd.get()}"],
        ]
        small_table = Table(small_table_data, colWidths=[80, 80], rowHeights=[20] * 3, hAlign="LEFT")
        small_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ]))
        content.append(Spacer(1, 20))  # Add spacing before the small table
        content.append(small_table)

        # Create a PageTemplate and Frame to add content to specific positions
        page_template = PageTemplate(frames=[Frame(30, 100, 550, 500)])  # Adjust the position and size as needed
        doc.addPageTemplates(page_template)

        # Build the PDF document with the content
        doc.build(content)
        # Use PyPDF2 to merge the generated PDF with the existing "template.pdf" as a template
        existing_pdf_file = resource_path("template.pdf")
        output_file = "invoice.pdf"

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
            # Open the generated PDF file using the default associated program
            os.startfile(output_file)



class gen_bill():

    def __init__(self,id):
        self.id=id
        # self.root=root
        self.root = tk.Tk()

        self.root.iconbitmap(resource_path(relative_to_assets('logo.ico')))
        self.root.title("Billing Page")
        self.root.geometry("900x450")
        self.root.configure(bg="lightgray")
        self.root.resizable(False, False)
        g_bill(self.id, self.root)
        self.root.mainloop()

# gen_bill(17)




