book = {"Author":"J.K Rowling",
        "Title":"Harry Potter",
        "Price":2000}
book2= {"Author":"William Shakespeare",
        "Title":"Merchant of Venice",
        "Price":3000}

print(book)
x=book.get("Author")
print(x)
y=book.get("Title")
print(y)
z=book.get("Price")
print(z)
x=book.keys()
print(x)
y=book.values()
print(y)
y=book2.keys()
print(y)
x=book2.values()
print(x)
x=book.items()
print(x)
y=book2.items()
print(y)


#Update function
book = {"Author":"J.K Rowling",
        "Title":"Harry Potter",
        "Price":2000}
book["Publication"]="Rowling ltd" #add the new key and value
print(book)
book.update({"Author":"William Shakespeare"})#updating the value
print(book)

#delete the item in dictionary
book = {"Author":"J.K Rowling",
        "Title":"Harry Potter",
        "Price":2000}
print(book)
book.pop("Price")#delete th existing key and value
print(book)
#book.popitem()#for the deletion of last key and value
#print(book)
#book.clear()#remove all item from dict and print empty dict
#print(book)


#using if else and membership function find the dictionary
book = {"Title": "Harry Potter", "Author": "J.K Rowling", "Price": 1000}
key = "Author"

if key in book:
    print("Key found:", book[key])
else:
    print("Key not found")

    