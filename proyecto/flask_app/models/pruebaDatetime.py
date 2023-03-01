import datetime

 

# Create a date object with today's date

d1 = datetime.datetime.now()
d2 = datetime.datetime.now()
d3 = d1
print("Today's date: {}".format(d1))

dia = int(d1.strftime("%d")) +1
print(dia)
# Replace the time of t1 - set hours to 15

d1 = d1.replace(hour=7, minute=0, second = 0)
d1 = d1 + datetime.timedelta(days=1)

print("New date: {} ".format(d1))

print("D2: {} ".format(d2))

if d1>d2:
	print("d1>")

while(d1>d2):
	d2 = d2 + datetime.timedelta(minutes=30)
	print(d2)

print("d1:",d1)
print("nuevo d2", d2)
print(d3)