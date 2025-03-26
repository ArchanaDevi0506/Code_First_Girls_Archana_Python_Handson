#Adding, Replacing, and Removing Elements in a List
#We can add items with append, insert and extend.
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("grapes")
print(fruits)
fruits.insert(0, "Kiwi")
print(fruits)
fruits.extend(["orange", "Pears"])
print(fruits)

#We can remove items with clear, remove and pop
fruits.pop()
print(fruits)

fruits.remove("cherry")
print(fruits)

fruits.clear()
print(fruits)
