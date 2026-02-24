# different adding function in list
list = [10,20,30,40,50]
list.append(60)
print(list)

list.insert(2, "Rahul")
print(list)

list.extend(["Das", 90,100])
print(list)

# different removing function in list
list = [10,20,30,40,50]
list.remove(20)
print("list after removing 20, list")

list.pop(2)
print("list after pop 2nd element", list)

list.clear()
print("list after clear", list)

#
list = [10,20,30,40]

if 20 in list:
  print("20 is present in the list")
else:
  print("20 is not present in the list")