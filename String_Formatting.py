#String Formatting format() method
name = "Hari"
age = 30
message = "My name is {} and I am {} years old".format(name, age)
print(message)

#String Formatting f Strings
message = f"My name is {name} and I am {age} years old"
print(message)

#String Formatting Addtion / Concatenation
message = "My name is " +name+ " and I am " +str(age)+ " years old"
print(message)

a=f"5 + 3 = {5 + 3}"
print(a)