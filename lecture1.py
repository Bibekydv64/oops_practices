class Atm:

    def __init__(self):

        self.pin = ''
        self.balance = 0
        self.menu()





# print(type(obj))
# print(obj)


    def menu(self):
        user_input = input("""
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to cheak balance
        4. press 4 to withdrow balance
        5. press 5 to exit
         :""")

        
        if user_input == '1':
            #create_pin
            self.create_pin()
        
        elif user_input == '2':
            #change_pin
            self.change_pin()

        elif user_input == '3':
            #cheak_balance
            self.cheak_balance()

        elif user_input == '4':
            #withdrow balance
            self.withdrow_balance()
            


    def create_pin(self):
            user_first_initilize_pin = input('Enter a Pin')
            self.pin = user_first_initilize_pin
            print('Print Created Sucessfully:')
            user_balance = int(input('ENter a balance:'))
            self.balance = user_balance
            self.menu()

    def change_pin(self):
        old_pin = input('Enter a Old  pin:')
        if old_pin == self.pin:
            user_new_pin = input('Enter a new Pin:')
            self.pin = user_new_pin
        else:
            print('chal nikal, Wrong pin, try agin.')
            self.menu()

    def cheak_balance(self):
            current_balance = self.pin
            print(current_balance)
            self.menu()

    def withdrow_balance(self):
            print(self.balance)
            with_drow_balance = int(input('Enter a withdrow Balance'))

            if with_drow_balance < self.balance:
                self.pin = with_drow_balance - self.balance
                print('with drow secessfully')
                self.menu()
            else:
                print('insufficent balannce')
                self.menu()

        

obj = Atm()
print(obj)