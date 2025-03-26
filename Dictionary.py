#Dictionaries

person = {
    "name": "Hari",
    "age": 30,
    "City": "Edinburgh"
}
print(person)
print(person["name"])
person["name"] = "Archana"
print(person)
del person["name"]
print(person)
person["address"] = "123 South Gyle Wynd"
print(person)
person.update({"age": 26})
print(person)
person.clear()
print(person)

my_dict = {
    "a" : 1,
    "b" : 2
}
print(my_dict['b'])