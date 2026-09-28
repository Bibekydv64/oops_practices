
class StudentManagementSystem:
    def __init__(self):
        print('Welcome to the Student Management System')
        # Using a dictionary where StudentID will be the key
        self.database1 = {}
        self.menu()

    def menu(self):
        while True:
            user_menu_input = input('''
============ MENU ============
1. Press 1 to Add Student
2. Press 2 to View Students
3. Press 3 to Search Student
4. Press 4 to Update Student
5. Press 5 to Delete Student
6. Press any other key to Exit
==============================
Enter choice: ''')

            if user_menu_input == '1':
                self.Add_student()
            elif user_menu_input == '2':
                self.view_student()
            elif user_menu_input == '3':
                self.search_student()
            elif user_menu_input == '4':
                self.update_student()
            elif user_menu_input == '5':
                self.delete_student()
            else:
                print('Program exited successfully.')
                break  # Stops the menu loop and exits

    def Add_student(self):
        try:
            count = int(input('How many students do you want to add? '))
            for _ in range(count):
                student_id = input('Enter Student ID: ')
                
                # Check if ID already exists to avoid overwriting
                if student_id in self.database1:
                    print(f"Student with ID {student_id} already exists!")
                    continue
                
                name = input('Enter Student Name: ')
                age = input('Enter Student Age: ')
                marks = input('Enter Student Total Marks: ')

                # Store student data using ID as the primary key
                self.database1[student_id] = {
                    'Name': name,
                    'Age': age,
                    'Marks': marks
                }
                print(f"Student '{name}' added successfully!\n")
        except ValueError:
            print("Invalid input. Please enter numbers where required.")

    def view_student(self):
        if not self.database1:
            print("No student records found.")
            return
        
        print("\n--- Student Records ---")
        for s_id, info in self.database1.items():
            print(f"ID: {s_id} | Name: {info['Name']} | Age: {info['Age']} | Marks: {info['Marks']}")

    def search_student(self):
        s_id = input('Enter Student ID to search: ')
        if s_id in self.database1:
            info = self.database1[s_id]
            print(f"\nStudent Found:\nID: {s_id}\nName: {info['Name']}\nAge: {info['Age']}\nMarks: {info['Marks']}")
        else:
            print("Student ID not found.")

    def update_student(self):
        s_id = input('Enter Student ID to update: ')
        if s_id in self.database1:
            print("Leave blank if you don't want to change the value.")
            name = input(f"Enter new Name ({self.database1[s_id]['Name']}): ")
            age = input(f"Enter new Age ({self.database1[s_id]['Age']}): ")
            marks = input(f"Enter new Marks ({self.database1[s_id]['Marks']}): ")

            # Update only if the user typed something
            if name: self.database1[s_id]['Name'] = name
            if age: self.database1[s_id]['Age'] = age
            if marks: self.database1[s_id]['Marks'] = marks
            print("Student records updated successfully.")
        else:
            print("Student ID not found.")

    def delete_student(self):
        s_id = input('Enter Student ID to delete: ')
        if s_id in self.database1:
            del self.database1[s_id]
            print(f"Student ID {s_id} deleted successfully.")
        else:
            print("Student ID not found.")

# Start the application
StudentManagementSystem_obj = StudentManagementSystem()

















class HotelBookingSystem:

    def __init__(self):
        self.database = {}
        self.room_number_database = []
        self.menu()

    def menu(self):

        while True:

            user_input_chose = input('''
        ===== HOTEL MANAGEMENT SYSTEM =====
        1. Add Room
        2. View Rooms
        3. Book Room
        4. Search Booking
        5. Check-in
        6. Check-out
        7. Cancel Booking
        8. Exit
        ===================================
        Choose a number: ''')

            if user_input_chose == '1':
                self.add_room()

            elif user_input_chose == '2':
                self.view_room()

            elif user_input_chose == '3':
                self.book_room()

            elif user_input_chose == '4':
                self.search_room()

            elif user_input_chose == '5':
                self.checkin_room()

            elif user_input_chose == '6':
                self.checkout_room()

            elif user_input_chose == '7':
                self.cancel_room()

            elif user_input_chose == '8':
                print('Exit successfully')
                break

            else:
                print('Invalid choice!')


    def add_room(self):

        add_room_number = int(input('Enter room number: '))

        if add_room_number not in self.room_number_database:

            self.room_number_database.append(add_room_number)

            print(f'Room {add_room_number} added successfully.')
            print(f'Current rooms: {self.room_number_database}')

        else:
            print(f'Room {add_room_number} already exists in database.')


    def view_room(self):

        print(f'Total rooms available: {self.room_number_database}')


    def book_room(self):
        pass


    def search_room(self):
        pass


    def checkin_room(self):
        pass


    def checkout_room(self):
        pass


    def cancel_room(self):
        pass


HotelBookingSystem_obj = HotelBookingSystem()

