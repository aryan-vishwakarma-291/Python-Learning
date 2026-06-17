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

from os import name


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
# # print(phonebook)

# pol_eng_dictionary = {"kwiat": "flower"}
# pol_eng_dictionary.update({"gleba": "soil"})
# print(pol_eng_dictionary) # outputs: {'kwiat': 'flower', 'gleba': 'soil'}
# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary) # outputs: {'kwiat': 'flower'}
# print("aryan")

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil",
#     1: "one",
#     }
# if 1 in pol_eng_dictionary:
#    print("Yes it is present in the dectionary")
# else:
#    print("No it is not present in the dictionary")

# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
# print(pol_eng_dictionary) # outputs: {'zamek': 'castle', 'woda': 'water', 'gleba': 'soil'}
# print(len(pol_eng_dictionary)) # outputs: 3
# del pol_eng_dictionary["woda"]
# print(pol_eng_dictionary) # outputs: {'zamek': 'castle', 'gleba': 'soil'}
# print(len(pol_eng_dictionary)) # outputs: 2
# pol_eng_dictionary.clear()
# print(pol_eng_dictionary) # outputs: {}
# print(len(pol_eng_dictionary)) # This will raise an error because the dictionary has been deleted.

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# dictionary['cat'] = 'minou'
# print(dictionary)

# sd = {}
# while True:
#    name = input("Enter name: ")
#    if name == "":
#        break
#    score = int(input("Enter score: "))
#    if score not in range(1,11):
#       break

#    if name in sd:
#       sd[name] += (score,)
#    else:
#       sd[name] = (score,)

# for name, marks in sd.items():
#    sum = 0
#    for mark in marks:
#       sum += mark
#    print(name, "->", sum/len(marks))  

# object oriented programming

# class ThisIsAClass:  # class name should be in camel case
#       name = "Aryan"
#       age = 22

#       def getname(self): # method should have self as the first parameter
#            print(self.name) # self is a reference to the current instance of the class, and it allows us to access the attributes and methods of the class within its own definition.
          
# first_object = ThisIsAClass() # creating an instance of the class

# first_object.getname() # outputs: Aryan
# print(first_object.name) # outputs: Aryan

class Student:
      def __init__(self,name,age,gender,grade): # this is a constructor, it is called when an instance of the class is created
            self.name = name
            self.age = age
            self.gender = gender
            self.grade = grade

      def printDetails(self): # this is a method, it is a function that belongs to a class
            print("Name:", self.name)
            print("Age:", self.age)
            print("Gender:", self.gender)
            print("Grade:", self.grade) 

# mayur = Student()
# print(mayur)

# mayur.name = "Mayur"
# mayur.age = 21
# mayur.gender = "Male"
# mayur.grade = "A"

# print(mayur.name) # outputs: Mayur
# print(mayur.age) # outputs: 21
# print(mayur.gender) # outputs: Male
# print(mayur.grade) # outputs: A

# mayur = Student("Mayur", 21 ,"Male", "A")
# mayur.printDetails()

# verb = input("enter your name: ")
# print(f"I can {verb} better then you")
# print(4*f"{verb} "+verb)


# insance variable
# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val
 
#     def set_second(self, val):
#         self.second = val
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)
# print(example_object_3.third) 


#OOPS Methods

# class Classy:
#     def method(self):
#         print("method")
# obj = Classy()
# obj.method()  
 
# class Classy:
#      def method(self,par):
#           print("method: ", par)
# obj = Classy()
# obj.method("hello")

# class Classy:
#       varia = 2
#       def method(self):
#             print( self.varia, self.var)

# obj = Classy()
# obj.var = 3
# obj.method()

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
# sun = Star("Sun", "Milky Way")
# print(sun)

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
    
#     def __str__(self):
#         return self.name + ' in ' + self.galaxy
# sun = Star("Sun" , "Milky Way")
# print(sun)


#INheritance

# class Vehicle:
#       pass
# class LandVehicle(Vehicle):
#       pass
# class TrackedVehicle(LandVehicle):
#       pass
 

# class Vehicle:
#       pass
# class LandVehicle(Vehicle):
#       pass
# class TrackedVehicle(LandVehicle):
#       pass
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:                  
#       for cls2 in [Vehicle, LandVehicle, TrackedVehicle]  :  
#             print(issubclass(cls1, cls2), end = "\t")
#       print()

# class Super:
#       super_var = 1
# class Sub(Super):
#       sub_var = 2

# obj = Sub()
# obj1 = Super()
# print(obj1.super_var) # outputs: 1
# print(obj1.sub_var) # This will raise an error because sub_var is not defined in the Super class.
# print(obj.super_var) # outputs: 1
# print(obj.sub_var) # outputs: 2

#for contructor 
# class Super:
#         def __init__(self):
#             self.supVar = 1
# class Sub(Super):
#         def __init__(self):
#             super().__init__() # this will call the constructor of the Super class and initialize the supVar variable
#             self.subVar = 2

# obj = Sub()
# print(obj.supVar) # outputs: 1
# print(obj.subVar) # outputs: 2

# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#     def fun_1(self):
#         return 102
    
# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
#     def fun_2(self):
#         return 202
    
# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#     def fun_3(self):
#         return 302
# obj = Level3()
# print(obj.variable_1 , obj.var_1, obj.fun_1()) 
# print(obj.variable_2 , obj.var_2, obj.fun_2()) 
# print(obj.variable_3 , obj.var_3, obj.fun_3()) 


#class variables

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)
# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
# example_object = ExampleClass(1)
# print(example_object.a)
# print(example_object.b)



# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
# example_object = ExampleClass(2)
# print(example_object.a)
# try:
#     print("a=", example_object.a)
# except AttributeError:
#     try:
#         print("b=", example_object.b)
#     except AttributeError:
#         print("The object does not have the attribute 'b'")


# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
# example_object = ExampleClass(1)
# # print(example_object.a)
 
# if hasattr(example_object, 'b'):
#     print("b=", example_object.b)
# if hasattr(example_object, 'a'):
#     print("a=", example_object.a)

# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2
# example_object = ExampleClass()
# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))


# class Python:
#       population = 1000000000
#       victims = 0
#       def __init__(self):
#             self.length = 1
#             self.__weight = 1
# myobj = Python()
# print(myobj.length)
# print(myobj._Python__weight) # this is how we can access the private variable __weight outside the class using name mangling
# print(myobj.population)
# print(myobj.victims)

# Name Mangling in Methods
# class Classy:
#     def visible(self):
#         print("visible")
#     def __hidden(self):
#         print("hidden")
# obj = Classy()
# obj.visible()               # Output: visible
# try:
#     obj.__hidden()          # This fails
# except:
#     print("failed")         # Output: failed
# obj._Classy__hidden() 

# print(type(obj).__name__) # outputs: <class '__main__.Classy'>

# class sampleClass:
#     def __init__(self, val):
#         self.val = val
# obj1 = sampleClass(10)
# obj2 = sampleClass(20)
# obj3 = obj1
# obj3.val = 30

# print(obj1 is obj2) # outputs: False
# print(obj2 is obj3) # outputs: True
# print(obj3 is obj1) # outputs: True
# print(obj1.val) # outputs: 30
# print(obj2.val) # outputs: 20
# print(obj3.val) # outputs: 30

# str1 = "Hello new"
# str2 = "Hello"
# str2 += " new"
# print(str1 == str2 , str1 is str2) # outputs: False False

# class Super:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return "My name is " + self.name + "."
# class Sub(Super):
#     def __init__(self, name):
#       #   Super.__init__(self, name)
#       super().__init__(name) # this is the recommended way to call the constructor of the Super class
# obj = Sub("Andy")
# print(obj)  # Output: My name is Andy.  

#multiple inheritance
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
    
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA, SuperB):
#     pass
# obj = Sub()

# print(obj.var_a, obj.fun_a())  # Output: 10 11
# print(obj.var_b, obj.fun_b())  # Output: 20 21

# class Level1:
#     var = 100
#     def fun(self):
#         return 101
# class Level2(Level1):
#     var = 200        # Overrides Level1.var
#     def fun(self):   # Overrides Level1.fun()
#         return 201
# class Level3(Level2):
#     def fun(self):   # Overrides Level2.fun()
#         return 202
# obj = Level3()
# print(obj.var, obj.fun())  # Output: 200 202

      
# class Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"
# class Right:
#     var = "R"           # Same name as Left.var
#     var_right = "RR"
#     def fun(self):      # Same name as Left.fun()
#         return "Right"
# class Sub(Left, Right):
#     pass
# obj = Sub()
# print(obj.var, obj.var_left, obj.var_right, obj.fun())

# class One:
#     def do_it(self):
#         print("do_it from One")
#     def doanything(self):
#         self.do_it()
# class Two(One):
#     def do_it(self):
#         print("do_it from Two")
# one = One()
# two = Two()
# one.doanything()  # Output: do_it from One
# two.doanything()  # Output: do_it from Two

# # exceptions
# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         return None
#     else:
#         print("Everything went fine")
#         return n
# print(reciprocal(2))  # Uses else branch
# print(reciprocal(0))  # Uses except branch


# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         n = None
#     else:
#         print("Everything went fine")

#     finally:
#             print("This is executed no matter what.")  
#     return n

# print(reciprocal(2))
# print(reciprocal(0))

# try:
#     i = int("Hello!")
# except Exception as e:
#     print(e)
#     print(e.__str__())



# class MyZeroDivisionError(ZeroDivisionError):    
#     pass
# def do_the_division(mine):
#     if mine:
#         raise MyZeroDivisionError("some worse news")
#     else:        
#         raise ZeroDivisionError("some bad news")
# do_the_division(False)

#Stringss

# str1 = "aryan"
# print(str1[1])
# print(str1[-1])

# alpha = "abdefg"

# print(alpha[1:3])
# print(alpha[3:])
# print(alpha[:3])
# print(alpha[3:-2])
# print(alpha[-3:4])
# print(alpha[::2])
# print(alpha[1::2])

text = '  Hello Python World  '
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# #strp whitedpaces

# print(text.strip())

# #search 
# print('Python' in text)
# print(text.find('Python'))
# print(text.count('l'))

# print(text.replace('Python' , 'ML'))

# #Split and Join
# csv = 'Aryan,22,Indore,Engineer'
# parts = csv.split(',')
# print(parts)
# print(parts[0])
# rejoined = ' | '.join(parts)
# print(rejoined)

# #check COntent
# print('hello123'.isalnum())
# print('1234'.isdigit())
# print('Python'.isalpha())
# print(" ".isspace())

# #start and check
# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))

# name,marks,rank = 'Aryan' , 92.567,3

# #basic
# print(f'Hellow , {name}!')

# print(f'Marks , {marks:.2f}')
# print(f'Marks: {marks:.0f}')
# print(f'Count: {100000:,}')

# print(f'{name:<15} | {marks:>8.2f}|Rank:{rank}')

# price , gst = 500 , 0.18
# print(f'Price{price} | Gst{price*gst:.2f} | total {price*(1+gst):.2f}')

# string = "Hellow, How are you doing today?"

#count vowels in the string
#print you from the string
# print the string in reverse order
# nonpali , palin = "abcdef" , "axttxa"
#check if the string os palindrome or nor


# readinf and writind csv,txt files

# with open("data.txt" ,"r") as file:
#       data = file.read()
# print(data)

# with open('student.txt' , 'w') as f:
#       f.write('Rahul sharma,85,Bhopal\n')
#       f.write('Priya Verma,92,Indore\n')
#       f.write('Amit kumar,73,Jabalpur\n')

# with open('student.txt' , 'a') as f:
#       f.write('Sneha Joshi,88,Bhopal\n')
# with open('student.txt', 'r') as f:
#       content = f.read()
# print(content)

# with open('student.txt' , 'r') as  f:
#       for line in f:
#             name, marks , city = line.strip().split(',')
#             print(f'{name:<15} | {marks:>5} | {city}')
#             print("----------")

# creatin CSV files
import csv 
# records = [
#       ['Name' , 'Marks' , 'City' , 'Grade'],
#       ['Rahul' , 87 , 'Bhopal' , 'A'],
#       ['Aryan' , 85 , 'Indore' , 'B'],
#       ['Akash' , 89 , 'Ujjain' , 'C'],
#       ['Aman' , 90 , 'Jabalpur' , 'A'],
# ]

# with open('students.csv' , 'w' , newline='') as f:
#       csv.writer(f).writerows(records)

# with open('students.csv' , 'r') as f:
#       for row in csv.DictReader(f):
#             print(f'{row["Name"]} :{row["Marks"]} Marks({"City"})')

# StuRec = [
#       ['Name' , 'Age' , 'Marks'],
#       ['Aryan', 21 , '90'],
#       ['Akash' , 20,  '85'],
#       ['Aman' , 22 , '92'],
# ]

# with open('student.csv' , 'w' , newline='') as f:
#       csv.writer(f).writerows(StuRec)
# flag = 0
# with open('student.csv' , 'r') as f:
#       name = input("Enter Name of Student")
#       for row in csv.DictReader(f):
#             if row["Name"] == name:
#                   flag = 1
#                   break
# if flag == 1:
#        print(f'{row["Name"]} :{row["Marks"]} Marks({"City"})')
# else:
#       print("Record Not Found")

# import numpy as np
# arr1d = np.array([1,2,3,4,5])
# arr2d = np.array([[11,22,33],[44,55,66],[77,88,99]])
# print(arr2d.shape)
# print(arr2d.dtype)
# print(arr2d.ndim)

# zeros = np.zeros((3,4))
# # 3x4 array of zeros
# print(zeros)

# ones = np.ones((2,5))
# #2x5 array of 1
# print(ones)

# rng = np.arange(0,50,5)
# #[o,5,10,15 ......45]
# print(rng)
         
# lin = np.linspace(0,1,11)
# print(lin)

# random = np.random.randint(40,100,(5,3))
# print(random)

# arr = np.array([10,20,30,40,50])
# print(arr*2)
# print(arr+5)
# print(arr**2)

# marks_2d = np.array([[85,90,78],[72,88,95],[91,76,83]])

# print(np.mean(marks_2d)) #mean of whole array
# print(np.mean(marks_2d,axis=1)) #mean per row
# print(np.mean(marks_2d,axis=0)) #mean per coloumn
# print(np.max(marks_2d)) #max number from 3=2d array
# print(np.std(marks_2d)) #standard deviation

# arr = np.array([55,82,43,91,67,78,35,83])
# print(arr[arr>70])

# Pandas

import pandas as pd

data = {
      'Name': ['Rahul' , 'Priya' , 'Amit' , 'Sneha' , 'Vikram'],
      'Age': [22,21,23,20,24],
      'Marks': [85,92,78,83,73],
      'City': ['Bhopal','Indore','Bhopal','Jabalpur','Indore']
}
df = pd.DataFrame(data)
# print(df)

# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())

#select column 
# print(df['Name'])
# print(df[['Name','Marks']])

#Filter rows
# print(df[df['Marks'] >= 85])
# print(df[df['City'] == 'Bhopal'])
# print(df[(df['Marks'] >= 80) & (df['City'] == 'Indore')])

# def get_grade(x):
#       if x >= 90:
#             return 'A'
#       elif x >= 75:
#             return 'B'
#       else:
#             return 'C'
# df['Grade'] = df['Marks'].apply(get_grade)
# print(df['Grade'])

#group By 
# city_avg = df.groupby('City')['Marks'].mean()
# print(city_avg)

# create new CSV file 
# df2 = pd.read_csv('students.csv')
# print(df2)
# print("-----------------")
# df2['Name'] , df2['City'], df2['Grade'] = df2['Name'].str.strip()  ,  df2['City'].str.replace('#', ''), df2['Grade'].str.replace('#','')
# df2['Marks'] = df2['Marks'].replace('$','')
# print(df2)


# data cleaning 
# df2.to_csv('clean_output.csv' , index=False) 


#matplotlib

import matplotlib.pyplot as plt

# months = ['Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'June' , 'July' , 'Aug' , 'Sep' , 'Oct' , 'Nov' , 'Dec']
# sales = [45,52,48,61,58,72,69,75,68,82,90,95]

#line chart

# plt.figure(figsize=(12,5))
# plt.plot(months,sales,marker = 'o' , color= 'steelblue' , linewidth = 2 , markersize=8)
# plt.fill_between(months,sales,alpha=0.15,color='steelblue')
# plt.title('Monthly Sales 2026 (Rs. Thousands)', fontsize=14 , fontweight= 'bold')
# plt.xlabel('Month')
# plt.ylabel('Sales (Rs, K)')
# plt.grid(True, alpha = 0.3)
# plt.tight_layout()
# plt.show()


#Bar chart
# cities = ['Bhopal' , 'Indore' , 'Jabalpur' , 'Gwalior' , 'Ujjain']
# Students = [1200 , 2000 , 900 , 850 , 600]
# colors = ['#2196F3' , '#4CAF50' , '#FF9800' , '#9C27B0' , '#F44336']

# #BAr chart
# plt.figure(figsize=(9,5))
# bars = plt.bar(cities,Students, color=colors, edgecolor='white',linewidth=1.5)
# plt.title('Students enrolled per city')
# plt.ylabel('Number of Students')
# for bar,val in zip(bars,Students):
#       plt.text(bar.get_x() + bar.get_width()/2, val+30 , str(val) , ha='center',fontweight='bold')
# plt.tight_layout()
# plt.show()

#scatter plot
# import numpy as np

# study_hrs = np.random.uniform(2,10,50)
# marks = study_hrs*7+np.random.normal(0,8,50)
# marks = np.clip(marks,30,100)

# plt.figure(figsize=(8,5))
# plt.scatter(study_hrs,marks,c=marks,cmap='RdYlGn', s=100, alpha=0.8)
# plt.colorbar(label='Marks')
# plt.title('Study Hours vs Exam Marks')
# plt.xlabel('Study Hours/Day')
# plt.ylabel('Exam Marks')
# plt.show()

# seaborn library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    'marks': np.random.randint(40, 100, 100),
    'study_hours': np.random.uniform(2, 10, 100),
    'city': np.random.choice(['Bhopal', 'Indore', 'Jabalpur'], 100),
    'gender': np.random.choice(['Male', 'Female'], 100)
})

# Histogram
# plt.figure(figsize=(10, 4))
# sns.histplot(df['marks'], bins=20, kde=True, color='steelblue')
# plt.title('Distribution of Student Marks')
# plt.show()

# Box plot — outliers and spread per group
# sns.boxplot(data=df, x='city', y='marks', palette='Set2')
# plt.title('Marks Distribution by City')
# plt.show()

# Correlation Heatmap — critical in data science
# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks','study_hours']].corr(),annot=True,cmap='coolwarm',vmin=-1,vmax=1)
# plt.title('Correlation Matrix')
# plt.show()

# Pair plot — all relationships at once
# sns.pairplot(df[['marks','study_hours']],diag_kind='kde')
# plt.show()

# Statistics for AIML 

