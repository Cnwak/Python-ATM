name = input("What is your name? \n" )

from datetime import datetime
now= datetime.now()

approved_names=["Emeka", "Deji" , "Mike"]
approved_passwords= ["passwordEmeka", "passwordDeji","passwordMike"]


if(name in approved_names):
    password= input("Please input your password \n")
    user_id = approved_names.index(name)

    if(password == approved_passwords[user_id]):
        print("Welcome back %s" %name)
        
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Todays date and time are ",date_time )

        print("These are the options:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Complaint")
        
        atm_input=input("How can we help you today? \n")
        if(atm_input == "1"):
            input("How much would you like to withdraw? \n")
            print("Take your cash.")
            pass
        
        elif(atm_input == "2"):
            deposit=input("How much would you like to deposit? \n")
            print("Your current balance is $%s." %deposit)
            pass
        
        elif(atm_input == "3"):
             input("What issue will you like to report? \n")
             print("Thank you for contacting us.")
             pass
        else:
            print("Invalid option selected")
    else:
        print("Incorrect password, please try again.")
        
else:
    print("You are not an approved user")
    

        
    




