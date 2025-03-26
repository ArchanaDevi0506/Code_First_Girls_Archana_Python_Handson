#list indexing
fruits = ["apple", "orange", "Plums", "grapes", "banana", "cherry"]

#We can use list slicing to get sublists
fruits_sublist = fruits[0:3]
print(fruits_sublist)

#We can also use an optional step argument
fruits_sublist = fruits[0::3]
print(fruits_sublist)

fruits_sublist = fruits[::-1]
print(fruits_sublist)


a= [1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)