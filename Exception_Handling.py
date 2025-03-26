#try:
    # code that might raise an exception
    #age = int(input("Enter your age: "))
    #age = int(age)
#except:
    # code that runs if an exception occurs
    #print("Error: unable to convert that into a number")
#else:
    # code that runs if no exception occurs
    #print(f"Your age is {age}")
#finally:
    # code that always runs
    #print("Program Finished")
    
try:
    print(1/0)
except:
    print("Cannot divide by zero")
    