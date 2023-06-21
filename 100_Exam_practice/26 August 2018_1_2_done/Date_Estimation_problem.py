from datetime import datetime

date1 = "2018-08-26"
date2 = input()

newdate1 = datetime.strptime(date1, "%Y-%m-%d")
newdate2 = datetime.strptime(date2, "%Y-%m-%d")

if newdate1 > newdate2:
    print("Passed")
elif newdate2 == newdate1:
    print("Today date")
elif newdate1 < newdate2:
    result = (newdate2 - newdate1).days + 1
    print(f"{result} days left")

