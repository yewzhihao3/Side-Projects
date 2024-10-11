import datetime
date_time = datetime.datetime.now()

def Delay(second):
    import time
    time.sleep(second)

def clear():
    import os
    os.system("cls")


class User:
    def __init__(user, name, pin, acc_number, balance, pnumber, tnumber):
        user.name        = name
        user.pin         = pin
        user.acc_number  = acc_number
        user.balance     = balance
        user.pnumber     = pnumber
        user.tnumber     = tnumber

user1 = User("Jason", int(123456), str(145698723), float(5000.00), str("01113065923"), float(20.87))


class O_Receiver:
    def __init__(o_receiver, name, acc_number, bank_name):
        o_receiver.name        = name
        o_receiver.acc_number  = acc_number
        o_receiver.bank_name   = bank_name

o_receiver1 = O_Receiver("Ali", int(123456789), str("CIMB Bank"))
o_receiver2 = O_Receiver("Bruce Wayne", int(234567891), str("Public Bank"))
o_receiver3 = O_Receiver("Tony Stark", int(567891123), str("Maybank"))
o_receiver4 = O_Receiver("Abu", int(1234567890), str("OCBC Bank"))

class Bill:

    def __init__(bill, tnb, water, unifi, car ):
        bill.tnb       = tnb
        bill.water     = water
        bill.unifi     = unifi
        bill.car       = car

billuser1 = Bill (float(300),float(20),float(200),float(6000))


class Topup:

    def __init__(topup, p1, p2, p3, p4):
        topup.p1 = p1
        topup.p2 = p2
        topup.p3 = p3
        topup.p4 = p4

tuser1 = Topup (float(5), float(10), float(50), float(100))



def Intro():
    print("====================")
    print("Welcome to XYZ Bank")
    print("====================")
    print("Please insert your card")
    Delay(1)
    print("verifying....")
    Delay(1)
    print("verified!")
    print("")
    verify_password()




def TnG():
    clear()
    print("Your phone number: ", user1.pnumber)
    print("Your current balance in TnG is ", user1.tnumber)
    print("Please choose options 0-4")
    print("""
    1 = 10
    2 = 50
    3 = 100
    4 = Others
    0 = exits
    """)
    t_choice = int(input(""))
    if t_choice == 1:
        clear()
        print("Your TnG Top-up is processing....")
        Delay(3)
        print("Your current TnG balance is: ", user1.tnumber + float(10))
        Anothertrans()
    elif t_choice == 2:
        clear()
        print("Your TnG Top-up is processing....")
        Delay(3)
        print("Your current TnG balance is: ", user1.tnumber + float(50))
        Anothertrans()
    elif t_choice == 3:
        clear()
        print("Your TnG Top-up is processing....")
        Delay(3)
        print("Your current TnG balance is: ", user1.tnumber + float(100))
        Anothertrans()
    elif t_choice == 4:
        clear()
        print("Your current balance is:", user1.balance)
        print("Please input amount")
        t_amt = float(input(""))
        if t_amt <= user1.balance:
            clear()
            print("Your TnG Top-up is processing....")
            Delay(3)
            print("Your current TnG balance is: ", user1.tnumber + t_amt)
            Anothertrans()
        else:
            print("Insufficient Balance")
            print("Please check your balance")
            Delay(1)
            print("Do you want to continue TnG Top-up ? (y/n)")
            Con = input("")
            if Con == "y":
                TnG()
            else:
                main_ATM()

    elif t_choice == 0:
        main_ATM()

    else:
        clear()
        print("Please input options 0-4 only")
        Delay(2)
        TnG()



def verify_password():
        print("Please enter pin number")
        password = int(input(""))
        if password == user1.pin:
            main_ATM()
        else:
            print("Invalid pin")
            Delay(1)
            verify_password()




def own_pnumber():
    clear()
    print("Your phone number is", user1.pnumber)
    print ("""
    1 = RM5
    2 = RM10
    3 = RM50
    4 = RM100
    5 = Other
    0 = exit
    """)
    print("Your current balance is RM",user1.balance )
    print("How much do you want to top up (0-5)")
    topup_amt = int(input(""))

    if topup_amt == 1:
        if user1.balance > tuser1.p1:
            print("Your top up is processing....")
            Delay(3)
            print("Sucessfully topup to ", user1.pnumber)
            print("Your current balance is: ", user1.balance - tuser1.p1)
            Anothertrans()
        else:
            print("Insufficient Balance")
            print("Please check your balance")
            Anothertrans()
    elif topup_amt == 2:
        if user1.balance > tuser1.p2:
            print("Your top up is processing....")
            Delay(3)
            print("Sucessfully topup to ", user1.pnumber)
            print("Your current balance is: ", user1.balance - tuser1.p2)
            Anothertrans()
        else:
            print("Insufficient Balance")
            print("Please check your balance")
            Anothertrans()

    elif topup_amt == 3:
        if user1.balance > tuser1.p3:
            print("Your top up is processing....")
            Delay(3)
            print("Sucessfully topup to ", user1.pnumber)
            print("Your current balance is: ", user1.balance - tuser1.p3)
            Anothertrans()
        else:
            print("Insufficient Balance")
            print("Please check your balance")
            Anothertrans()

    elif topup_amt == 4:
        if user1.balance > tuser1.p4:
            print("Your top up is processing....")
            Delay(3)
            print("Sucessfully topup to ", user1.pnumber)
            print("Your current balance is: ", user1.balance - tuser1.p4)
            Anothertrans()
        else:
            print("Insufficient Balance")
            print("Please check your balance")
            Anothertrans()

    elif topup_amt == 5:
        print("Your balance is:", user1.balance)
        topup5 = float(input("Please Enter Amount for Top Up : "))
        if user1.balance > topup5:
            print("Your top up is processing....")
            Delay(3)
            print("Sucessfully topup to ", user1.pnumber)
            print("Your current balance is: ", user1.balance - topup5)
            Anothertrans()
        else:
            print("Insufficient Balance")
            print("Please check your balance")
            Anothertrans()

    elif topup_amt == 0:
        main_ATM()

    else:
        print("Please input option 0-5 only")
        Delay(2)
        own_pnumber()



def other_pnumber():
        clear()
        print("Please insert phone number")
        Mnumber = int(input(""))
        print ("""
        1 = RM5
        2 = RM10
        3 = RM50
        4 = RM100
        5 = Other
        0 = exit
        """)
        print("Your current balance is RM",user1.balance )
        print("How much do you want to top up (0-5)")
        topup_amt = int(input(""))

        if topup_amt == 1:
            if user1.balance > tuser1.p1:
                print("Your top up is processing....")
                Delay(3)
                print("Sucessfully topup to ", Mnumber)
                print("Your current balance is: ", user1.balance - tuser1.p1)
                Anothertrans()
            else:
                print("Insufficient Balance")
                print("Please check your balance")
                Anothertrans()
        elif topup_amt == 2:
            if user1.balance > tuser1.p2:
                print("Your top up is processing....")
                Delay(3)
                print("Sucessfully topup to ", Mnumber)
                print("Your current balance is: ", user1.balance - tuser1.p2)
                Anothertrans()
            else:
                print("Insufficient Balance")
                print("Please check your balance")
                Anothertrans()

        elif topup_amt == 3:
            if user1.balance > tuser1.p3:
                print("Your top up is processing....")
                Delay(3)
                print("Sucessfully topup to ", Mnumber)
                print("Your current balance is: ", user1.balance - tuser1.p3)
                Anothertrans()
            else:
                print("Insufficient Balance")
                print("Please check your balance")
                Anothertrans()

        elif topup_amt == 4:
            if user1.balance > tuser1.p4:
                print("Your top up is processing....")
                Delay(3)
                print("Sucessfully topup to ", Mnumber)
                print("Your current balance is: ", user1.balance - tuser1.p4)
                Anothertrans()
            else:
                print("Insufficient Balance")
                print("Please check your balance")
                Anothertrans()

        elif topup_amt == 5:
            print("Your current balance is:", user1.balance)
            topup5 = float(input("Please Enter Amount for Top Up : "))
            if user1.balance > topup5:
                print("Your top up is processing....")
                Delay(3)
                print("Sucessfully topup to ", Mnumber)
                print("Your current balance is: ", user1.balance - topup5)
                Anothertrans()
            else:
                print("Insufficient Balance")
                print("Please check your balance")
                Anothertrans()

        elif topup_amt == 0:
            main_ATM()

        else:
            print("Please input options 0-5 only")
            Delay(2)
            other_pnumber()



def Anothertrans():
    print("Do you want to make another transaction? (y/n)")
    anothertrans = input("")
    if anothertrans == "y":
        main_ATM()
    else:
            print("Okay,Thank you for using our service!")
            Delay(1)
            exit()



def Localtrans():
    clear()
    print("Your current balance is RM",user1.balance )
    print("Please enter the Bank number")
    bank_num = int(input(""))
    print("Enter amount to Transfer")
    oth_usr_amt = float(input(""))
    if oth_usr_amt <= user1.balance:
        print("Successfully Transferred to", bank_num)
        print("=============================================")
        print("Your new balance is ", user1.balance - oth_usr_amt)
        Anothertrans()
    else:
        print("Insufficient balance")
        print("Please check your balance")
        Anothertrans()



def Overseastrans():
    clear()
    print("Please input account number")
    rec_bn = int(input(""))
    if rec_bn == o_receiver4.acc_number:
        print("Your current balance is RM",user1.balance )
        print("Enter amount to tranfer")
        oth_usr_amt = float(input(""))
        if oth_usr_amt <= user1.balance:
            print("Successfully Transferred to", o_receiver4.name)
            print("Bank: ", o_receiver4.bank_name,"======", "Account number: ", o_receiver4.acc_number)
            print("=============================================")
            print("Your new balance is ", user1.balance - oth_usr_amt)
            Anothertrans()
        else:
            print("Insufficient balance")
            Anothertrans()
    else:
        print("Invalid account number")



def Favouritetrans1():
    clear()
    print("Your current balance is RM",user1.balance )
    print("Enter amount to tranfer")
    oth_usr_amt = float(input(""))
    if oth_usr_amt <= user1.balance:
        print("Successfully Transferred to", o_receiver1.name)
        print("Bank: ", o_receiver1.bank_name,"======", "Account number: ", o_receiver1.acc_number)
        print("=============================================")
        print("Your new balance is ", user1.balance - oth_usr_amt)
        Anothertrans()
    else:
        print("Insufficient balance")
        Anothertrans()



def Favouritetrans2():
    clear()
    print("Your current balance is RM",user1.balance )
    print("Enter amount to tranfer")
    oth_usr_amt = float(input(""))
    if oth_usr_amt <= user1.balance:
        print("Successfully Transferred to", o_receiver2.name)
        print("Bank: ", o_receiver2.bank_name,"======", "Account number: ", o_receiver2.acc_number)
        print("=============================================")
        print("Your new balance is ", user1.balance - oth_usr_amt)
        Anothertrans()
    else:
        print("Insufficient balance")
        Anothertrans()



def Favouritetrans3():
    clear()
    print("Your current balance is RM",user1.balance )
    print("Enter amount to tranfer")
    oth_usr_amt = float(input(""))
    if oth_usr_amt <= user1.balance:
        print("Successfully Transferred to", o_receiver3.name)
        print("Bank: ", o_receiver3.bank_name,"======", "Account number: ", o_receiver3.acc_number)
        print("=============================================")
        print("Your new balance is ", user1.balance - oth_usr_amt)
        Anothertrans()
    else:
        print("Insufficient balance")
        Anothertrans()



def Favourite():
    clear()
    print("Please choose options")
    print("""
        1 == Ali
        2 == father
        3 == brother
        """)
    options = int(input(""))
    if options   == 1:
        Favouritetrans1()
    elif options == 2:
        Favouritetrans2()
    elif options == 3:
        Favouritetrans3()
    else:
        clear()
        print("Please choose options 1-3 only")
        Delay(2)
        Favourite()



def main_ATM():
    clear()
    while True:
        print("Welcome,",user1.name)
        print("""
        Choose Transaction

        1  = Enquire bank balance
        2  = Amount withdrawn
        3  = Amount transfer
        4  = Mobile top-up
        5  = Change of ATM card pin
        6  = Print mini statement
        7  = Pay bills
        8  = ATM card activation For overseas usage
        9  = TnG Top-up
        10 = User profile information
        0  = Exit
        """)



        print("Please choose a transaction(0-10) ")
        user_transaction = input("")

        if   user_transaction == "0":
            close()
        elif user_transaction == "1":
            Enquire()
        elif user_transaction == "2":
            FN_withdrawn()
        elif user_transaction == "3":
            Transfer()
        elif user_transaction == "4":
            TopUp()
        elif user_transaction == "5":
            ChangePin()
        elif user_transaction == "6":
            Print()
        elif user_transaction == "7":
            PayBills()
        elif user_transaction == "8":
            Activation()
        elif user_transaction == "9":
            TnG()
        elif user_transaction == "10":
            User_profile()

        else:
            clear()
            print("Invalid transaction, Please input option 1-9 only")
            Delay(2)


def Enquire():
    clear()
    print(user1.name, "your balance is ", user1.balance)
    print("=============================================")
    Anothertrans()



def FN_withdrawn():
    clear()
    print("Your current balance is RM",user1.balance )
    print("Enter amount to withdrawn")
    withdrawn = float(input(""))
    if withdrawn <= user1.balance :
        print("Checking balance....")
        Delay(2)
        print("Success")
        print("=============================================")
        print("Your new balance is ", user1.balance - withdrawn)
        Anothertrans()
    else:
        print("Checking balance....")
        Delay(2)
        print("Insufficient balance, your current balance is", user1.balance)
        Anothertrans()



def Transfer():
    clear()
    print("Please choose option 1-2")
    print("")
    print("""
        1 = Local     Transfer
        2 = Overseas  Transfer
        3 = Favourite Transfer
        """)
    trans_type = int(input(""))
    if trans_type   == 1:
        Localtrans()
    elif trans_type == 2:
        Overseastrans()
    elif trans_type == 3:
        Favourite()

    else:
        print("Please input option 1-3 only")



def TopUp():
    clear()
    print("Mobile Top up")
    print("Choose options")
    print("""
    1  = My phone number
    2  = Other phone number
    0  = exit
    """)
    p_option = int(input(""))
    if p_option   == 1:
        own_pnumber()
    elif p_option == 2:
        other_pnumber()
    elif p_option == 3:
        main_ATM()
    else:
        print("Please choose option 0-2 only")
        TopUp()



def ChangePin():
    clear()
    print("Please insert old Pin for verification")
    old_pin = int(input(""))
    if old_pin == user1.pin:
        print ("Please insert the New Pin Number")
        Npinnumber = input("")
        print("Changing....")
        Delay(2)
        print("Your pin number has been updated successfully!")
        Anothertrans()
    else:
        print("Invalid Pin")
        Anothertrans()



def Print():
    clear()
    print("This is your statement              ", user1.name)
    print(date_time,"          XYZBank")
    print("""
    ===============================================
    To know more info. Call xxx-xxxxxxx for
    more customer services
    ===============================================
    ||   Date    || Amount(RM) ||   +   ||   -   ||
    ||  22/09/20 ||   5900     ||       ||       ||
    ||  31/10/20 ||   5900     || 300   ||       ||
    ||  16/10/20 ||   6200     ||       ||  900  ||
    ||  12/11/20 ||   5300     ||       ||  300  ||
    ||  01/01/21 ||   5000     || 7000  ||       ||
    ||  03/02/21 ||   12000    ||       ||  2000 ||
    ||  04/03/21 ||   10000    ||       ||       ||
    ==============================================
    || Total     ||      RM5000                  ||
    ===============================================
    """)
    print("Do you want to print a mini statement? (y/n)")
    printMS = input("")
    if printMS == "y":
        print("Printing.....")
        Delay(2)
        print("Complete!")
        Anothertrans()
    else:
        Anothertrans()



def PayBills():
    clear()
    print("Current payable bills")
    print("""

    1  =  TnB          = RM300
    2  =  Water Bill   = RM30
    3  =  Unifi        = RM200
    4  =  Car          = RM6000
    0  =  exit
    """)
    print("Which bills do you want to pay?")
    print("Please Enter (0-4)")
    bill = int(input(""))
    if bill == 1:
        if user1.balance > billuser1.tnb:
            print("Verfying balance..")
            Delay(2)
            print("Payment complete!")
            print("Your current balance is", user1.balance - billuser1.tnb)
            Anothertrans()
        else:
            print("Verifying balance..")
            Delay(2)
            print("Insufficient balance")
            Anothertrans()


    elif bill == 2:
        if user1.balance > billuser1.water:
            print("Verfying balance..")
            Delay(2)
            print("Payment complete!")
            print("Your current balance is", user1.balance - billuser1.water)
            Anothertrans()
        else:
            print("Verifying balance..")
            Delay(2)
            print("Insufficient balance")
            Anothertrans()


    elif bill == 3:
        if user1.balance > billuser1.unifi:
            print("Verfying balance..")
            Delay(2)
            print("Payment complete!")
            print("Your current balance is", user1.balance - billuser1.unifi)
            Anothertrans()
        else:
            print("Verifying balance..")
            Delay(2)
            print("Insufficient balance")
            Anothertrans()


    elif bill == 4:
        if user1.balance > billuser1.car:
            print("Verfying balance..")
            Delay(2)
            print("Payment complete!")
            print("Your current balance is", user1.balance - billuser1.car)
            Anothertrans()
        else:
            print("Verifying balance..")
            Delay(2)
            print("Insufficient balance")
            Anothertrans()

    elif bill == 0:
        main_ATM()

    else:
        print("Please input options 0-5 only")
        Delay(2)
        PayBills()



def Activation():
    clear()
    print ("=====================================")
    print("ATM card activation for overseas usage")
    print ("=====================================")
    print("Please insert current Pin for verification")
    old_pin = int(input(""))
    if old_pin == user1.pin:
        print("verifying...")
        Delay(2)
        print("Do you want to activate ATM card for overseas usage? (y/n)")
        activ = input("")
        if activ == "y":
            print("Activating....")
            Delay(3)
            print("Your card has sucessfully activated for overseas usage")
            Anothertrans()
        else:
            print("Overseas usage failed to be activated")
            Anothertrans()
    else:
        print("Invalid Pin")
        Anothertrans()

def User_profile():
    clear()
    print("Name            :", user1.name)
    print("Pin number      :", user1.pin)
    print("Account Number  :", user1.acc_number)
    print("Phone number    :", user1.pnumber)
    print("Current Balance : RM", user1.balance)
    print("TnG Balance     : RM", user1.tnumber)
    print()
    Anothertrans()



def close():
    print("Thank you for using our services, have a good day!")
    Delay(1)
    exit()

#  Main program
Intro()
