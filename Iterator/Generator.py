# def add(a,b):
#     return a+b
# s=add(9,6)

def num():
    yield 1
    yield 2
    yield 3
    yield 4
n=num()
for i in n:
    print(i)