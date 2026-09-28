

# content = """REAL-WORLD PYTHON OOP PROJECTS
# Special Methods: __init__, __str__, __add__, __sub__, __mul__, __truediv__

# LEVEL: INTERMEDIATE → ADVANCED
# NO SOLUTIONS / NO HINTS

# ============================================================
# PROJECT 1 — SHOPPING CART & PRODUCT SYSTEM
# ============================================================

# Real-world use: Online store / e-commerce.

# Create:
#     class Product:

# Properties:
#     product_id
#     name
#     price
#     quantity

# Requirements:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# class ShopingCard:

#     def __init__(self,product_id,name,price,quantity):
#         self.product_id = product_id
#         self.name = name
#         self.price = price
#         self.quanlity = quantity

#     def __str__(self):
#         return ''''
#         (+)→ combine shopping values/bills
#         (-) → deduct amount/discount
#         (*) → price * quantity
#         (/) → split/average amount
#         '''
#     def __add__(self,other):
#         product_id_result = f'products_Id:[{self.product_id},{other.product_id}]'
#         name_result = f"products_names:['{self.name}','{other.name}']"
#         price_result = self.price + other.price
#         price_result1 = f"total:{price_result}"
#         divide_result = (self.price + other.price) / (self.quanlity + other.price)
#         return f"{product_id_result}\n{name_result}\n{price_result1}\navg of price and quantity:{divide_result}"


#     def __sub__(self,other):
#         discount = self.price + other.price
#         user_discount = int(input('how much you want discount and limit at 5% out of 100:'))
#         final_discount = (user_discount * discount) / 100
#         return f"final discout:{final_discount}"
    
#     def __mul__(self,other):
#         total_price = self.price + other.price
#         total_quantity = self.quanlity + other.quanlity
#         final_result = total_price * total_quantity
#         return f"final_result:{final_result}"
    

#         pass
#     def __truediv__(self, other):
#         divide_result = (self.price + other.price) / (self.quanlity + other.price)
#         return f"avg of price and quantity:{divide_result}"

# obj = ShopingCard(123,'mouse',123,23)
# obj1 = ShopingCard(123,'laptop',123,23)
# print(obj1)
# print(obj + obj1)
# print(obj - obj1)
# print(obj * obj1)
# print(obj / obj1)
# Example objects:
#     laptop = Product(101, "Laptop", 120000, 2)
#     mouse = Product(102, "Mouse", 1500, 3)
# Requirements:
#     __mul__  → price × quantity
#     __add__  → combine shopping values/bills
#     __sub__  → deduct amount/discount
#     __truediv__ → split/average amount
#     __str__ → readable product information
# Make the output look like a real shopping/invoice system.




# ============================================================
# PROJECT 2 — RESTAURANT BILLING SYSTEM
# ============================================================

# Create:
#     class FoodItem:

# Properties:
#     item_id
#     name
#     price
#     quantity



# Example:
#     burger = FoodItem(1, "Burger", 250, 2)
#     pizza = FoodItem(2, "Pizza", 500, 1)

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__
# Real-world meanings:
#     __mul__      → price × quantity
#     __add__      → combine food bills
#     __sub__      → discount
#     __truediv__  → split bill between people

# Target output idea:
#     Burger x 2 = 500
#     Pizza x 1 = 500
#     Total = 1000












# ============================================================
# PROJECT 3 — ELECTRICITY BILL CALCULATOR
# ============================================================

# Create:
#     class ElectricityBill:

# Properties:
#     customer_name
#     previous_unit
#     current_unit
#     rate

# Calculate:
#     units_used
#     total_bill

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __sub__      → current reading - previous reading
#     __mul__      → units × rate
#     __add__      → combine bills
#     __truediv__  → average monthly bill

# Example:
#     meter = ElectricityBill("Ram", 1200, 1350, 12)


# ============================================================
# PROJECT 4 — HOTEL BOOKING & ROOM BILLING
# ============================================================

# Create:
#     class Room:

# Properties:
#     room_number
#     room_type
#     price_per_day
#     days

# Example:
#     room = Room(101, "Deluxe", 5000, 4)

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __mul__      → price × days
#     __add__      → multiple room bills
#     __sub__      → discount
#     __truediv__  → split bill between guests
#     __str__      → room/bill information

# Target output:
#     Room: 101
#     Type: Deluxe
#     Price: 5000
#     Days: 4
#     Total: 20000





# ============================================================
# PROJECT 4 — BANK ACCOUNT & MONEY
# ============================================================

# Create:
#     class Money:
#     class BankAccount:

# Money properties:
#     amount
#     currency

# BankAccount properties:
#     account_number
#     account_holder
#     balance

# Operations:
#     deposit
#     withdraw

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __add__      → salary + bonus
#     __sub__      → balance - expense
#     __mul__      → amount × percentage
#     __truediv__  → split money / monthly amount

# Example:
#     salary = Money(50000, "NPR")
#     expense = Money(12000, "NPR")




# Level 3 — Encapsulation

# Create a bank account where balance cannot be directly modified.
# Create a password-protected User class.
# Create an Employee class with private salary.
# Create a Product class where price cannot be negative.
# Create a Wallet class that prevents overspending.
# Create a Student class where marks must be 0–100.
# Create a Vehicle class with controlled speed.
# Create an ATM class with PIN verification.
# Create a LoanAccount with controlled loan amount.
# Create a DigitalWallet with transaction validation.




# ============================================================
# PROJECT 5 — SALARY & EMPLOYEE SYSTEM
# ============================================================

# Create:
#     class Salary:
#     class Employee:

# Salary properties:
#     basic_salary
#     bonus
#     tax
#     deduction

# Employee properties:
#     employee_id
#     name
#     position
#     salary

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __add__      → salary + bonus
#     __sub__      → salary - tax/deduction
#     __mul__      → salary × percentage
#     __truediv__  → annual salary / 12

# Calculate:
#     gross salary
#     tax
#     deductions
#     net salary
#     monthly salary



# ============================================================
# PROJECT 7 — FUEL & VEHICLE EXPENSE SYSTEM
# ============================================================

# Create:
#     class Fuel:
#     class Vehicle:

# Fuel properties:
#     liters
#     price_per_liter

# Vehicle properties:
#     vehicle_number
#     brand
#     fuel
#     distance

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __mul__      → liters × price
#     __add__      → add fuel expenses
#     __sub__      → remaining fuel
#     __truediv__  → cost per kilometer

# Calculate:
#     total fuel cost
#     fuel efficiency
#     cost per km






# ============================================================
# PROJECT 8 — STUDENT MARKS & GPA SYSTEM
# ============================================================

# Create:
#     class Marks:
#     class Student:

# Marks properties:
#     subject
#     marks
#     credit

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __add__      → total marks
#     __sub__      → marks deduction
#     __mul__      → marks × credit
#     __truediv__  → average

# Calculate:
#     total
#     average
#     weighted marks
#     GPA

# Example:
#     math = Marks("Math", 80, 3)
#     python = Marks("Python", 90, 4)
#     database = Marks("Database", 75, 3)


# ============================================================
# PROJECT 9 — E-COMMERCE INVOICE SYSTEM
# ============================================================

# Create:
#     Product
#     Cart
#     Invoice
#     Customer

# Architecture:
#     Customer
#         ↓
#     Cart
#         ↓
#     Product
#         ↓
#     Invoice

# Use all:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Meaning:
#     Product.__mul__     → price × quantity
#     Cart.__add__        → combine cart/bill
#     Invoice.__sub__     → discount
#     Invoice.__truediv__ → split payment
#     __str__             → readable output

# Final invoice should contain:
#     customer
#     products
#     quantity
#     subtotal
#     discount
#     final total
#     split amount


# ============================================================
# PROJECT 10 — COMPLETE HOTEL MANAGEMENT SYSTEM
# ============================================================

# ADVANCED PROJECT

# Create:
#     Hotel
#     Room
#     Customer
#     Booking
#     Bill
#     Payment

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Features:
#     1. Add room
#     2. Remove room
#     3. Register customer
#     4. Search room
#     5. Book room
#     6. Cancel booking
#     7. Calculate room bill
#     8. Add food bill
#     9. Apply discount
#     10. Calculate tax
#     11. Split bill
#     12. Generate final invoice

# Example concept:
#     room_bill = RoomBill(5000, 4)
#     food_bill = FoodBill(2500)

#     total_bill = room_bill + food_bill
#     discounted_bill = total_bill - 1000
#     per_person = discounted_bill / 3

#     print(per_person)


# ============================================================
# DUnder METHODS TO LEARN
# ============================================================

# __init__       → create/setup object
# __str__        → control print(object)
# __add__        → object + object
# __sub__        → object - object
# __mul__        → object * object
# __truediv__    → object / object

# IMPORTANT:
# Do not force an operator into a project without a meaningful
# real-world purpose.


# ============================================================
# RECOMMENDED ORDER
# ============================================================

# 1. Shopping Cart
# 2. Bank Account
# 3. Restaurant Billing
# 4. Electricity Bill
# 5. Salary & Employee
# 6. Hotel Booking
# 7. Fuel & Vehicle
# 8. Student Marks & GPA
# 9. E-Commerce Invoice
# 10. Complete Hotel Management System


# RULE:
# Build each project yourself.
# Do not look for the solution.
# Send your code when you get stuck, and debug it step by step.
# """

# path = Path("/mnt/data/real_world_oop_projects.txt")
# path.write_text(content, encoding="utf-8")
# print(f"Created: {path}")



# 🧠 Part 1 — 60 CLI-Based OOP Questions
# Level 1 — OOP Foundation
# Create a Student class with name, age, and faculty.
# class student:
#     name = 'bibek'
#     age = 12
#     facuilt = 'engineering'

#     def __init__(self):
#         print(id(self))
#         print('mai to execute hogaya')

# student_obj = student()
# print(student_obj)
# print(student_obj.name)
# print(id(student_obj))

        


# Create a BankAccount class with deposit and withdraw methods.
# Create a Rectangle class that calculates area and perimeter.
# Area = length × width


# class Rectangle:

#     def __init__(self,hight,width):
#         self.hight = hight
#         self.width = width
#         self.rectangle()
    

#     def rectangle(self):
#         area = self.hight * self.width
#         return area


# Rectangle_obj = Rectangle(20,30)
# print(Rectangle_obj)


# Area = length × width

# class Rectangle:

#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def rectangle(self):
#         area = self.height * self.width
#         return area


# Rectangle_obj = Rectangle(20, 30)

# print(Rectangle_obj.rectangle())



# class Rectangle:

#     def __init__(self):
#         print('Welcome to calc')
#         self.rectangle_class()


#     def rectangle_class(self):
#         user_input_hight = int(input('Enter a hight:'))
#         user_input_width = int(input('Enter a width:'))

#         area = user_input_hight * user_input_width
#         print(f'total area:{area}')

# Rectangle_obj = Rectangle()
# print(Rectangle)


# Create a Car class with start/stop methods.
# class Car:
#     def start(self):
#         print('mai chalgaaya')

#     def stop(self):
#         print('mai second wala hu')


# car_obj = Car()
# print(car_obj.start())
# print(car_obj.stop())


# Create an Employee class and calculate annual salary.
# class Empolyee:

#     def __init__(self):
#         self.calcuate_salary()

#     def calcuate_salary(self):
#         user_input = input('Enter a monthely salary:')
#         total = user_input * 12
#         print(f'anaual salary:{total}')

# Create a User class with login/logout methods.
# class LoginSystem:

#     def __init__(self):
#         self.login()



#     def lodin(self):
#         user_input_name = input('Enter a username:')
#         user_input_password = input('Enter a password:')

#         if user_input_name == 'bibek12':
#             if user_input_password == '1234':
#                 print('login sucesfully')
#             else:
#                 print('Envalid password')

#         else:
#             print('invalid usename')

# LoginSystem_obj = LoginSystem()
# print(LoginSystem_obj)

# Create a Temperature class for Celsius/Fahrenheit conversion.
# class Temperature:
#     def __init__(self):
#         self.fahrnheit_to_celcious()
#     def __str__(self):
#         print('str write because if i print print obj show memory address')

#     def fahrnheit_to_celcious(self):
#         fahrnheit_input = int(input('Enter a fahrnheit:'))
#         fahrnheit_to_celcious_result = (fahrnheit_input - 32) * 5 /9
#         print('celcious:',fahrnheit_to_celcious_result)

# obj = Temperature()
# print(obj)


# class Temperature:

#     def __init__(self,celcious):
#         self.celcious = celcious

#     def __str__(self):
#         result = (self.celcious - 32) * 5 /9
#         return f"converted in celcious:{result}"

# obj = Temperature(20)
# print(obj)

# What problem does OOP solve that procedural programming struggles with?
#=> direct i can not one functon to another calling varialbe of function 

# What is the difference between a class and an object?
# Create a Student class with attributes and methods.







# // LEVEL 6 — Dunder Methods | Q83–90
# // Implement __str__() for Student.
# // Implement __repr__() for Product.
# // Implement __add__() for custom numbers.
# // Implement __sub__() for custom numbers.
# // Implement __mul__() for custom numbers.
# // Implement __truediv__() for custom numbers.
# // Implement __eq__() to compare two objects.
# // Implement __lt__() / __gt__() to compare objects.



# content = """REAL-WORLD PYTHON OOP PROJECTS
# Special Methods: __init__, __str__, __add__, __sub__, __mul__, __truediv__

# LEVEL: INTERMEDIATE → ADVANCED
# NO SOLUTIONS / NO HINTS

# ============================================================
# PROJECT 1 — SHOPPING CART & PRODUCT SYSTEM
# ============================================================

# Real-world use: Online store / e-commerce.

# Create:
#     class Product:

# Properties:
#     product_id
#     name
#     price
#     quantity

# Requirements:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# class ShopingCard:

#     def __init__(self,product_id,name,price,quantity):
#         self.product_id = product_id
#         self.name = name
#         self.price = price
#         self.quanlity = quantity

#     def __str__(self):
#         return ''''
#         (+)→ combine shopping values/bills
#         (-) → deduct amount/discount
#         (*) → price * quantity
#         (/) → split/average amount
#         '''
#     def __add__(self,other):
#         product_id_result = f'products_Id:[{self.product_id},{other.product_id}]'
#         name_result = f"products_names:['{self.name}','{other.name}']"
#         price_result = self.price + other.price
#         price_result1 = f"total:{price_result}"
#         divide_result = (self.price + other.price) / (self.quanlity + other.price)
#         return f"{product_id_result}\n{name_result}\n{price_result1}\navg of price and quantity:{divide_result}"


#     def __sub__(self,other):
#         discount = self.price + other.price
#         user_discount = int(input('how much you want discount and limit at 5% out of 100:'))
#         final_discount = (user_discount * discount) / 100
#         return f"final discout:{final_discount}"
    
#     def __mul__(self,other):
#         total_price = self.price + other.price
#         total_quantity = self.quanlity + other.quanlity
#         final_result = total_price * total_quantity
#         return f"final_result:{final_result}"
    

#         pass
#     def __truediv__(self, other):
#         divide_result = (self.price + other.price) / (self.quanlity + other.price)
#         return f"avg of price and quantity:{divide_result}"

# obj = ShopingCard(123,'mouse',123,23)
# obj1 = ShopingCard(123,'laptop',123,23)
# print(obj1)
# print(obj + obj1)
# print(obj - obj1)
# print(obj * obj1)
# print(obj / obj1)
# Example objects:
#     laptop = Product(101, "Laptop", 120000, 2)
#     mouse = Product(102, "Mouse", 1500, 3)
# Requirements:
#     __mul__  → price × quantity
#     __add__  → combine shopping values/bills
#     __sub__  → deduct amount/discount
#     __truediv__ → split/average amount
#     __str__ → readable product information
# Make the output look like a real shopping/invoice system.




# ============================================================
# PROJECT 2 — RESTAURANT BILLING SYSTEM
# ============================================================

# Create:
#     class FoodItem:

# Properties:
#     item_id
#     name
#     price
#     quantity



# Example:
#     burger = FoodItem(1, "Burger", 250, 2)
#     pizza = FoodItem(2, "Pizza", 500, 1)

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__
# Real-world meanings:
#     __mul__      → price × quantity
#     __add__      → combine food bills
#     __sub__      → discount
#     __truediv__  → split bill between people

# Target output idea:
#     Burger x 2 = 500
#     Pizza x 1 = 500
#     Total = 1000












# ============================================================
# PROJECT 3 — ELECTRICITY BILL CALCULATOR
# ============================================================

# Create:
#     class ElectricityBill:

# Properties:
#     customer_name
#     previous_unit
#     current_unit
#     rate

# Calculate:
#     units_used
#     total_bill

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __sub__      → current reading - previous reading
#     __mul__      → units × rate
#     __add__      → combine bills
#     __truediv__  → average monthly bill

# Example:
#     meter = ElectricityBill("Ram", 1200, 1350, 12)


# ============================================================
# PROJECT 4 — HOTEL BOOKING & ROOM BILLING
# ============================================================

# Create:
#     class Room:

# Properties:
#     room_number
#     room_type
#     price_per_day
#     days

# Example:
#     room = Room(101, "Deluxe", 5000, 4)

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __mul__      → price × days
#     __add__      → multiple room bills
#     __sub__      → discount
#     __truediv__  → split bill between guests
#     __str__      → room/bill information

# Target output:
#     Room: 101
#     Type: Deluxe
#     Price: 5000
#     Days: 4
#     Total: 20000





# ============================================================
# PROJECT 4 — BANK ACCOUNT & MONEY
# ============================================================

# Create:
#     class Money:
#     class BankAccount:

# Money properties:
#     amount
#     currency

# BankAccount properties:
#     account_number
#     account_holder
#     balance

# Operations:
#     deposit
#     withdraw

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __add__      → salary + bonus
#     __sub__      → balance - expense
#     __mul__      → amount × percentage
#     __truediv__  → split money / monthly amount

# Example:
#     salary = Money(50000, "NPR")
#     expense = Money(12000, "NPR")




# Level 3 — Encapsulation

# Create a bank account where balance cannot be directly modified.
# Create a password-protected User class.
# Create an Employee class with private salary.
# Create a Product class where price cannot be negative.
# Create a Wallet class that prevents overspending.
# Create a Student class where marks must be 0–100.
# Create a Vehicle class with controlled speed.
# Create an ATM class with PIN verification.
# Create a LoanAccount with controlled loan amount.
# Create a DigitalWallet with transaction validation.




# ============================================================
# PROJECT 5 — SALARY & EMPLOYEE SYSTEM
# ============================================================

# Create:
#     class Salary:
#     class Employee:

# Salary properties:
#     basic_salary
#     bonus
#     tax
#     deduction

# Employee properties:
#     employee_id
#     name
#     position
#     salary

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __add__      → salary + bonus
#     __sub__      → salary - tax/deduction
#     __mul__      → salary × percentage
#     __truediv__  → annual salary / 12

# Calculate:
#     gross salary
#     tax
#     deductions
#     net salary
#     monthly salary



# ============================================================
# PROJECT 7 — FUEL & VEHICLE EXPENSE SYSTEM
# ============================================================

# Create:
#     class Fuel:
#     class Vehicle:

# Fuel properties:
#     liters
#     price_per_liter

# Vehicle properties:
#     vehicle_number
#     brand
#     fuel
#     distance

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __mul__      → liters × price
#     __add__      → add fuel expenses
#     __sub__      → remaining fuel
#     __truediv__  → cost per kilometer

# Calculate:
#     total fuel cost
#     fuel efficiency
#     cost per km






# ============================================================
# PROJECT 8 — STUDENT MARKS & GPA SYSTEM
# ============================================================

# Create:
#     class Marks:
#     class Student:

# Marks properties:
#     subject
#     marks
#     credit

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Real-world meanings:
#     __add__      → total marks
#     __sub__      → marks deduction
#     __mul__      → marks × credit
#     __truediv__  → average

# Calculate:
#     total
#     average
#     weighted marks
#     GPA

# Example:
#     math = Marks("Math", 80, 3)
#     python = Marks("Python", 90, 4)
#     database = Marks("Database", 75, 3)


# ============================================================
# PROJECT 9 — E-COMMERCE INVOICE SYSTEM
# ============================================================

# Create:
#     Product
#     Cart
#     Invoice
#     Customer

# Architecture:
#     Customer
#         ↓
#     Cart
#         ↓
#     Product
#         ↓
#     Invoice

# Use all:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Meaning:
#     Product.__mul__     → price × quantity
#     Cart.__add__        → combine cart/bill
#     Invoice.__sub__     → discount
#     Invoice.__truediv__ → split payment
#     __str__             → readable output

# Final invoice should contain:
#     customer
#     products
#     quantity
#     subtotal
#     discount
#     final total
#     split amount


# ============================================================
# PROJECT 10 — COMPLETE HOTEL MANAGEMENT SYSTEM
# ============================================================

# ADVANCED PROJECT

# Create:
#     Hotel
#     Room
#     Customer
#     Booking
#     Bill
#     Payment

# Use:
#     __init__
#     __str__
#     __add__
#     __sub__
#     __mul__
#     __truediv__

# Features:
#     1. Add room
#     2. Remove room
#     3. Register customer
#     4. Search room
#     5. Book room
#     6. Cancel booking
#     7. Calculate room bill
#     8. Add food bill
#     9. Apply discount
#     10. Calculate tax
#     11. Split bill
#     12. Generate final invoice

# Example concept:
#     room_bill = RoomBill(5000, 4)
#     food_bill = FoodBill(2500)

#     total_bill = room_bill + food_bill
#     discounted_bill = total_bill - 1000
#     per_person = discounted_bill / 3

#     print(per_person)


# ============================================================
# DUnder METHODS TO LEARN
# ============================================================

# __init__       → create/setup object
# __str__        → control print(object)
# __add__        → object + object
# __sub__        → object - object
# __mul__        → object * object
# __truediv__    → object / object

# IMPORTANT:
# Do not force an operator into a project without a meaningful
# real-world purpose.


# ============================================================
# RECOMMENDED ORDER
# ============================================================

# 1. Shopping Cart
# 2. Bank Account
# 3. Restaurant Billing
# 4. Electricity Bill
# 5. Salary & Employee
# 6. Hotel Booking
# 7. Fuel & Vehicle
# 8. Student Marks & GPA
# 9. E-Commerce Invoice
# 10. Complete Hotel Management System


# RULE:
# Build each project yourself.
# Do not look for the solution.
# Send your code when you get stuck, and debug it step by step.
# """

# path = Path("/mnt/data/real_world_oop_projects.txt")
# path.write_text(content, encoding="utf-8")
# print(f"Created: {path}")



# 🧠 Part 1 — 60 CLI-Based OOP Questions
# Level 1 — OOP Foundation
# Create a Student class with name, age, and faculty.
# class student:
#     name = 'bibek'
#     age = 12
#     facuilt = 'engineering'

#     def __init__(self):
#         print(id(self))
#         print('mai to execute hogaya')

# student_obj = student()
# print(student_obj)
# print(student_obj.name)
# print(id(student_obj))

        


# Create a BankAccount class with deposit and withdraw methods.
# Create a Rectangle class that calculates area and perimeter.
# Area = length × width


# class Rectangle:

#     def __init__(self,hight,width):
#         self.hight = hight
#         self.width = width
#         self.rectangle()
    

#     def rectangle(self):
#         area = self.hight * self.width
#         return area


# Rectangle_obj = Rectangle(20,30)
# print(Rectangle_obj)


# Area = length × width

# class Rectangle:

#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def rectangle(self):
#         area = self.height * self.width
#         return area


# Rectangle_obj = Rectangle(20, 30)

# print(Rectangle_obj.rectangle())



# class Rectangle:

#     def __init__(self):
#         print('Welcome to calc')
#         self.rectangle_class()


#     def rectangle_class(self):
#         user_input_hight = int(input('Enter a hight:'))
#         user_input_width = int(input('Enter a width:'))

#         area = user_input_hight * user_input_width
#         print(f'total area:{area}')

# Rectangle_obj = Rectangle()
# print(Rectangle)


# Create a Car class with start/stop methods.
# class Car:
#     def start(self):
#         print('mai chalgaaya')

#     def stop(self):
#         print('mai second wala hu')


# car_obj = Car()
# print(car_obj.start())
# print(car_obj.stop())


# Create an Employee class and calculate annual salary.
# class Empolyee:

#     def __init__(self):
#         self.calcuate_salary()

#     def calcuate_salary(self):
#         user_input = input('Enter a monthely salary:')
#         total = user_input * 12
#         print(f'anaual salary:{total}')

# Create a User class with login/logout methods.
# class LoginSystem:

#     def __init__(self):
#         self.login()



#     def lodin(self):
#         user_input_name = input('Enter a username:')
#         user_input_password = input('Enter a password:')

#         if user_input_name == 'bibek12':
#             if user_input_password == '1234':
#                 print('login sucesfully')
#             else:
#                 print('Envalid password')

#         else:
#             print('invalid usename')

# LoginSystem_obj = LoginSystem()
# print(LoginSystem_obj)

# Create a Temperature class for Celsius/Fahrenheit conversion.
# class Temperature:
#     def __init__(self):
#         self.fahrnheit_to_celcious()
#     def __str__(self):
#         print('str write because if i print print obj show memory address')

#     def fahrnheit_to_celcious(self):
#         fahrnheit_input = int(input('Enter a fahrnheit:'))
#         fahrnheit_to_celcious_result = (fahrnheit_input - 32) * 5 /9
#         print('celcious:',fahrnheit_to_celcious_result)

# obj = Temperature()
# print(obj)


# class Temperature:

#     def __init__(self,celcious):
#         self.celcious = celcious

#     def __str__(self):
#         result = (self.celcious - 32) * 5 /9
#         return f"converted in celcious:{result}"

# obj = Temperature(20)
# print(obj)

# What problem does OOP solve that procedural programming struggles with?
#=> direct i can not one functon to another calling varialbe of function 

# What is the difference between a class and an object?
# Create a Student class with attributes and methods.






































