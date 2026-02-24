#checking the datatype in function
def add(a,b):
  print(a+b)
x = add(10,20)
print(type(x))

#checking the datatype in function
def add(a,b):
  return(a+b)
x = add(10,20)
print(type(x))

def stu(name,age,rollno,sec):
  print(f"Good Morning ji !! \nHello my name is {name}\n my age is {age} \n my roll no. is {rollno} \n my sec is {sec}")

stu("Rahul",20,101,"I")


#bank details
def bank(customer_name,age,account_no,branch,ifsc_code,balance,account_type):
  print(f"Good Morning !!\nYour Details\nCustomer Name: {customer_name}\nAge: {age}\nAccount Number: {account_no}\nBranch: {branch}\nIFSC Code: {ifsc_code}\nBalance: {balance}\nAccount Type: {account_type}")

bank("Rahul",19,34567235,"Parlakhemundi","SBI00N23",25000,"Savings")


#used keyword arguments
def book(book_name,author_name,price,quantity):
  print(f"Book Name:{book_name}\nAuthor Name:{author_name}\nPrice:{price}\nQuantity:{quantity}")

book(book_name="Merchant of Venice ",author_name="William Shakespeare",price=500,quantity=2)
book(book_name="Macbeth ",author_name="William Shakespeare",price=600,quantity=2)

##
def stu(*name):
  print("Suprabhat",name)
  print(type(name))
  print(len(name))
  print("First Name:", name[0])
  print("Last Name:", name[-2])

stu("Madhav","Shyam","Vasudev","Krishna","Devkinandan","Gopal","Dwarkadish")

# Combine all arguments
def stu(*name,rollno,branch):
  print(f"I have joined it 3 years ago and my name is {name}, i am studying in {branch[0]} and my roll no is {rollno}")
  print(len(branch))
  print(type(branch))
  for i in name:
    print("Good morning :",i)
  print("First Branch is :",branch[0])
  print("Last Branch is ",branch[-1])

stu("Ram","Raj", rollno="23CSE546", branch=("CSE","IT","ECE"))

# function with dictionary
def stu(info):
  print("Name :",info["name"])
  print("Roll No :",info["rollno"])
  print("Branch :",info["branch"])
  print("Marks :",info["marks"])
  print("Attendance :",info["attendance"])
  print(type(info))
info={"name":"Rahul","rollno":"23CSE546","branch":"CSE","marks":90,"attendance":"Present"}
stu(info)

def stu(info):
  print("Name of Student:",info["Name"])
  print("Blood Group of Student:",info["Blood group"])
  print(type(info))
  print(len(info))
info={"Name":"Rahul","Age":19,"Blood group":"O+ve"}
stu(info)

#Arbitary Keyword Arguments
def stu(info):
  print("Name of Student:",info["Name"])
  print("Blood Group of Student:",info["Blood group"])
  print(type(info))
  print(len(info))

student_details = {"Name":"Rahul", "Age":"19", "Blood group":"O+ve", "City":"Delhi"}
stu(student_details)

#Online Bill Payment
def online_bill(name,prices,discount="10"):
  total=sum(prices)
  discount_amount=total*(float(discount.strip('%'))/100)
  final_amount=total-discount_amount
  print(f"Customer name:{name}")
  print(f"Total amount to be paid:{total}")
  print(f"Final amount to be paid:{final_amount}")
  print(f"Discount is :{discount_amount}")


online_bill("Rahul",[60,40,30,20],discount="10%")

#Employee details
def employee_details(name,department="IT",**other_details):
  print(f"Employee Name :{name}")
  print(f"Employee Department :{department}")
  print(f"Employee Other Details:")

  for key,values in other_details.items():
    print(f"{key} : {values}")


other_details_emp1={"emp_id":"546","City":"Gunupur"}
employee_details("Rahul",**other_details_emp1)

other_details_emp2={"emp_id":"706","City":"Gunupur"}
employee_details("Ranjeet",**other_details_emp2)

#Bank Details
def bank_d(name, balance, bank="SBI"):
    print("Name:", name)
    print("Bank:", bank)
    print("Initial Balance:", balance)

    balance += 2000
    print("Deposited:", 2000)

    balance += 1500
    print("Deposited:", 1500)

    balance -= 1000
    print("Withdrawn:", 1000)

    balance -= 500
    print("Withdrawn:", 500)

    print("Final Balance:", balance)
    print()

bank_d("Rahul", 10000)
bank_d("Anita", 15000, "HDFC")

#lambda functions
add=lambda a,b:a+b
print("Addition:",add(10,20))

#lambda square
mul=lambda a,b:a*b
print("Multiplication:",mul(10,20))



# filter returns only True value
# syntax = filter(function, iterable)
l=["Ram","Sita","Adi","Ramesh"]
s=filter(lambda name:len(name)>3,l)
print(list(s))

#print the even number by using lambda and filter function
l=[1,2,3,4,5,6,7]
e=filter(lambda a:a%2==0,l)
print(list(e))