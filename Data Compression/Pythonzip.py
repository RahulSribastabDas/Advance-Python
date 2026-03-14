import zipfile
with zipfile.ZipFile("Python.zip", "w") as f:
    f.write("file4.txt")
    f.write("file5.txt")
    f.extractall()
    print(f.namelist())
