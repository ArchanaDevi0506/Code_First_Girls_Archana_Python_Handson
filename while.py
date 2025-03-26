#while loops
#lets create a countdown

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    
#Controlling the flow of loop
#break statement
for i in range(5):
    if i == 3:
        break
    print(i)
    
#continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)