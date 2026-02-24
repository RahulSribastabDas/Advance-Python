#Calculator using match case
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = input("Enter your choice: 1,2,3,4:")

match choice:
  case "1":
    print(f"Addition is ,{a+b}" )
  case "2":
    print(f"Subtraction is ,{a-b}" )
  case "3":
    print(f"Multiplication is ,{a*b}" )
  case "4":
    print(f"Division is ,{a/b}" )
