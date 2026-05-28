# print("aryan")
# def message():
#     print("Enter value:")

# message()
# a = int(input())

# message()
# b = int(input())

# message()
# c = int(input())

# print("Sum:", a + b + c)

# def message():
#     print("Enter a value: ")
# print("We start here.")
# message()
# print("We end here.")

# print("We start here.")
# message()
# print("We end here.") 
# def message():
#     print("Enter a value: ")

# def message():
#     print("Enter a value: ")
#     temp = int(input())
#     return temp

# a = message()
# b = message()
# c = message()

# print("a:", a)
# print("b:", b)
# print("c:", c)

# def hi():
#     print("Hi there!")
# hi()

# def hi(name):
#     print("Hi", name)

# hi("Aryan")

# def message(number):
#     print("Enter a number:", number)
# number = 1234
# message(1)
# print(number) 

# def message(what, number):
#     print("Enter", what, "number", number)
# message("telephone", 11)
# message("price", 5)
# message("number", "number")

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
 
# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
# introduction(first_name = "James", last_name = "Bond")
# introduction(last_name = "Skywalker", first_name = "Luke")

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)

# adding(1, 2, 3)
# adding(c = 1, a = 2, b = 3)
# adding(3, c = 1, b = 2)
# adding(3, a = 1, b = 2)

# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year!")
# # happy_new_year()
# happy_new_year(False)

# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123
# print("This lesson is interesting!")

# temp = boring_function()
# print("This lesson is boring...", temp)

# def checkMy(variable):
#     if(variable == 10):
#         print("Variable is 10")
#         return 2
#     else:
#         print("Variable is not 10")
#         return 

# checkMy(5)
# print(checkMy(10))

# def list_sum(lst):
#     s = 0
#     for elem in lst:
#         s += elem
#     return s
# print(list_sum([5, 4, 3]))


# def strange_list_fun(n):
#     strange_list = []
#     for i in range(0, n):
#         strange_list.insert(0, i)
#     return strange_list
# print(strange_list_fun(5))

# def isint(d):
#     if type(d) == int:
#         return True
#     elif type(d) == float:
#         return False
            
# print(isint("5"))

# def lis(lst):
#     ipf = []
#     for i in lst:
#         i = i ** 2
#         ipf.append(i)
#     return ipf

# foo = [1, 2, 3, 4]
# print(lis(foo))

# def scope_test():
#   x = 123
# scope_test()
# print(x)

# def my_function():
#     print("Do I know that variable?", var)

# var = 1
# my_function()
# print(var)

# def mult(x):
#     var = 7
#     return x * var

# var = 3
# print(mult(7))

# def my_function():
#     global var
#     var = 2
#     print("Do I know that variable?", var)
# var = 1
# my_function()
# print(var)
# var = 3
# print(var)

# var = 2
# print(var) # outputs: 2
# def return_var():
#     global var
#     var = 5
#     return var

# print(return_var()) # outputs: 5
# print(var)

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)

# var = 1
# my_function(var)
# print(var)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)

# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0] # Pay attention to this line.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)

# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# a = 0

# def recursion(n):
#     print(n)
#     if n == 5:
#         return 
#     else:
#         print("going in rec " , n)
#         recursion(n + 1)
#         print("coming out of rec " , n)
# print("starting recursion")
# print(recursion(a))
# print("ending recursion")

# a = 5

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(a))

# my_tuple = (1, 10, 100)
# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3
# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

# tuple
# Example 1
# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)
# Example 2
# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)
# Example 3
# tuple_3 = (1, 2, 3, 4)
# print(len(tuple_3))
# print(5 not in tuple_3)
# # Example 4
# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 2 
# print(tuple_4)
# print(tuple_5)

# my_tuple = tuple((1, 2, "string"))
# print(my_tuple)
# my_list = [2, 4, 6]
# print(my_list) # outputs: [2, 4, 6]
# print(type(my_list)) # outputs: <class 'list'>
# tup = tuple(my_list)
# print(tup) # outputs: (2, 4, 6)
# print(type(tup)) # outputs: <class 'tuple'>


# var = 123
# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)
# t1, t2, t3 = t2, t3, t1
# print(t1, t2, t3)

dictionary = {
"cat": "chat", 
"dog": "chien", 
"horse": "cheval"
   }
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}
# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))
# name = {1: "Aryan", 2: "Satyarth", 3: "Shivam"} 
# print(name)

# print(dictionary["cat"])
# print(phone_numbers["presinde"])

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse']
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for key in dictionary.keys(): 
#     print(key, "->", dictionary[key])

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# for english, french in dictionary.items():
#     print(english, "->", french)

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# for french in dictionary.values():
#     print(french)

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
# copy_dictionary = pol_eng_dictionary.copy()

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
# pol_eng_dictionary["woda"] = "juice"
# pol_eng_dictionary["gleba"] = "earth"
# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# item2 = pol_eng_dictionary["gleba"]
# item3 = pol_eng_dictionary["woda"]
# print(item) # outputs: lock
# print(item2) # outputs: earth   
# print(item3) # outputs: juice

# phonebook = {}
# phonebook["Alice"] = 1234567890
# print(phonebook)
# del phonebook["Alice"]
# print(phonebook)

pol_eng_dictionary = {"kwiat": "flower"}
pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower', 'gleba': 'soil'}
pol_eng_dictionary.popitem()
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower'}
print("aryan")
