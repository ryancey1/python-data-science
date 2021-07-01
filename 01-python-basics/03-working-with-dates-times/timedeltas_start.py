#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=244, minutes=62, seconds=1))

# print today's date
now = datetime.now()
print(f"now it is:\n{now}")

# print today's date one year from now
print(f"in 1yr:\n{now + timedelta(days=365)}")

# create a timedelta that uses more than one argument
print(f"in 1yr, 3wk, 2hr:\n{now + timedelta(days=365, weeks=3, hours=2)}")

# calculate the date 1 week ago, formatted as a string
weekago = now - timedelta(weeks=1)
p = weekago.strftime("%A %B %d, %Y")
print(f"1wk ago:\n{p}")

# How many days until April Fools' Day?
today = date.today()
afd = date(year=today.year, month=4, day=1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if today > afd:
    print(f"April Fool's Day passed {(today-afd).days} days ago")
    afd = afd.replace(year=today.year+1)

# Now calculate the amount of time until April Fool's Day
print(f"Days until next AFD: {(afd-today).days} days")
