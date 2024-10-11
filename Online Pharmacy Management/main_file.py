#
#


# Admin Privilege

def admin_login():
    print("Please insert your username and password to proceed")
    A_username = str(input("Username: "))
    A_password = str(input("Password: "))
    with open("admin.txt", "r") as adminfile:  # Open txt files and read content
        if A_username and A_password in adminfile.read():  # If the username that input by the user is the same as username in txt files then it will proceed
            print("Login successfully!")
            print("====================================================")
            print(" Welcome " + A_username + " to the admin main menu")
            print("====================================================")
            admin_menu()
        else:
            print("Invalid Credential")
            admin_login()


def admin_menu():
    print("""
        [1] Upload Medicine 
        [2] View Medicine 
        [3] Edit Medicine Information 
        [4] Delete Medicine Information 
        [5] Search Specific Medicine 
        [6] View Customer Order 
        [7] Search Customer Order
        [0] Exit 
        """)

    aoption = int(input("Please select options [0-7]: "))
    while aoption < 0 or aoption > 7:  # Loop the question until the user input the correct option
        print("Invalid option")
        aoption = int(input("Please select options [0-7]: "))
    if aoption == 0:
        print("Thank you and have a nice day!")
        main_menu()  # Redirect to main menu
    elif aoption == 1:
        admin_upload_medic()  # add medicine
        pass
        Acontinue_or_no()
    elif aoption == 2:
        view_medic() # View medicine
        pass
        Acontinue_or_no()
    elif aoption == 3:
        view_medic()
        admin_edit_medic() # Edit medicine
        pass
        Acontinue_or_no()
    elif aoption == 4:
        view_medic()
        admin_delete_medic() # Delete medicine
        pass
        Acontinue_or_no()
    elif aoption == 5:
        admin_show_medic_only()
        admin_search_medic() # Search medicine
        pass
        Acontinue_or_no()
    elif aoption == 6:
        admin_view_order() # View order
        pass
        Acontinue_or_no()
    elif aoption == 7:
        admin_show_order_only()
        admin_search_order() # Search orders
        pass
        Acontinue_or_no()


def admin_upload_medic():
    print("============================================")
    print("              Add Medicine                  ")
    print("============================================")
    m_name = str(input("Please input medicine name: "))
    m_edate = str(input("Please input medicine expiry date: "))
    m_price = float(input("Please input medicine price : "))
    m_spec = str(input("Please input medicine specification: "))
    medifile = open("medic.txt", "a")  # open text files and append new data into the text files
    medifile.write(str(m_name) + ";" + str(m_edate) + ";" + str(m_price) + ";" + str(m_spec) + ";" + "\n") # Data is taken and stored into variables then export the data into the textfile
    print("Data added successfully in medic file")
    medifile.close # Close file


def admin_edit_medic():
    list_of_medicine = []
    with open("medic.txt", "r") as medifile:
        for line in medifile.readlines():
            split = line.split(";")
            list_of_medicine.append(split)
    updated_details = []
    data = str(input("Please input details to edit from the list: "))
    edit = str(input("Please input new details to replace: "))
    for medicine in list_of_medicine:
        medicine = [edit if elem == data else elem for elem in medicine]
        updated_details.append(medicine)

    with open('medic.txt', 'w', encoding='utf-8') as new_file:
        for line in updated_details:
            line = ";".join(line)
            new_file.write(line)
    print("Data Updated!")      


def admin_delete_medic():
    medicine = input('Enter the medicine that you want to delete: ')
    with open('medic.txt', 'r') as f:
        medic = f.readlines() # scan the file
    medic_found = [x for x in medic if x.split(';')[0].lower() == medicine.lower()] # Read the line by splitting the ";"
    if medic_found:
        print('Removed medicine: {}'.format(medicine))
        medic.remove(medic_found[0]) # Remove the whole row by scanning the comparing the medicine name that is stored in variables and medicine stored in txt files
        with open('medic.txt', 'w') as f:
            f.write(''.join(medic)) # Write an empty space into the text file
    else:
        print('Sorry! Medicine "{}" not found.'.format(medicine))


def admin_show_medic_only():
    medifile = open("medic.txt", "r")
    for row in medifile:
        data = row.split(";")
        print(data[0])
    medifile.close()    


def admin_search_medic():  
    search = str(input("Please input medicine name: "))
    medifile = open("medic.txt", "r")
    for i in medifile:
        data = i.split(";")
        if search == data[0]:
            print(data)


def admin_view_order():
    print(
        "===================================================================================================================================")
    print(
        "                                                         Customer Order List                                                       ")
    print(
        "===================================================================================================================================")
    print(
        "|     Name     |     Address     |     Email     |     Phone number     |               Ordered Item               |     Price     ")
    print(
        "===================================================================================================================================")
    with open("order.txt", "r") as orderfile: # Open textfile and read every data
        for row in orderfile:
            print(row)


def admin_show_order_only():
    medifile = open("order.txt", "r")
    for row in medifile:
        data = row.split(";")
        print(data[0] , data[1])
    medifile.close()    


def admin_search_order():
    search = str(input("Please input user's unique ID: "))
    medifile = open("order.txt", "r")
    for i in medifile:
        data = i.split(";")
        if search == data[0]:
            print(data)




# Guest Privilege

def guest_menu():
    print("""
            [1] View available medicine in stocks
            [2] Register as member
            
            [0] Exit 
            """)

    aoption = int(input("Please select options [0-4]: "))
    while aoption < 0 or aoption > 2:
        print("Invalid option")
        aoption = int(input("Please select options [0-4]: "))
    if aoption == 0:
        print("Thank you and have a good day!")
        main_menu()
    elif aoption == 1:
        view_medic() # View available medicine
        Gcontinue_or_no()
    elif aoption == 2:
        register() # Register as user
        Gcontinue_or_no()


def register():
    print("====================")
    print("Register as a member")
    print("====================")
    name = str(input("Please insert your name: "))
    address = str(input("Please input your address: "))
    email = str(input("Please input your email ID: "))
    phone_number = str(input("Please input your phone number: "))
    gender = str(input("Please insert your gender (m/f): "))
    userid = str(input("Please input a userid: "))
    password = str(input("Please input your desired password: "))
    re_password = str(input("Confirm password. Please rewrite the password again: "))
    
    if password != re_password:  # Check if the password matched with the password that is re-entered by the user
        print("Password incorrect, Restart again")
        register()
    else:
        if len(password) <= 2:
            print("Password too short. Restart again")  # The length of the password must be more than 2
            register()
        else:
            userinfofile = open("userinfo.txt", "a") # Open text file for append
            userinfofile.write(str(userid) + ";" + str(password) + ";" + str(email) + ";" + str(phone_number) + ";" + str(gender) + ";" + str(name) + ";" + str(address) + ";" + "\n") # Write the data that is stored from variable into text file
            user = open("user.txt", "a") # Open text file for append
            user.write(str(userid) + ";" + str(password) + ";" + "\n") # Input the data from variable into text file
            print("user successfully created!")
            option = int(input("Do you want to proceed to login? [1] -- yes [2] -- no: "))
            if option == 1:
                user.close()
                userinfofile.close()
                user_login()  # Login page for user
            else:
                userinfofile.close()
                guest_menu() # Guest menu page




# User Privilege

def user_login():
    print("Please insert your username and password to proceed")
    U_username = str(input("Username: "))
    U_password = str(input("Password: "))
    with open("user.txt", "r") as userfile: # Open textfiles and read every data of the file
        if U_username and U_password in userfile.read():
            print("Login successfully!")
            print("====================================================")
            print(" Welcome " + U_username + " to the user main menu")
            print("====================================================")
            user_menu()
        else:
            print("Invalid Credential")
            user_login()


def user_menu():
    print("""
        [1] View Medicine 
        [2] Place Order of medicine
        [3] View order
        [4] View Personal information
        [0] Exit 
        """)

    uoption = int(input("Please select options [0-4]: "))
    while uoption < 0 or uoption > 5:
        print("Invalid option")
        uoption = int(input("Please select options [0-4]: "))
    if uoption == 0:
        print("Thank you and have a good day!")
        main_menu()
    elif uoption == 1:
        view_medic() # View medicine
        pass
        Ucontinue_or_no()
    elif uoption == 2:
        view_medic()
        add_customer_order() # Add customer order
        pass
        Ucontinue_or_no()
    elif uoption == 3:
        user_view_order() # View Order
        pass
        Ucontinue_or_no()
    elif uoption == 4:
        user_view_personal() # View personal information
        pass
        Ucontinue_or_no()


def add_customer_order(): 
    print("\n" * 2)
    print("============================================================================")
    print("|                             Place Order                                   ")
    print("============================================================================")
    name = str(input("Please insert your name: "))
    address = str(input("Please input your address: "))
    email = str(input("Please input your email ID: "))
    phone_number =str(input("Please input your phone number: "))
    unique_id = str(input("Please insert your unique ID: "))
    cart = [] # Cart as empty list
    number_item = int(input("Please input number of item that you want to purchase: "))
    for i in range(0, number_item): # Loop number of item to add into the cart
        item = str(input("Please input the medicine name that you wanted to purchase: "))
        cart.append(item) # Add the item into cart's list

    input_price = input("Enter price of the item separated by (,) :  ")
    print("")
    user_price = input_price.split(",")
    for i in range(len(user_price)): # Loop every data in user price
        user_price[i] = float(user_price[i]) # convert each item to float type
    print("You have selected item: ", cart)
    print("Sum = RM", round(sum(user_price), 2))

    payment = float(input("Please make payment: RM"))
    if payment >= float(round(sum(user_price), 2)): # If user made payment more or equal to the total price
        balance = payment - float(round(sum(user_price), 2)) # Calculation of the remaining balance
        balance = round(balance,2)
        print("Order successfully created!")
        print("Your remaining balance: RM" + str(balance))
        userorder = open("order.txt", "a") # Open text file to append data into the text file
        userorder.write(str(unique_id) + ";" + str(name) + ";" + str(address) + ";" + str(email) + ";" + str(phone_number) + ";" + str(cart) + ";" + str(round(sum(user_price), 2))+ ";" + "\n")
    else:
        print("Insufficient amount")
        Ucontinue_or_no()


def user_view_order():
    search = str(input("Please input your unique ID: "))
    ownorder = open("order.txt", "r")
    for i in ownorder:
        data = i.split(";")
        if search == data[0]:
            print(data)  


def user_view_personal():
    search = str(input("Please input your username: "))
    ownorder = open("userinfo.txt", "r")
    for i in ownorder:
        data = i.split(";")
        if search == data[0]:
            print(data)  


def view_medic():
    print("===========================================================================================================")
    print("                                                    Medicine List                                           ")
    print("===========================================================================================================")
    with open("medic.txt", "r") as medifile: # Open text files and read the contents
        for row in medifile: # Scan every data in the text file
            print(row) # Output the data from the text file


def Acontinue_or_no():
    option = int(input("Do you wish to continue? [1]-- Yes  [2]-- No: "))
    if option == 1:
        print("Returning to admin main menu")
        print("")
        admin_menu()
    else:
        print("Returning to main menu")
        print("")
        main_menu()


def Gcontinue_or_no():
    option = int(input("Do you wish to continue? [1]-- Yes  [2]-- No: "))
    if option == 1:
        print("Returning to guest main menu")
        print("")
        guest_menu()
    else:
        print("Returning to main menu")
        print("")
        main_menu()


def Ucontinue_or_no():
    option = int(input("Do you wish to continue? [1]-- Yes  [2]-- No: "))
    if option == 1:
        print("Returning to user main menu")
        print("")
        user_menu()
    else:
        print("Returning to main menu")
        print("")
        main_menu()


def main_menu():
    print("""
        ===============================================
        |Welcome to Online Pharmacy Management System |
        ===============================================          
        |[1] -- Admin                                 |
        |[2] -- User                                  |
        |[3] -- Guest                                 |
        |                                             |
        |[0] -- Exit                                  |
        ===============================================
        """)

    role = int(input("Which role are you?(Please input option 0-3): "))
    while (role < 0) or (role > 3):
        print("Invalid Input")
        role = int(input("Which role are you?(Please input option 0-3): "))
    if role == 1:
        admin_login() # Proceed to admin login page
    elif role == 2:
        user_login() # Proceed to user login page
    elif role == 3:
        guest_menu() # Proceed to guest's menu
    elif role == 0:
        print("Thank you and have a nice day!")
        exit()
    else:
        print("Invalid input")


# Main Program
main_menu()
