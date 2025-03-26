#Dictionary Methods

person = {
    "name": "Hari",
    "age": 30,
    "City": "Edinburgh"
}
print(person)

#returns all the keys in the dictionary
print(person.keys())

#returns all the values in the dictionary
print(person.values())

#get is a safe way to check for a key, value pair
print(person.get("name"))


