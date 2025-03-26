#json

import json
person = {
    "name": "Hari",
    "age": 30,
    "City": "Edinburgh"
}
print(person)
json_person = json.dumps(person)
print(json_person)