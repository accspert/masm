import smtplib
import tempfile
from svglib.svglib import svg2rlg
from email.utils import formatdate
from email.mime.text import MIMEText
from reportlab.graphics import renderPDF
from email.mime.multipart import MIMEMultipart
from pypdf import PdfWriter, PdfReader, PdfMerger
from email.mime.application import MIMEApplication

def convert(my_bill, html):
    with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
        my_bill.as_svg(temp)
        temp.seek(0)
        drawing = svg2rlg(temp)

    qr = tempfile.TemporaryFile()

    renderPDF.drawToFile(drawing, qr)

    invoice = tempfile.TemporaryFile()
    html.write_pdf(invoice)

    invoice = PdfReader(invoice)
    page = invoice.pages[0]
    page.cropbox.lower_left = (0, 300)

    output = PdfWriter()
    output.add_page(page)

    temp = tempfile.TemporaryFile()
    output.write(temp)

    merger = PdfMerger()
    merger.append(temp)
    merger.append(qr)


    temp = tempfile.TemporaryFile()
    merger.write(temp)

    temp.seek(0)

    return temp


def prepare_html(html, debtor, creditor, amount):
    html = html.replace("{PRICE}", str(amount))
    html = html.replace("{DEBTOR_NAME}", debtor["name"])
    html = html.replace("{DEBTOR_ADDRESS}", debtor["street"])
    html = html.replace("{DEBTOR_HOUSENUMBER}", debtor["house_num"])
    html = html.replace("{DEBTOR_POSTCODE}", debtor["pcode"])
    html = html.replace("{DEBTOR_CITY}", debtor["city"])
    html = html.replace("{DEBTOR_COUNTRY}", debtor["country"])
    html = html.replace("{CREDITOR_COUNTRY}", creditor["country"])
    html = html.replace("{CREDITOR_NAME}", creditor["name"])
    html = html.replace("{CREDITOR_ADDRESS}", creditor["street"])
    html = html.replace("{CREDITOR_HOUSENUMBER}", creditor["house_num"])
    html = html.replace("{CREDITOR_POSTCODE}", creditor["pcode"])
    html = html.replace("{CREDITOR_CITY}", creditor["city"])

    return html


def send_mail(file, email):
    send_mail_internal(
        server="mx2f83.netcup.net",
        user="noreply@business-software-for-free.de",
        password="kpGz74~65",
        send_from="noreply@business-software-for-free.de",
        send_to=email,
        subject="Invoice generated",
        text="""Hello,
An invoice has been generated for your account. See attachment for more details and how to pay.

All the best,
Generic Company
        """,
        file=file
    )


def send_mail_internal(server, user, password, send_from, send_to, subject, text, file, port=587):
    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = send_to
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    msg.attach(MIMEText(text))

    part = MIMEApplication(
        file.read(),
        Name="invoice.pdf"
    )

    part["Content-Disposition"] = f"attachment; filename=invoice.pdf"
    msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    smtp.connect(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(user, password)
    smtp.sendmail(send_from, [send_to], msg.as_string())
    smtp.close()
