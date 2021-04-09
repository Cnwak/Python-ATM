
# IMPORTING DATE-TIME
from datetime import datetime
now= datetime.now()


# IMPORTING RANDOM
import random
records={"Emeka": "passwordEmeka",
          "Seyi" : "passwordSeyi",
          "Mike": "passwordMike"}


# INITIALIZING FUNCTION
def init():
    is_valid_option = False 

    print("Welcome to Simba Bank")
    while is_valid_option == False:

        have_acct=input("Do you have an account with us? 1 (yes) 2 (no) \n")
        if(have_acct == '1'):
            is_valid_option = True
            login()
            
        elif(have_acct == '2'):
            is_valid_option = True
            print(register())  
            
        else:
            print("Invalid option selected")  

# LOGIN FUNCTION
def login():
    
    name = input("What is your login name? \n" )



    if(name in records):
        password= input("Please input your password \n")
        

        if(password == records[name]):
            print("Welcome back %s" %name)
            
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Todays date and time are ",date_time )
            bank_operations()

        else:
            print("Incorrect password, please try again.")
            init()
            
    else:
        print("You are not an approved user.")
        init()
            

# REGISTRATION FUNCTION        
def register():
  will_register = input("You do not have an account with us, would you like to register? 1 (yes) 2 (no) \n")
  if(will_register == '1'):
    first_name = input("What is your first name? \n")
    last_name =input("What is your last name? \n")
    email =input("What is your email address? \n")
    password =input("Create a password \n")
    account_num = generate_acct_num()

    records[account_num] = [first_name, last_name, email]

    print("Your account has been created")

    login()

  elif(will_register == '2'):
    print("Please come back again sometime.")

  else:
    print("Invalid option selected")
    init()  


# ACCOUNT NUMBER GENERATOR FUNCTION
def generate_acct_num():
  print("Generating account number...")
  return random.randrange(0000000000,9999999999)


# BANK OPERATION FUNCTIONS
def bank_operations():
    
            print("These are the options:")
            print("1. Withdrawal")
            print("2. Deposit")
            print("3. Complaint")

            # IMPROVEMENT/EXTRA/ADDITIONAL OPTION
            print("4. Logout")
            
            atm_input=input("How can we help you today? \n")
            if(atm_input == "1"):
                withdraw()
             
            elif(atm_input == "2"):
               deposit()
            
            elif(atm_input == "3"):
                complaint()


            elif(atm_input == "4"):
                init()


            else:
                print("Invalid option selected")
                init()

# WITHDRAW FUNCTION
def withdraw():
       input("How much would you like to withdraw? \n")
       print("Take your cash.")
       pass
            
# DEPOSIT FUNCTION
def deposit():
     deposit=input("How much would you like to deposit? \n")
     print("Your current balance is $%s." %deposit)
     pass

# COMPLAINT FUNCTION
def complaint():
    input("What issue will you like to report? \n")
    print("Thank you for contacting us.")
    pass    

    
# INITIALIZING   
init()





