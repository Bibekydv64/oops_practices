# // OOP + LeetCode-Style Questions — 100
# Qn) LEVEL 1 — OOP Foundation | Q1–20


# Qn) Create a Student class with name and age.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
Student_obj = Student('bibek',12)
# print(Student_obj.name)


# Qn) Create a Car class with start() and stop().
class Car:
    def start(self):
        return  "i am start"
    def stop(self):
        return "i am stop"


obj = Car()
# print(obj.start())
# print(obj.stop())



# Qn) Create a Rectangle class and calculate area.
class Rectange:

    def rectange1(self,length,breath):
        self.length = length
        self.breath = breath
        area =  length * breath
        return(f"your area:{area}")
    
# obj = Rectange()
# print(obj.rectange1(12,13))

# Qn) Create a Book class with title, author, and price.
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self._price = price

# obj = Book('legend python','mangle lal',123)
# print(obj._price)


# Qn) Create a Counter class with increment/decrement.

class Counter:
    def __init__(self,parameter):
        self.parameter = parameter

    def counter_increment(self):
        self.counter1 = 0
        for num in range(self.paramete +1):
            self.counter1 += 1
            return f"total incremnet count:{self.counter1}"

    def counter_decrement(self):
        for num in range(self.parameter +1):
            self.counter1 -=1
        return f"Total decrement counter:{self.counter1}"


# obj = Counter(5)
# print(obj.counter_increment())

        


# Qn) Create a Student class that calculates average marks.
class Student:
    def calcuate(self,markoflist):
        total_marks = 0
        couter_variable = 0

        for list in markoflist:
            total_marks += list
            couter_variable +=1
        avg = total_marks / couter_variable
        return (f"avg marks of student:{avg}")


# obj = Student()
# print(obj.calcuate([1,2,3,4,56,78]))


# Qn) Create a ShoppingCart class that calculates total price.

class ShopingCard:
    def __init__(self,priceOFList):
        self.PriceOfList = priceOFList


    def Shoping_Card(self):
        sum_counter = 0
        list = []
        for sum in self.PriceOfList.values():
            sum_counter += sum

        for j in self.PriceOfList.keys():
            list.append(j)

        return f"total Price of bunchs:{sum_counter} \n name:{list}"

# obj = ShopingCard({'english':12,'math':23,'phyces':34,'chemistery':46 })
# print(obj.Shoping_Card())


# Qn) Create a Point class with x/y coordinates.
class Point:
    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y

    def cordinates(self):
        return "{}/{}".format(self.x_cord , self.y_cord)

# obj = Point(2,3)
# print(obj.cordinates())

# Qn) Create a Time class with hour/minute/second.
class Time:
    def __init__(self,hr,min,sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def __str__(self):
        return f"hour:{self.hr} min:{self.min} sec:{self.sec}"

    def access_min(self):
        pass

# obj = Time(2,3,4)
# print(obj)



# Qn) Create a Person class and calculate age from birth year.
class Person:
    def __init__(self,other):
        self.time_information = other

    def calcuate_birth(self):
        months = self.time_information[1]
        days = self.time_information[-1]
        months_calcuation = 12 - months 
        days_calcuation = 30 - days
        final_result = f"Remaning Months:{months_calcuation}\nRemaning Days:{days_calcuation}"

        return final_result

# obj = Person([2063,7,25])
# print(obj.calcuate_birth())



#  LEVEL 3 — Encapsulation | Q41–55
# Qn) Create a BankAccount with private balance.

class BankAccount:
    def __init__(self,pin,name):
        self.name = name
        self.__pin = pin

    def getter_pin(self):
        return f"this is private attributes🙅:{self.__pin}"
    
    def setter_Pin(self):
        user_new_pin = input('Enter a new pin:')
        self.__pin = user_new_pin
        return f"pin change sucesfully:{self.__pin}"


obj = BankAccount('parash',1234)
# # print(obj.getter_pin())
# print(obj.setter_Pin())
# # chainging = obj.name = 'bibek'
# # print(obj.name)

# # # obj._BanKAccount__pin = '4331'
# # print(obj._BankAccount__pin)

# Qn) Prevent withdrawal when balance is insufficient.
class Withdrowl:
    def __init__(self,balance):
        self.__balance = balance


    def withdrowl(self):
        user_input_withdrowl_balance = int(input('Enter a withdrowl amount:'))
        if self.__balance > user_input_withdrowl_balance:
            self.__balance =  self.__balance - user_input_withdrowl_balance
            return (f"withdrowl sucessfully:\n Curent balance:{self.__balance}")
        else:
            return ('Chal nikal garib:')
    def getter_balabce(self):
        return (f"current balance{self.__balance}")
    
# obj = Withdrowl(20000)
# print(obj.withdrowl())
# Qn) Create a password class with validation.

# Qn) Create an ATM class with PIN verification.
class Atm:
    def __init__(self):
        self.__pin = 1234

    def pin_verfication(self):
        user_input_verification_pin = int(input('Enter a Verification Pin:')) 
        if self.__pin == user_input_verification_pin:
            return (f"Pin veridied Sucessfully:")
        else:
            return (f"invalid pin sir:")

# obj = Atm()
# print(obj.pin_verfication())



# Qn) Create a User class with private password.
class User:
    def __init__(self):
        self.__password = 'bibek'

    def getter_password(self):
        return f"your Password:{self.__password}"

# obj = User()
# print(obj.getter_password())

# Qn) Create an employee salary class with controlled salary modification.
class Empolyee:
    def __init__(self,salary):
        self.salary = salary


# obj = Empolyee(20000)
# obj.salary = 10000
# print(obj.salary)




# Q21. Largest Number
# Create a class that stores a list of numbers in a private attribute and provides a method to find the largest number.
class LargestNumber:
    def __init__(self,listnumber):
        self.__list_holder = listnumber


    def largest_numner_finder_method(self):
        largest_number = max(self.__list_holder)
        return largest_number

# obj = LargestNumber([12,33,44,55,565,66,77,777])
# print(obj.largest_numner_finder_method())



# Q25. Even & Odd Counter
# Create a class that privately stores numbers and provides methods to count:
# - Even numbers
# - Odd numbers

class counter:
    def __init__(self,other):
        self.__other = other
        self.__even_counter = 0
        self.__odd_count = 0
        
    def counter_method(self):
        for num in self.__other:
            if num % 2==0:
                self.__even_counter +=1
            else:
                self.__odd_count +=1
        return f"total even counter:{self.__even_counter}\nTotal odd counter:{self.__odd_count}"

# obj = counter([2,3,4,5,6,66,7,77,8,88,9,99,10,100])
# print(obj.counter_method())
    

#=================================================================================================================
# Q1 — Vehicle → Car, Bike, Truck
# Architecture
#                  Vehicle
#               /     |      \
#             Car    Bike    Truck
# Parent: Vehicle
# Common attributes
# vehicle_name
# fuel_type
# fuel_consumed
# distance
# Common methods
# display_info()
# fuel_cost()



# Children
# Car
# own fuel-cost calculation

# Bike
# own fuel-cost calculation

# Truck
# own fuel-cost calculation
# Inheritance concept
# Inheritance
# +
# Method Overriding
# Your task: Parent has fuel_cost(), but every child overrides it.
    


class Vehicle:
    def __init__(self,vehicle_name,fule_type,fule_consumed,distance):
        self.vehicle = vehicle_name
        self.fule_type =  fule_type
        self.fule_consumed = fule_consumed
        self.distance = distance

    def display_info(self):
        return f"vehicle Name:{self.vehicle}\nFule Type:{self.fule_type}\nFule consumed:{self.fule_consumed}\nDistance:{self.distance}"
    def fule_cost(self):
        pass
    
class Car(Vehicle):
    # def __init__(self):
    #     pass
    def Car_Fule_calcuation(self):
        Car_result = self.fule_consumed / self.distance
        return(f"{self.fule_consumed} % {self.distance} = {Car_result}km/L")
    
    
class Bike(Car):
    # def __init__(self):
    #     pass

    def Bike_fule_calcuation(self):
        Bike_result = self.fule_consumed / self.distance
        return(f"{self.fule_consumed} % {self.distance} = {Bike_result}km/L")

class Truck(Bike):
    # def __init__(self):
    #     pass

    def Truck_Fule_calcuation(self):
        Truck_result = self.fule_consumed / self.distance
        return(f"{self.fule_consumed} % {self.distance} = {Truck_result} km/L")

# Truck_obj = Truck('Bike','petrol',120,10)
# print(Truck_obj.Bike_fule_calcuation())
# print(Truck_obj.display_info())





# 🟢 DAY 1 — ONE CLASS

# Project: Student Management System

# Architecture

# StudentManagementSystem
# │
# ├── Add student
# ├── View students
# ├── Search student
# ├── Update student
# ├── Delete student
# └── Exit

# Your class
# StudentManagementSystem
# The class owns:
# - student data
# - menu
# - operations



# 🟢 DAY 2 — ONE CLASS

# Project: Expense Tracker
# Architecture
# ExpenseTracker
# │
# ├── Add expense
# ├── View expenses
# ├── Delete expense
# ├── Search expense
# ├── Calculate total
# └── Exit
# Example:
# Food        500
# Transport   200
# Internet   1000
# Your class owns
# expenses
# Possible conceptual state:
# ExpenseTracker
#       ↓
# expenses
#       ↓
# [
#    {...},
#    {...},
#    {...}
# ]
# ---






# 🟢 DAY 3 — ONE CLASS

# Project: Bank Account

# This day is extremely important.

# Architecture

# BankAccount

# deposit()
# withdraw()
# check_balance()
# transaction_history()

# Object state

# Account
#    │
#    ├── balance
#    └── transactions

# Example:

# Initial balance
#        ↓
#      5000

# deposit(1000)
#        ↓
#      6000

# withdraw(2000)
#        ↓
#      4000

# The important idea:

# OBJECT STATE
#      ↓
# METHOD
#      ↓
# STATE CHANGES

# Questions

# 1. Where should balance live?
# 2. Who should change balance?
# 3. Should outside code directly modify balance?
# 4. What happens if withdrawal > balance?
# 5. Where should transaction history belong?

# Target

# You should become comfortable with:

# «"Objects have state, and methods control how that state changes."»

# ---




# 🔥 DAY 4 — FIRST TWO-CLASS PROJECT

# Student + Course

# This is the first major jump.

# Architecture

# Student
#    ↕
# Course

# Student

# Responsible for:

# student_id
# name
# email

# Course

# Responsible for:

# course_code
# course_name
# students

# Now something new happens.

# A Course doesn't just store normal data.

# It stores:

# «Student objects.»

# Conceptually:

# student1 = Student(...)
# student2 = Student(...)

# course = Course(...)

# course.add_student(student1)
# course.add_student(student2)

# Now:

# Course
#   │
#   ├── Student object
#   └── Student object

# 🚨 THE FIRST IMPORTANT OOP QUESTION
# Don't think:
# «"How do I write two classes?"»
# Think:
# «"Why should these be two classes?"»
# Answer:
# Because Student and Course represent different entities with different responsibilities.
# ---








# 🔥 DAY 5 — TWO CLASSES
# Customer + Order
# Real-world relationship
# Customer
#     ↓
# creates
#     ↓
# Order

# Customer

# name
# email
# orders

# Order

# order_id
# items
# total
# status

# Example:

# customer1
#      │
#      ├── order1
#      ├── order2
#      └── order3

# Now Customer contains Order objects.

# Workflow

# Create Customer
#       ↓
# Create Order
#       ↓
# Attach Order to Customer
#       ↓
# Customer has orders

# Important question

# Why shouldn't Customer contain all Order logic?

# Because:

# Customer responsibility
#         ≠
# Order responsibility

# Customer manages customer-related information.

# Order manages order-related information.

# This is separation of responsibility.

# ---

# 🔥 DAY 6 — TWO CLASSES

# Bank + Account

# This is where you learn:

# «One object can manage MANY other objects.»

# Architecture

# Bank
#  │
#  ├── Account
#  ├── Account
#  └── Account

# Account handles

# balance
# deposit()
# withdraw()

# Bank handles

# accounts
# create_account()
# find_account()

# Example:

# bank
#  │
#  ├── account1
#  ├── account2
#  └── account3

# This is different from Day 5.

# Day 5:

# Customer → Orders

# Day 6:

# Bank → Many Accounts

# Key concept

# ONE OBJECT
#      ↓
# MANAGES
#      ↓
# MANY OBJECTS

# Questions

# 1. Who creates Account?
# 2. Where are Accounts stored?
# 3. Who searches for Account?
# 4. Who performs deposit?
# 5. Should Bank directly change Account.balance?
# 6. What responsibility belongs to Account?

# ---

# 🔥 DAY 7 — THREE CLASSES

# Library Management System

# Now introduce a coordinator/manager class.

# Architecture

#              Library
#             /       \
#          Book      Member

# Book

# Responsible for:

# book_id
# title
# author
# availability

# Member

# Responsible for:

# member_id
# name
# borrowed_books

# Library

# Responsible for:

# books
# members
# borrow_book()
# return_book()
# search_book()
# register_member()

# Workflow

# Create Book
#      ↓
# Library stores Book

# Create Member
#      ↓
# Library stores Member

# Member wants Book
#      ↓
# Library coordinates
#      ↓
# Book + Member relationship

# Very important

# 3 classes does NOT mean:

# Program 1
# Program 2
# Program 3

# It means:

#              ONE SYSTEM
#                  │
#        ┌─────────┼─────────┐
#        ↓         ↓         ↓
#      Book     Member    Library

# The classes collaborate.
# ---




# 🔥 DAY 8 — THREE CLASSES

# Restaurant Management System

# Architecture

# Restaurant
#     │
#     ├── Customer
#     │
#     └── Order

# You can initially represent menu items using dictionaries instead of creating a fourth Food/Product class.

# Example:

# Restaurant
# │
# ├── customers
# ├── orders
# └── menu

# Customer

# customer_id
# name
# orders

# Order

# order_id
# items
# total
# status

# Restaurant

# customers
# orders
# menu

# register_customer()
# create_order()
# find_customer()
# find_order()

# Workflow

# Customer
#    ↓
# places order
#    ↓
# Order
#    ↓
# selects menu items
#    ↓
# calculate total

# New challenge

# You now have:

# Object A
#    ↓
# Object B
#    ↓
# Object C/data

# Your job is to understand the workflow rather than memorizing syntax.

# ---

# 🔥 DAY 9 — FOUR CLASSES

# Mini E-Commerce System

# Now introduce four separate responsibilities.

# Architecture

#               Store
#           /     |      \
#          ↓      ↓       ↓
#     Customer  Product  Order

# Product

# product_id
# name
# price
# stock

# Methods:

# increase_stock()
# decrease_stock()

# Customer

# customer_id
# name
# email
# orders

# Order

# order_id
# customer
# products
# total
# status

# Store

# products
# customers
# orders

# Methods:

# add_product()
# register_customer()
# create_order()
# find_product()
# find_customer()

# Complete workflow

# Store
#   ↓
# Customer
#   ↓
# creates Order
#   ↓
# Order
#   ↓
# contains Product objects
#   ↓
# Product stock changes

# Now you are beginning to think in terms of:

# «System architecture rather than individual classes.»

# ---

# 🔴 DAY 10 — FINAL PROJECT

# Bank Management System

# This is your final architecture challenge.

# Recommended classes

# Bank
#  │
#  ├── Customer
#  │      │
#  │      └── Account
#  │              │
#  │              └── Transaction
#  │
#  └── Customer
#         │
#         └── Account
#                 │
#                 └── Transaction

# You can implement the relationships in different ways depending on your design.

# ---

# CLASS RESPONSIBILITIES

# Customer

# Owns:

# customer_id
# name
# email
# phone
# accounts

# Responsible for customer information.

# ---

# Account

# Owns:

# account_number
# balance
# account_type
# transactions

# Responsible for:

# deposit()
# withdraw()
# transfer()
# get_balance()

# ---

# Transaction

# Owns:

# transaction_id
# transaction_type
# amount
# date
# description

# Responsible for representing a transaction record.

# ---

# Bank

# Owns/manages:

# customers
# accounts

# Responsible for:

# register_customer()
# create_account()
# find_customer()
# find_account()

# ---

# COMPLETE SYSTEM WORKFLOW

#              BANK
#               │
#               ↓
#        Register Customer
#               │
#               ↓
#           CUSTOMER
#               │
#               ↓
#         Create Account
#               │
#               ↓
#           ACCOUNT
#               │
#        ┌──────┼──────┐
#        ↓      ↓      ↓
#     Deposit Withdraw Transfer
#        │      │      │
#        └──────┼──────┘
#               ↓
#         TRANSACTION
#               │
#               ↓
#        Transaction History

# ---

# REQUIRED FEATURES

# Your final project should include:

# 1. Register customer
# 2. Login
# 3. Create account
# 4. View account
# 5. Deposit
# 6. Withdraw
# 7. Transfer
# 8. Check balance
# 9. Transaction history
# 10. Search customer
# 11. Search account
# 12. Update customer
# 13. Logout
# 14. Exit

# ---

# OOP REQUIREMENTS

# Use:

# ✓ Classes
# ✓ Objects
# ✓ __init__
# ✓ Instance attributes
# ✓ Methods
# ✓ Encapsulation
# ✓ Multiple objects
# ✓ Object-to-object communication
# ✓ Composition
# ✓ Lists
# ✓ Dictionaries
# ✓ Exception handling
# ✓ File handling
# ✓ CLI







# Q2 — Employee → Manager, Developer, Intern
#                  Employee
#               /     |       \
#          Manager  Developer  Intern
# Parent: Employee
# Attributes:
# name
# employee_id
# base_salary
# Methods:
# display_info()
# calculate_salary()
# Children
# Manager
# bonus
# manager salary calculation
# Developer
# project_bonus / overtime
# developer salary calculation
# Intern
# stipend
# intern salary calculation
# Practice
# Parent method
#       ↓
# Same method name
#       ↓
# Different calculation
#       ↓
# Method overriding




# Q3 — BankAccount → SavingsAccount, CurrentAccount
#                  BankAccount
#                     /    \
#                    /      \
#              Savings     Current
# Parent
# Attributes:
# account_number
# holder_name
# balance
# Methods:
# deposit()
# withdraw()
# display_balance()
# SavingsAccount
# Special rules:
# minimum balance
# withdrawal limit
# Override:
# withdraw()
# CurrentAccount
# Special rules:
# overdraft / different withdrawal rule
# Override:
# withdraw()
# Important thinking
# Ask:
# Why shouldn't BankAccount.withdraw() have every possible rule?
# Because the withdrawal behavior changes according to account type.





# Q4 — Person → Student → CollegeStudent
# This one is different.
# Architecture
# Person
#    ↓
# Student
#    ↓
# CollegeStudent
# This is multilevel inheritance.
# Person
# Attributes:
# name
# age
# Method:
# display_person()
# Student
# Inherited:
# name
# age
# Adds:
# roll_no
# course
# Method:
# display_student()
# CollegeStudent
# Inherited:
# Person features
# Student features
# Adds:
# college_name
# semester
# Method:
# display_college_student()
# Main concept
# CollegeStudent
#        ↓
# Student
#        ↓
# Person
# The child indirectly receives features from the grandparent.




# Q5 — Shape → Rectangle, Circle, Triangle
#                   Shape
#                /    |     \
#        Rectangle   Circle  Triangle
# Parent
# Method:
# area()
# You don't need to make the parent calculate a specific shape's area.
# Rectangle
# Attributes:
# length
# width
# Override:
# area()
# Circle
# Attribute:
# radius
# Override:
# area()
# Triangle
# Attributes:
# base
# height
# Override:
# area()
# Main concept
# This is a classic:
# Same method
#       ↓
# Different implementation
#       ↓
# Polymorphism
# You should eventually be able to do:
# shape.area()
# and let the actual object decide which calculation happens.




# Q6 — Payment → CreditCard, UPI, CashPayment
#                   Payment
#                 /    |      \
#        CreditCard   UPI   CashPayment
# Parent
# Attributes:
# amount
# Method:
# process_payment()
# CreditCard
# Additional:
# card_number
# Own:
# payment processing
# UPI
# Additional:
# upi_id
# Own:
# payment processing
# CashPayment
# Additional:
# cash_received
# Own:
# payment processing
# Main concept
# Payment
#    ↓
# process_payment()
#    ↓
# different child behavior
# Don't create three completely unrelated payment systems.
# The common concept is payment, while the implementation differs.



#11Qn) Create a University Management System:
# Person
#  ├── Student
#  │    ├── Undergraduate
#  │    └── Postgraduate
#  └── Teacher
#       ├── Professor
#       └── Lecturer
# Each class must have different information and behavior.


#12Qn) Create an Online Shopping System:
# Product
#  ├── Electronics
#  ├── Clothing
#  └── Grocery
# Requirements:
# Different tax
# Different discount
# Different delivery charge
# Final bill calculation
# Product validation

#12Qn) Create a Hospital Management System:
# Person
#  ├── Patient
#  ├── Doctor
#  └── Nurse

# Add:
# Patient admission
# Doctor assignment
# Treatment cost
# Medicine cost
# Final hospital bill


#14Qn) Create a Hotel Management System:
# Room
#  ├── StandardRoom
#  ├── DeluxeRoom
#  └── LuxuryRoom
# Calculate booking cost based on:
# Number of nights
# Room type
# Extra services
# Discount
# Tax




#20Qn) 🔥 Final Challenge — E-Commerce System

# Design:
# User
#  ├── Customer
#  └── Admin

# Product
#  ├── Electronics
#  ├── Clothing
#  └── Grocery

# Order
#  ├── OnlineOrder
#  └── StorePickupOrder

# Payment
#  ├── CardPayment
#  ├── CashPayment
#  └── DigitalPayment

# Your program must support:

# User registration/login
# Product management
# Add/remove product
# Shopping cart
# Category-specific discount
# Tax
# Multiple payment methods
# Order creation
# Order cancellation
# Order history
# Admin product management
# Final invoice

