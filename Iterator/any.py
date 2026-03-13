l=[10,20,30,40,0]  
print(any(l))    # if any value will true it will show True 
print(all(l))    # if all value will true then only it will show True otherwise False

print(any(i>10 for i in l))
print(all(i>10 for i in l))