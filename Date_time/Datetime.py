from datetime import datetime ,timezone, timedelta
print(datetime.now())
print(datetime.now(timezone.utc))
Tommorow = datetime.now(timezone.utc) + timedelta(days=1)
print(Tommorow)
#The datetime module provides classes for manipulating dates and times in Python.
print(Tommorow.strftime('%d-%m-%Y %H:%M:%S'))#stribg format time (strftime()) method is used to convert a datetime object to a string.

user_date = input("Enter the date in YYYY-mm-dd format: ")
user_date = datetime.strptime(user_date, '%Y-%m-%d')#string pass time (strptime()) method is used to convert a string to a datetime object.
print(user_date)
#print(user_date - datetime.now(timezone.utc))