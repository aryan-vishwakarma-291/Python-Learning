# x = ["maruti" , "bmw"]
# y =  ["maruti" , "bmw"]
# z = x
# print("maruti" not in x)

# input 
# name = input("Enter name ")
# print(name)

#IF-eLSE
# sum = 11
# if sum > 0:
#     print("high")
# elif sum > 10:
#     print("mid")
# else:
#     print("low")

#example to find largest number

# a = int(input("enter first number: "))
# b = int(input("Enter second number: "))

# if a>b:
#     print("a is big number")
# else: 
#     print("b is bigger")


# b = int(input("Enter second number: "))
# a = int(input("enter first number: "))

# largest = max(a,b)
# print(largest)

# odd_numbers = 0
# even_numbers = 0
# Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))
# 0 terminates execution.
# while number != 0:
# Check if the number is odd.
    # if number % 2 == 1:
# Increase the odd_numbers counter.
    #     odd_numbers += 1
    #     number = int(input("Enter a number or type 0 to stop: "))
    # else:
# Increase the even_numbers counter.
        # even_numbers += 1
        # number = int(input("Enter a number or type 0 to stop: "))

# Read the next number.
# number = int(input("Enter a number or type 0 to stop: "))
# Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)


#for loop
# for i in range(5):
#     print("aryan")

# for counter in range(1):
#     print("The value of counter is currently", counter)

#break and continue loop
# break - example
# print("The break instruction:")
# for counter in range(1, 6):
#     if counter == 3:
#         break
#     print("Inside the loop.", counter)
# print("Outside the loop.")

# print("\nThe continue instruction:")
# for counter in range(1, 6):
#     if counter == 3:
#         continue
#     print("Inside the loop.", counter)
# print("Outside the loop.")

# counter = 1
# while counter < 5:
#     print(counter)
#     counter += 1
# else:
#     print("else:", counter)

# counter = 5
# while counter < 5:
#     print(counter)
#     counter += 1
# else:
#     print("else:", counter)

# for counter in range(5):
#     print(counter)
# else:
#     print("else:", counter)


#logical expression
# var = 1
# print(var > 0)
# print(not (var <= 0))

i = 1
j = not not i
print(j)