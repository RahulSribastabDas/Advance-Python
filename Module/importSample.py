import MyModule as mm
print(mm.sub(10,5))
print(mm.mul(10,5))
print(mm.div(10,5))
print(mm.add(10,5))
print(dir(mm))

for i in dir(mm):
    print(i)