f=open("file1.txt", "r")
print(f.name)  # it will return the name of the file
print(f.mode)  # it will return the mode in which the file is opened    
print(f.closed)  # it will return False if the file is open and True if the file is closed
f.close()  # it will close the file