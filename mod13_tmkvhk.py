import unittest
import datetime

symbol= input ("Enter Symbol:")
if len(symbol)==7  and symbol.isalpha()== True and symbol.isupper()== True:

    print("The symbol you entered is valid")
else:
        print("The symbol you entered was invalid.")

try:
    chart_type= int(input("Enter Chart Type:"))
    if chart_type ==1 or chart_type == 2:
        print("Valid Chart Type")
    else:
            print("invalid time series")
except ValueError:
  print("Invaild Time Series")


date= input("Enter start date in the format YYYY-MM-DD: ")
date_format = '%Y-%m-%d'
try:
    date_obj = datetime.datetime.strptime(date, date_format) 
    print("Vaild date format") 
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format")

date = input("Enter end date in the format YYYY-MM-DD: ") 
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date, date_format)
  print("Vaild date format") 
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format")