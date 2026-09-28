# class Point:

#     def __init__(self,x,y):
#         self.x_cord = x
#         self.y_cord = y

#     def __str__(self):
#         result = f"({self.x_cord},{self.y_cord})"
#         # return "({},{})".format(self.x_cord,self.y_cord)
#         return (result)
#     # @staticmethod
#     # def point1(x,y,z):
#     #     return "{}X{}Y{}Z".format(x,y,z)
    

# Gemotery_obj = Point(2,3)





# class Point:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z


#     def __str__(self):
#         return f"{self.x}X{self.y}Y{self.z}Z"



# point_0bj = Point(2,3,4)
# print(point_0bj)




# class Encapsulation:

#     def __init__(self):
#         self.name = 'bibek'
#         self._brand = 'trader'
#         self.__balance = 12


# Encapsulation_obj = Encapsulation()
# print(Encapsulation_obj.name)
# print(Encapsulation_obj._brand)
# print(Encapsulation_obj._Encapsulation__balance)




# class Person:
#     def __init__(self,name,country):
#         self.__name = name
#         self.__country = country

#     def Greet(self):
#         if self.country == 'india':
#             print(f'Namaste:{self.name}:sir')

#         else:
#             print(f"hello:{self.name}:Sir")


# obj = Person('bibek','nepal')
# print(obj.Greet())

# obj.gender = 'male'
# print(obj.gender)

# Person('nitesh','male')



# user_input = int(input('Enter a Table Number:'))
# table_counter = 0
# while True:
#     if table_counter < 10:
#         table_counter += 1
#         total_number = user_input * table_counter
#         print(f"{user_input} X {table_counter} = {total_number}")   
#     else:
#         break

# user_input = int(input('Enter tohar table number:'))
# for num in range(1,11):
#     new_vars = user_input * num
#     print(f"{user_input} X {num}")

# a = 10
# while True:
#     if  a < 10:
#         pass
#     else:
#         break


# for i in range(0,51,2):
#     print(f"even number{i}")



# age = 10
# if age == 10:
#     print('done')
# else:
#     print('nikal')



# def age(age1):
#     money = 'heheh'
#     if age1 < 20:
#         print('bauwaxa')
#     else:
#         print('bethichod aabhi tu jawan xe:')



# age(10)

# print(money)


# class Custember:
#     def __init__(self,name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address

#     def print_address(self):
#         print(f"Your City:{self.address.city}\nYour Pin:{self.address.pin}\nYour state:{self.address.state}")

# class Addeess:
#     def __init__(self,city,pin,states):
#         self.city = city
#         self.pin = pin
#         self.state = states

# Addeess_obj = Addeess('nepal',4321,'pullchowk')
# Custember_obj = Custember('bibek','male',Addeess_obj)

# print(Custember_obj.print_address())



# class User:
#     def __init__(self):
#         self.name = 'nitesh'
    
#     def Login(self):
#         return 'Login'

# class student(User):

#     def __init__(self):
#         pass
#     def  enroll(self):
#         return "Enroll:"

# negative_counter  = 0

# for i in range(-50,1):
#     negative_counter = i
#     print(f"{negative_counter}. Parash")
    
# counter = 0

# for i in range(50):
#     counter +=1
#     print(i)


# print(counter)






















# odd = 0
# sum_odd = 0

# for num in range(1,31):
#     if num % 2 != 0:
#         odd +=1
#         sum_odd += num
#         print(f"odd number:{num}")

# print(f"Total sum of odd number:{sum_odd}")



















