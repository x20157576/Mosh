customer = {
    "name": "John Smith",
    "age": 30, 
    "is_verified": True
}


print(customer.get("name","no name"))

customer["birthdate"] = "Jan 1 1980"

print(customer.get("name","no name"))
print(customer.get("birthdate","no date"))

