"""
l=[10,20,30,40]
it=iter(l) 
print(next(it))  #10   next print only one value at a time to save our space.
print(next(it))  #20
print(next(it))  #30
print(next(it))  #40
print(next(it))  #Error StopIteration

"""
'''
#list
l=[10,20,30,40]
it=iter(l) 
for i in it:
    print(i)
'''

'''
#Tuple
l=(10,20,30,40)
it=iter(l) 
for i in it:
    print(i)
'''
"""
#String
text="Ranjeet"
it=iter(text)
for i in it:
    print(i)
"""

class Number:
    def __iter__(self):
        self.num=1
        return self
    
    def __next__(self):
        x=self.num
        self.num +=1
        return x

n=Number()
it=iter(n)

print(next(it))