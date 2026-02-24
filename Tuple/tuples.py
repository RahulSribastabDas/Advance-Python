#write a program to write a tuple in python
my_tuple=(10,20,30,40)

print("Tuples:",my_tuple)


###2
tu = (2, 1, 3, "Hi", True)
list1 = list(tu)
print(list1)
list1.append(4)
print(list1)
tu = tuple(list1)
print(tu)

###3
#pack and unpacked tuple
tu=(1,2,3,4,5,6,3,2456)
(a,b,c,d,e,f,g,h)=tu
print(a,b)
print(e)