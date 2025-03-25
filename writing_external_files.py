#-----------------------------
# writing_external_files.py
#Zach Ignacio
# Simple program to write static and user-inputted data to a file
#-----------------------------

def write_initial_data():
    # Opens the file in write mode, creating it if it doesn't exist
    file = open('userdata.txt', 'w')
    print("Creating and writing to file...")
    
    # Static data
    file.write("User Information:\n")
    file.write("----------------\n")
    file.write("Default Health: 100\n")
    file.write("Default Level: 1\n")
    
    file.close()
    print("Initial data written.")

def append_user_data():
    # Opens the file in append mode
    file = open('userdata.txt', 'a')
    
    # User input
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    user_hobby = input("Enter your favorite hobby: ")
    
    file.write(f"Name: {user_name}\n")
    file.write(f"Age: {user_age}\n")
    file.write(f"Hobby: {user_hobby}\n")
    file.write("----------------\n")
    
    file.close()
    print("User data appended.")

def main():
    write_initial_data()
    input("Press Enter to continue...")
    append_user_data()
    print("Process completed. Check 'userdata.txt'.")

#-----------------------Main Code------------------------

main()


