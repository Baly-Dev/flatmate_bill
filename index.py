# imported modules
import names
from random import randint

# custom modules
from objects.flatmate import Flatmate
from objects.bill import Bill
from objects.pdf_report import PdfReport

# create the bill
bill = Bill(
        float(input("Insert the amout of the bill: ")), 
        input("Insert the period of the bill (ex.: April 2021): ")
        )
print("")

# create flatmates
flatmates = []
for i in range(2):
    flatmates.append(Flatmate(
            input("Enter flatmate name: "), 
            float(input("Enter how many days in house stayed: ")))
            )
    print("")

# generate pdf report
bill_pdf_report = PdfReport('bill_' + bill.period)
bill_pdf_report.generate(bill, flatmates)
print('The pdf report has been generated in the /reports folder')