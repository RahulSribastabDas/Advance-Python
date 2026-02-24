dict2={"Name":"Rajeev",
       "Age":25,
       "Nationality":"Indian",
       "Gender":"Male",
       "Proffesion":"Data Analyst"}

print(dict2)
x=dict2.get("Name")
print(x)
y=dict2.values()
print(y)
y=dict2.keys()
print(y)
x=dict2.items()
print(x)
x=dict2.pop("Gender")
print(dict2)
x=dict2.update({"Name":"Rahul"})
print(dict2)
dict2.popitem()
print(dict2)
#x=dict2.clear()
#print(dict2)

dict2 = {
    "Name": "Rajeev",
    "Age": 25,
    "Nationality": "Indian",
    "Gender": "Male",
    "Profession": "Data Analyst"
}
print("Keys")
for key in dict2:
    print(key)
print("Values")
for value in dict2.values():
    print(value)
print("Key: Value")
for key, value in dict2.items():
    print(f"{key}: {value}")