temperature = float(input("What temperature is absolute zero "))
if temperature > 0:
    # If a positive number, raise ValueError will run and notify the user viewing the terminal what happened
    raise ValueError("The temperature has to be negative") 
else:
    # If a negative number is entered, else will run
    print("The temperature is negative, yes, -459.67 F to be exact.")