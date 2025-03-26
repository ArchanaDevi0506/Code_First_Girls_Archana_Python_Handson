# using the raise keyword

try:
    input = int(input("Please enter a number between 5 and 10:"))
    if input < 5 or input > 10:
        raise Exception("Number is not in the range of 5 to 10")
except:
    print("Error: Number is not in the range of 5 to 10")