#Matthew Blum 2/3/2020; create a script which asks for a year input, checks if the year is valid, and then determines if the year is a leap year.

#assign the year variable to a user input
year = input("please enter a year:")

# while TRUE is generic; true is always true, only used to create a loop in order to use 'try'
while True:
	#try will attempt something, if it fails with an error, it will go to the "except" statements
    try:
    	#attemps to cast the "float" type to the year input; if it returns a value error (ie it's a string), skip to the "except" statement.
        year = float(year)
        #checks if the year is divisible evenly by 1, ie, an int.  Also checks if the year is bigger than 0, ie positive.
        if (year%1 == 0) and (year > 0):
        	#casts the year to int
            year = int(year)
            #goes through checks from 02_problem4.py
            if year%4 == 0:
                if year%100 == 0:
                	if year%400 == 0:
                		print(str(year)+" is a leap year.")
                	else:
                		print(str(year)+" is not a leap year.")
                else:
                	print(str(year)+" is a leap year.")
            else:
                print(str(year) + " is not a leap year.")
        else:
        	#if the year could be cast to float but was not positive or an integer, print the statement.
            print("You have entered a number which is not a positive integer.")
        #since we are in a while loop which will never end, we need to break it now that we are done.    
        break
    #in case we can't cast the year to a float, this will tell us that we entered a non-number.    
    except ValueError:
        print("You have entered a non-number")
        #since we are in a while loop which will never end, we need to break it now that we are done.
        break