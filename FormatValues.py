
import datetime
from datetime import datetime



def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDate(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr




    

def CalBilDate():
    # Function will accept the invoice as current date and gives the first payment date as the first day of the next month.
    
    today = datetime.now()
    month = today.month + 1
    year = today.year
    if month > 12:
        month = 1
        year += 1
    BilDate = datetime(year, month, 1)
    return BilDate.strftime("%Y-%m-%d")




