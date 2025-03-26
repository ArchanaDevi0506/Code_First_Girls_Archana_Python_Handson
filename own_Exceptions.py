# Create an exception for too high and too low
class ValuetooHigh(Exception):
    pass
class ValuetooLow(Exception):
    pass
#using the raise keyword
try:
    input = int(input("Please enter a number between 5 and 10:"))
    if input < 5:
        raise ValuetooLow
    if input > 10:
        raise ValuetooHigh
except:
    print("Error: Number is not in the range of 5 to 10")