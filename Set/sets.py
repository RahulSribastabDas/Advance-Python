#function on set
s={1,2}
print(s)
print(type(s))

a={1,2,3,4,5}
a.add(6)
print(a)
a.remove(1)
print(a)
a.update([1,2])
print(a)

s = list([1, 2, 3, 4])
print(s)
s1 = tuple((1, 2, 3, 4))
print(s1)
s2 = dict(enumerate(s1))
print(s2)
s2.update({4: 5})
print(s2)
s3 = set(s2)
print(s3)
s3.add(10)
print(s3)

s = {2,2,4,"hi","apple","kiwi"}
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)
s.discard("kiwi")
print(s)
s.pop()
print(s)

s = {2,2,5,"hi","apple","kiwi"}
s.update([2,3])
print(s)

# constructor for set, tuple, list and dictionary
s=set((1,2,4,3,897,98,786))
print(s)
print(type(s))

d=dict(name="Rahul",roll_no=456,marks={90,45,43})
print(d)
print(type(d))

t=(1,2,4,3,897,98,786)
print(t)
print(type(t))

l=[1,2,4,3,897,98,786]
print(l)
print(type(l))