import datetime
from qrbill import QRBill
from weasyprint import HTML
from util import convert, prepare_html, send_mail
from db import get_entrys, delete_entrys, close as db_close

creditor = {"name": "Generic Webhost", "pcode": "1000", "city": "Lausanne", "country": "CH", "street": "Rue du Webhosting", "house_num": "13"}
iban_creditor = "CH5800791123000889012"


date = datetime.datetime.now().strftime("%d.%m.%Y")

def get_qr_bill(debtor, amount):
    my_bill = QRBill(
        account=iban_creditor,
        creditor=creditor,
        debtor=debtor,
        amount=amount
    )
    
    with open("invoice.html") as f:
        html = f.read()

    html = prepare_html(html, debtor, creditor, amount)
    html = HTML(string=html)

    return convert(my_bill, html)




invoices = get_entrys(date) or []

for i in invoices:
    amount, firstname, lastname, street, housenumber, citycode, city, iban, email = i
    country = iban[:2]

    debtor = {"name": f"{firstname} {lastname}", "street": street, "house_num": housenumber, "pcode": citycode, "city": city, "country": country}

    file = get_qr_bill(debtor, amount)

    send_mail(file, email)

    print(f"Sent invoice to {email}!")

delete_entrys(date)
db_close()