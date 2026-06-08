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

# i = 1
# j = not not i
# print(j)

#lists

number = [1,2,3] #declaration 
# print(number) # initialisation
# print(number[0]) #print value at index 0

# number[0] = 101 # assign value at index 0
# print(number)

# number[0] = number[2] #copy value at index 2 to index 0
# print(number)

# print(len(number)) # to print number od elements in a list

# del number[0] # to delete a nubmer at index 0
# print(number)

# print(number[-1])

number.append(4)
# print(number)

# number.insert(1,5)
# print(number)

# traversing through a list
# for item in range(len(number)):
#     print(item)

# list1 = []
# for i in range(1,11):
#     list1.append(i)

# for i in range(len(list1)):
    # print(list1[i])

# my_list = [10, 1, 8, 3, 5]
# total = 0
# for i in my_list:
#     total += i
# print(total)


# variable_1 = 1
# variable_2 = 2

# variable_1 , variable_2 = variable_2 , variable_1 #to interchange value by copying
# print(variable_1)
# print(variable_2)


# my_list = [10, 1, 8, 3, 5]
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
# print(my_list)


# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)


# lst = [5, 3, 1, 2, 4]
# print(lst)
# lst.reverse()
# print(lst)  # outputs: [4, 2, 1, 3, 5

# lst = ["D", "F", "A", "Z"]
# lst.sort()
# print(lst)

# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

