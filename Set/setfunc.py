# set union,intersection,difference,symmetric difference
a={1,2,3,4,5}
b={5,6,7,8,9,}
#print(a.union(b))//union
print(a|b)

#print(a.intersection(b))//intersection
print(a&b)

#print(a.difference(b))//difference
print(a-b)

#print(b.difference(a))
print(b-a)

#print(a.symmetric_difference(b))//symmetric difference
print(a^b)

#set operations
a={1,2,3,4,5}
b={5,6,7,8}
c={5,8,9,10,11}

print(a|b|c)
print(a&b&c)
print(a-b-c)
print(a^b^c)
