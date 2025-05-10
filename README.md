#Instialize lists
students = []
attendance = []

#function for main menu
def main_menu():
    print("\n" + " " * 30 + "IIT Campus")  
    print("\n" + " " * 30 + "Main Menu")
    #display campus name and function name
    
    print("\n1) Enroll a new student")
    print("2) View details of a student")
    print("3) View details of all students according to the branch")
    print("4) Update student details")
    print("5) Mark attendance")
    print("6) View attendance")
    print("7) Exit\n")
    #display 7 options of the main menu for selection


    #Call the functions according to the user's respond
    try:
        choice = int(input("                                                     Your Choice: ")) #Get choice as an input from the user
        if choice == 1:
            enroll_new_student()
        elif choice == 2:
            view_a_detail()
        elif choice == 3:
            view_all_details()
        elif choice == 4:
            update_details()
        elif choice == 5:
            mark_attendance()
        elif choice == 6:
            view_attendance()
        elif choice == 7:
            print("Exiting the program")
            exit()
        else:
            print("Invalid choice")
            main_menu()
    except ValueError:
        print("Invalid input, please enter a number.")
        main_menu() #Back to main menu


#Functions to check whether inputs are under the given conditions
def correct_student_id(student_id):
    return len(student_id) == 9 and student_id.isdigit()
    #To check whether input has 9 characters which are all digits

def correct_nic(nic):
    return len(nic) == 10
    #To check whether input has only 10 characters

def correct_first_name(first_name):
    return len(first_name) <= 10 and first_name.isalpha()
    #To check whether input has less than 11 characters from alphabet

def correct_last_name(last_name):
    return len(last_name) <= 15 and last_name.isalpha()
    #To check whether input has less than 16 characters from alphabet

def correct_bday(bday):
    return len(bday) == 10
    #To check input has 10 characters

def correct_nb(nb):
    return len(nb) == 10 and nb.isdigit()
    #To check whether input has only 10 characters which are only digits

def correct_address(address):
    return len(address) <= 15
    #To check whether input has less than 16 characters

def correct_group(tutor_group):
    return len(tutor_group) == 1
    #To check whether input has only 1 character

def correct_centre(centre):
    allowed_centres = ["Galle", "Colombo", "Kurunagala"]
    return centre in allowed_centres
    #User is allowed to input only one from given centres 


#Function for enrolling students
def enroll_new_student():
    print("\n" + " " * 30 + "IIT Campus")  
    print("\n" + " " * 25 + "Enroll a new student")
    
    student_id = input("\nStudent ID          - ") #Get student id as an input
    while not correct_student_id(student_id):  
        print("Invalid student ID, please enter a correct student ID.")
        student_id = input("Student ID(9-digit number)- ")
        #check if the entered ID meets the required criteria 
        #If the ID is invalid, the user will be prompted to enter it again until a valid input is provided.
        
    nic = input("\nNIC                 - ") #Get nic as an input from the user
    while not correct_nic(nic):
        print("Invalid NIC number, please enter the correct NIC number.")
        nic = input("\nNIC-National Identity Card Number(Text with 10 characters- ")
        #check if the entered NIC meets the required criteria 
        #If the NIC is invalid, the user will be prompted to enter it again until a valid input is provided.
        
    first_name = input("\nFirst Name         - ") #Get first name as an input from the user
    while not correct_first_name(first_name):
        print("Invalid first name, re-enter your first name.")
        first_name = input("Student's First Name- ")
        #check if the entered first name meets the required criteria 
        #If the first Name is invalid, the user will be prompted to enter it again until a valid input is provided.
        
    last_name = input("\nLast Name           - ")#Get last name as an input from the user
    while not correct_last_name(last_name):
        print("Invalid last name, re-enter your last name.")
        last_name = input("Student's Last Name - ")
        #check if the entered last name meets the required criteria 
        #If the last name is invalid, the user will be prompted to enter it again until a valid input is provided.
        
    bday = input("\nBirth Date         - ") #Get birth date as an input from the user
    while not correct_bday(bday):
        print("Invalid format, try again.")
        bday = input("Birth Date (DD/MM/YYYY): ")
        #check if the entered birth date meets the required criteria 
        #If the birth date is invalid, the user will be prompted to enter it again until a valid input is provided.
        
    address = input("\nPermanent Address  - ") #Get permanent address as an input 
    while not correct_address(address):
        print("Invalid address.")
        address = input("Permanent Address(text with 15 characters)- ")
        #check if the entered address meets the required criteria 
        #If the address is invalid, the user will be prompted to enter it again until a valid input is provided.

    nb = input("\nPhone Number       - ") #
    while not correct_nb(nb):
        print("Invalid number, enter the number again.")
        nb = input("Phone Number(10 digits)- ")
        #check if the entered phone number meets the required criteria 
        #If the phone number is invalid, the user will be prompted to enter it again until a valid input is provided.
        
    tutor_group = input("\nTutorial Group      - ").upper()
    while not correct_group(tutor_group):
        print("Invalid group, re-enter.")
        tutor_group = input("Tutorial Group      - ")
        #check if the entered tutorial group meets the required criteria 
        #If the tutorial group is invalid, the user will be prompted to enter it again until a valid input is provided.
        
    centre = input("\nCentre              - ").title()
    while not correct_centre(centre):
        print("Invalid centre. Please enter one of the following: Galle, Colombo, Kurunagala.")
        centre = input("Centre(Galle/Colombo/Kurunagala)- ")
        #check if the entered centre meets the required criteria 
        #If the centre is invalid, the user will be prompted to enter it again until a valid input is provided.
        
    save = input("\n\nDo you want to save the details (Yes/No)? ") #Ask user whether user want to save the details or not
    if save.lower() == "yes":
        student_data = [student_id, nic, first_name, last_name, bday, address, nb, tutor_group, centre]
        students.append(student_data)
        print("\nEnrollment successful.")
        #If user say yes, data will store in the corresponding lists' in corresponding indexes and then display enrollment is successful
    else:
        print("\nEnrollment cancelled.")
        #otherwise data will not save and get clear and display enrollment is cancelled
    
    main_menu()
    #return back to main menu


#Function for view a specific student's details
def view_a_detail():
    print("\n" + " " * 30 + "IIT Campus")  
    print("\n" + " " * 23 + "View Details of a Student")
    #Display campus and function name
    
    student_id = input("\nStudent ID          - ")
    #Get student id as an input from the user
    for student in students: #check whether input student id is in the lists using loop
        if student[0] == student_id:
            print("\nNIC                - "     , student[1])#Print corresponding NIC of the corresponding list where above input student id is located
            print("\nPhone Number       - "     , student[6])#Print corresponding phone number of the corresponding list where above input student id is located
            print("\nFirst Name         - "     , student[2])#Print corresponding first name of the corresponding list where above input student id is located
            print("\nLast Name          - "     , student[3])#Print corresponding last name of the corresponding list where above input student id is located
            print("\nTutorial Group     - "     , student[7])#Print corresponding tutorial group of the corresponding list where above input student id is located
            print("\nCentre             - "     , student[8])#Print corresponding centre of the corresponding list where above input student id is located
            
            another = input("\n\n\nDo you want to view another student's details (Yes/No)? ") #ask user whether user want to view another student's details
            if another.lower() == "yes" :
                view_a_detail()
                #if user says yes, call the function again
            else:
                main_menu()
                #otherwise call the main menu function
            return
    else:
        print("\nStudent ID not found.")
        main_menu()
        #if input student id is not in list, display statement and call back the main menu


#Function to view all students details under the selected branch
def view_all_details():
    print("\n" + " " * 30 + "IIT Campus")  
    print("\n" + " " * 20 + "View Students by Branch")
    #display campus name and function name
    
    if len(students) > 0: #check if the students list is empty or not
        branch_name = input("\nBranch name: ").strip() #get branch name is an input

        branch_students = [student for student in students if student[8].lower() == branch_name.lower()]
        #filter the students details according to the input branch name

        if branch_students: 
            print(f"\nBranch Name: {branch_name}")
            print("{:<12} {:<15} {:<15} {:<15} {:<15}".format(
                "NIC", "Student ID", "First Name", "Last Name", "Tutorial Group"))
            #create the table format and table headers if branch has any student
            print("\n")
            for student in branch_students:
                print("{:<12} {:<15} {:<15} {:<15} {:<15}".format(
                    student[1], student[0], student[2], student[3], student[7]))
                #display filtered student/students details in the suitable format
                print("\n")
        else:
            print(f"\nNo students found in the branch '{branch_name}'.")
            #if no students were found in the input branch display a statement 

        update = input("\nDo you want to update any student's details (Yes/No)? ").strip().lower() #ask whether user want to update any of the student's details
        if update == "yes":
            update_details()
            #if uuser says yes, call the update details function
        else:
            main_menu()
            #otherwise return to the main menu
    else:
        print("\nNo students found.")
        main_menu()
        #if not students were found in the lists, display statement and return back to the main menu


#Function to update students' details
def update_details():
    print("\n" + " " * 30 + "IIT Campus")  
    print("\n" + " " * 23 + "Update Student Details")
    #display campus name and function name
    
    student_id = input("\nStudent ID          - ") #get student id as an input from the user
    for student in students: 
        if student[0] == student_id: #check whether student id is in students' list using for loop
                nic = input("\nNIC                 - ") #get nic as an input from the user
                while not correct_nic(nic):
                    print("Invalid NIC number, please enter the correct NIC number.")
                    nic = input("NIC (10 digits)     - ")
        #check if the entered NIC meets the required criteria 
        #If the NIC is invalid, the user will be prompted to enter it again until a valid input is provided.
                    
                first_name = input("\nFirst Name          - ") #get first name as an input from the user
                while not correct_first_name(first_name):
                    print("Invalid first name, re-enter your first name.")
                    first_name = input("First Name          - ")
        #check if the entered first name meets the required criteria 
        #If the first Name is invalid, the user will be prompted to enter it again until a valid input is provided.
                    
                last_name = input("\nLast Name           - ") #get last name as an input from the user
                while not correct_last_name(last_name):
                    print("Invalid last name, re-enter your last name.")
                    last_name = input("Last Name           - ")
        #check if the entered last name meets the required criteria 
        #If the last name is invalid, the user will be prompted to enter it again until a valid input is provided.
                    
                bday = input("\nBirth Date          - ") #get birth date as an input from the user
                while not correct_bday(bday):
                    print("Invalid format, try again.")
                    bday = input("Birth Date (DD/MM/YYYY)- ")
        #check if the entered birth date meets the required criteria 
        #If the birth date is invalid, the user will be prompted to enter it again until a valid input is provided.
                    
                address = input("\nPermanent Address   - ") #get address as an input from the user
                while not correct_address(address):
                    print("Invalid address.")
                    address = input("Permanent Address   - ")
        #check if the entered address meets the required criteria 
        #If the address is invalid, the user will be prompted to enter it again until a valid input is provided.

                nb = input("\nPhone Number        - ")#get mobile number as an input from the user
                while not correct_nb(nb):
                    print("Invalid number, enter the number again.")
                    nb = input("Phone Number        - ")
        #check if the entered phone number meets the required criteria 
        #If the phone number is invalid, the user will be prompted to enter it again until a valid input is provided.

                choice = input("\n\nDo you want to save the updates (Yes/No)? ") #ask user whether user want to save those updated details
                if choice.lower() == "yes":
                            student[1] = nic
                            student[2] = first_name
                            student[3] = last_name
                            student[4] = bday
                            student[5] = address
                            student[6] = nb
                            print("Details updated successfully.")
                            main_menu()
                            return
                        #if user says yes, replace updated details with previous details in corresponding indexes
                        #after replacement display a statement and return to main menu
                else:
                            print("Update cancelled.")
                            main_menu()
                            return
                        #if user says no, display a statement and return back to main menu
        else:
            print("Student ID not found.")
            main_menu()
            #if input student id were not found in the list, display statement and return to the main menu


#functions to check whether data input for the user in update details function are valid  
def correct_student_id(student_id):
    return len(student_id) == 9 and student_id.isdigit()
#function to check whether the input student id meets suitable conditions (9 digits number)

def correct_nic(nic):
    return len(nic) == 10
#function to check whether the input nic meets suitable conditions (10 digits number)

def correct_first_name(first_name):
    return len(first_name) <= 10 and first_name.isalpha()
#function to check whether the input first name meets suitable conditions (text with less than 11 characteristics)

def correct_last_name(last_name):
    return len(last_name) <= 15 and last_name.isalpha()
#function to check whether the input last name meets suitable conditions (text with less than 16 characteristics)

def correct_bday(bday):
    return len(bday) == 10
#function to check whether the input birth date meets suitable conditions (string with 10 characters)

def correct_nb(nb):
    return len(nb) == 10 and nb.isdigit()
#function to check whether the input mobile number meets suitable conditions (10 digit number)

def correct_address(address):
    return len(address) <= 15
#function to check whether the input address meets suitable conditions (text with less than 16 characters)

def correct_group(tutor_group):
    return len(tutor_group) == 1
#function to check whether the input tutorial group meets suitable conditions (only one character)

def correct_centre(centre):
    allowed_centres = ["Galle", "Colombo", "Kurunagala"]
    return centre in allowed_centres
#function to check whether the input centre meets suitable conditions (only one from "Galle" , "Colombo" , "Kurunagala")

def mark_attendance():
    print("                             IIT Campus                                    ")
    print("                          Mark Attendance                                  ")
    # display campus name and function name

    centre = input("\nCentre              -   ")  # get centre as an input from the user
    while not correct_centre(centre):
        print("Invalid centre. Please enter one of the following: Galle, Colombo, Kurunagala.")
        centre = input("Centre              - ")
        # check if the entered centre meets the required criteria
        # If the centre is invalid, the user will be prompted to enter it again until valid

    tutor_group = input("\nTutorial Group      -   ")  # get tutorial group as an input from the user
    attendance_date = input("\nDate                -   ")  # get attendance date from user as an input

    filtered_students = [student for student in students if student[7] == tutor_group and student[8] == centre]
    # filter and get the students who are under the certain tutorial and centre

    if not filtered_students:
        print("No students found for the selected branch and tutorial group.")
        main_menu()
        return
    # if no student found on the selected branch and tutorial group, display a statement and return to main menu

    attendance_records = []  # create a list to store attendance records temporarily
    print("\nStudent ID    Present/Absent")

    for student in filtered_students:
        print(f"{student[0]:<15}", end="")
        attendance_status = input(" ").strip().lower()
        # normalize user input to lowercase to handle case insensitivity

        if attendance_status not in ["present", "absent"]:
            print("Invalid input, defaulting to Absent")
            attendance_status = "absent"
            # if user input is not "present" or "absent", default to "absent"

        attendance_records.append([centre, tutor_group, attendance_date, student[0], attendance_status.capitalize()])
        # Append the attendance record for the current student, capitalize the status for consistency

    save = input("\nDo you want to save the details (Yes/No)? ").strip().lower()
    # Prompt the user to confirm saving the attendance details
    if save == "yes":
        attendance.extend(attendance_records)
        print("Attendance saved successfully.")
        # If the user confirms, save the attendance records to the main attendance list

    else:
        print("Attendance not saved.")
        # If the user declines, attendance is not saved

    main_menu()
    # return to the main menu

# Function to view attendance of the students
def view_attendance():
    print("                             IIT Campus                                    ")
    print("                       View Attendance Details                              ")
    # Display campus name and function name

    student_id = input("\nStudent ID     - ")  # Get student ID as an input from the user
    if not correct_student_id(student_id):
        print("Invalid Student ID.")
        main_menu()
        return
    # If input student ID is not in the list, display a statement and return back to main menu

    from_date = input("From           - ")  # Get starting date from the user
    to_date = input("To             - ")  # Get ending date from the user

    print("\nDate              Present/Absent")
    
    # Print headers for the Date and Status columns

    # Iterate through the attendance records
    for record in attendance:  
        if record[3] == student_id:  # Check if the record matches the input Student ID
            # Display each record with Date and Status only
            print(f"{record[2]}        {record[4]}")

    # Ask if the user wants to go back to the main menu
    go_back = input("\nDo you want to direct to the main menu (Yes/No)? ")
    if go_back.lower() == "yes":
        main_menu()
    else:
        print("Thank you for using the attendance system.")

main_menu()
#return to main menu
