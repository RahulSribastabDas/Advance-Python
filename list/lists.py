# list datatpye
list = [10,20,30,40,50]
print(list)

#sum of list using for loop
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total = total + num
print(f"Final Sum: {total}")

#even number from list
numbers = [10,20,30,40,45,65]
even_numbers=[num for num in numbers if num %2 ==0]
print("Even numbers from list:",even_numbers)