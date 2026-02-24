#match case example
choice = input("Enter your choice: 1, 2, 3, 4: ")

match choice:
    case "1":
        print("Tea")
    case "2":
        print("Coffee")
    case "3":
        print("Sorry invalid choice")
    case _:
        print("Invalid choice")

        