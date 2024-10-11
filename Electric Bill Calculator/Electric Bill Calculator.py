import csv  # Import csv file into the system
import matplotlib.pyplot as plt  # Import matplotlib to create a graph based on data

def main_program(): # Main program function
    print("Electric Bill Calculation")
    name = str(input("Please insert your name to continue: "))  # User input name into system
    print("       =================")
    print("         Welcome " + name)  # Output name
    print("       =================")
    main_menu()  # Call main menu function
    
def main_menu(): # Main menu Function
    print("""
          [1] Add Electric Bill
          [2] Show data of monthly Electric Bill
          [3] Show Graph of monthly Electric Bill
          Input "0" to exit
          
          """)      
    option = int(input("Please input options [0-3]: "))  # Get user input as option
    while option < 0 or option > 3:  #The system will loop when the user does not input the correct option
        print("Invalid Option")
        option = int(input("Please input options [0-3]: "))
    if option == 1: 
        add_month() # Add electric bill and calculation function
        continue_or_no()
    elif option == 2:
        show_result() # Show Result function
        continue_or_no()
    elif option == 3:
        show_graph() # Show Graph function
        continue_or_no()
    elif option == 0:
        print("Thank you for using the system")
        exit()  # Exit system 
    
def add_month(): # Add month/ data and calculation function
    month = str(input("Please insert month [e.g January]: "))  # User input month
    consumption = float(input("Please insert total electric consumption of this month[kWh]: "))  # User input total electric consumption of the month 
    if(consumption>0 and consumption<=200): # if electric is less and equal to 200
        consumptionP = ((consumption*21.80)/100) 
        consumptionGP = ((consumption*3.7)/100) # Green Electric Tariff calculation 
        print("")

    elif(consumption>200 and consumption<=300): # If electric in range of 201-300
        first_consumption = 200  # Assume the first 200kWh when consumption exceed 200kWh
        consumption1 = ((first_consumption)*21.80)/100  # (200 x 21.80)/100
        consumption2 = ((consumption - 200)*33.4)/100  # (remaining x 33.40)/100
        consumptionP = consumption1 + consumption2
        consumptionGP = ((consumption*3.7)/100) # Green Electric Tariff calculation 
        print("")
        
    elif(consumption>300 and consumption <= 600): 
        first_consumption = 200 # Assume the first 200kWh when consumption exceed 200kWh
        second_consumption = 100  # Assume the first 200kWh when consumption exceed 200kWh
        consumption1 = ((first_consumption)*21.80)/100 # (200 x 21.80)/100
        consumption2 = ((second_consumption)*33.4)/100 # (100 x 33.40)/100
        consumption3 = ((consumption - 300)*51.6)/100  # (remaining x 51.60)/100
        consumptionP = consumption1 + consumption2 + consumption3
        consumptionGP = ((consumption*3.7)/100) # Green Electric Tariff calculation
        print("")
        
    elif (consumption > 600):
        first_consumption = 200
        second_consumption = 100
        third_consumption = 300
        consumption1 = ((first_consumption)*21.80)/100 # (200 x 21.80)/100
        consumption2 = ((second_consumption)*33.4)/100 # (100 x 33.40)/100
        consumption3 = ((third_consumption)*51.6)/100 # (300 x 51.60)/100
        consumption4 = ((consumption - 600)*54.6)/100 # (remaining x 54.60)/100
        consumptionP = consumption1 + consumption2 + consumption3 + consumption4
        consumptionGP = ((consumption*3.7)/100) # Green Electric Tariff calculation
        print("")

        
    else:
        print("Your current bill: RM 0")

    TotalPrice = (consumptionGP + consumptionP) # Total price of the bill
    Total_Price = str(TotalPrice) # Change float(TotalPrice) variable into string variable
    print("============================================================")
    print("Your electric consumption[kWh]: " + str(consumption) + "kWh")
    print("Your electric consumption Price w/o tariff: RM" + str(consumptionP))
    print("============================================================")
    print("Total Price = RM" + str(TotalPrice))
    print("============================================================")        
    option = int(input("Do you want to save this data? [1] -- yes  [2] -- no: ")) # Allow user to save the data into csv file
    if option == 1: 
            file = open("data.csv", "a") # Open and append "a" csv file
            file.write(month + ", " + Total_Price + "\n") # Append the month variable and Total_Price variable into data
            print("Data added successfully!")
    else:
        continue_or_no()


def show_result():  #Show data of the files in console
    file = open("data.csv") # Open csv file
    csvreader = csv.reader(file) # Read csv file as .reader
    print("===================")
    print("  Month  |  Price  ")
    print("===================")
    for row in csvreader: # Scan the every rows that are available in the csv file
        print(row) # Print data
    file.close # Close csv file


def show_graph():   # Show graph with matplotlib
    x = []  # Assume x as an empty array
    y = []  # Assume x as an empty array
    
    with open("data.csv", "r") as csvfile:  # Open and read "r" csv file
        plots = csv.reader(csvfile, delimiter = ",") # read the csv file while removing ","
        
        for row in plots:   #Scan every rows that are available in the file
            x.append(row[0])    # Add data of the row 0 (month) into x array
            y.append(float(row[1])) # Add data of the row 1(Price (RM)) into y array
            
    plt.bar(x, y, color = "b", width = 0.72, label = "Month")   # Modify the file by applying colors, adjust widdth and put label as month
    plt.xlabel("Month") # X-axis
    plt.ylabel("Price(RM)") # Y- axis
    plt.title("Monthly Electric bill fee") # Title
    plt.legend("Month") # Legend
    plt.show() #Show Graph


def continue_or_no():   # Allow the user to continue the program or no
    option = int(input("Do you want to continue? [1] -- yes [2] -- no: "))
    if option == 1:
        main_menu()    # Redirect user to main menu
    else:
        print("Thank you for using the system")
        exit() # Exit Program

main_program()  #Main Program