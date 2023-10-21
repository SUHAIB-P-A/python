import datetime

print(datetime.datetime.now())
print(datetime.date.today())
now = datetime.datetime.now()
print(now.strftime("%m/%d/%Y"))
x = datetime.datetime(2023, 5, 20)
# print(x)

y = datetime.datetime(year=2022, day=1, month=12)

diff = x-y  # identefy no. of days

print(diff)

end = datetime.datetime.now()

difference = end-now  # using perfomance analysis
print(difference)
