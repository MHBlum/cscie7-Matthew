#Matthew Blum 2/3/2020; create a script which assigns a year and then determines if the year is a leap year.

#assign the year variable
year = 2000

#checks if year is evenly divisible by 4; if so, move on to further checks.
if year%4 == 0:
	#checks if year is evenly divisible by 100 (if is divisible by 4); if not, is a leap year, if so, not a leap year.
	if year%100 == 0:
		#checks if year is divisible by 400 (if is divisible by 4 and 100); if so, leap year, if not, not leap year.
		if year%400 == 0:
			print(str(year)+" is a leap year.")
		else:
			print(str(year)+" is not a leap year.")
	else:
		print(str(year)+" is a leap year.")
else:
	print(str(year) + " is not a leap year.")