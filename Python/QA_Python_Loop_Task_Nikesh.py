import os
#menu user enters a number to select their desired option
def menu():
    print (56 * "-", "Main Menu", 56 * "-", "\n")  # top margin to highlight its a menu
    print ("1: Print out square numbers between 1 and 100 until the squared value reaches 200. ")
    print ("2: Enter a value that you want to square up to. (custom) ")
    print ("0: Exit ") # option to leave the program
    print (123 * "-") # bottom margin

def square_numbers(max_val,square_lim): # this function prints squared numbers alongside the original number
    for i in range(max_val):
        if i**2 > square_lim: # checks if the maximum squared value is reached
            break
        else:
            print (str(i) + " - " + str(i**2))

ans = True

while ans:
    
    menu() # calling the menu function to display the options to the user
    selection = input("Enter the corresponding number to select an option [1,2,0]: ") # user inputs option

    if selection == '1': # default requirement 1-100
        os.system('cls') # On terminals such as command prompt it clears any previous output if the user decides to run another configuration/option
        print ("You have selected to print out square numbers between 1 and 100, if a squared number is above 200 the program will stop.")
        square_numbers(101,200)
        
    elif selection == '2': # custom run
        os.system('cls')
        custom_num =  int(input("Enter a number that you want to square numbers up to: "))
        custom_lim =  int(input("Enter the maximum squared number you wish to stop the program at: "))
        square_numbers(custom_num+1,custom_lim)
        
    elif selection == '0': # exit program
        os.system('cls')
        print ("Exiting")
        loop = False
        break
    
    else: # if the user enters an invalid key/s
        os.system('cls')
        print ("Invalid option, enter any key to try again...")
    
        
