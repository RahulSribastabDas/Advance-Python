#List Comprehension
'''I=[1,2,3,4,5]
empty_list = [i*1 for i in I] #Syntax [expression for variable _name in iterable]
print(empty_list)'''

#convert l=["ram","seeta","riya"] to l1=["RAM","SEETA","RIYA"]
'''l=["ram","seeta","riya"]
l1=[i.upper() for i in l]
print(l1)'''
# [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)] list comprehesion
l=[(i,j) for i in range(3) for j in range(3)]
print(l)

#list to dictionary
I=[1,2,3,4,5]
D={i: i**2 for i in I}
print(D)

