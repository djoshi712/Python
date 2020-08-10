import datetime 
odds= [1,3,5,7,9,11]
todays_date= datetime.date.today()
current_month= datetime.date.today().month
current_day= datetime.date.today().day
print(todays_date)

if current_month in odds:
    print("odd month")
else:
    print("even month")
