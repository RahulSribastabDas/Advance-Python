#List Comprehension
'''I=[1,2,3,4,5]
empty_list = [i*1 for i in I] #Syntax [expression for variable _name in iterable]
print(empty_list)'''

#convert l=["ram","seeta","riya"] to l1=["RAM","SEETA","RIYA"]
l=["ram","seeta","riya"]
l1=[i.upper() for i in l]
print(l1)

