import hashlib
import datetime

# Initialize an empty dictionary to store user login data
user_login_data = {}
user_id_counter = 1  # Starting user ID

def register_user():
    global user_id_counter  # Use the global counter
    
    username = input("Enter your desired username: ")
    
    # Check if the username already exists
    if username in user_login_data:
        print("Username already exists. Please choose another username.")
        return  # Exit the function if the username already exists
    
    password = input("Enter your password: ")
    
    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Assign a unique user ID
    user_id = user_id_counter
    user_id_counter += 1
    
    # Store the user registration data in the dictionary
    user_login_data[username] = {'user_id': user_id, 'hashed_password': hashed_password}
    
    print(f"Registration successful for {username} with user ID:{user_id}.")

# Example of registering a user
register_user()

username = input("Enter your username for login: ")

current_balance = 20000

# Check login credentials
if username in user_login_data:
    stored_hashed_password = user_login_data[username]['hashed_password']
    password = input("Enter your password for login: ")
    
    # Verify the entered password against the stored hashed password
    if hashlib.sha256(password.encode()).hexdigest() == stored_hashed_password:
        print(f"Welcome {username}")
        
        today = datetime.datetime.now()
        print('Date:', today)

        def menu():
            print("LBDI ATM Machine Liberia Inc")
            print("Date: ", today)
            print('1. Withdrawal ')
            print('2. Cash Deposit')
            print('3. Complaint')
            print('4. Other services') 

        
        menu()
        SelectedOption = int(input('Please select an option: '))

        while SelectedOption != 0:
            if SelectedOption == 1:
                print(f'You selected option:  {SelectedOption}')
                withdrawal_amount = float(input('How much will you like to withdraw: '))
                if withdrawal_amount > current_balance:
                    print('Insufficient funds. Please try a lower amount.')
                else:
                    current_balance -= withdrawal_amount
                    print(f'Take your cash. Transaction successful. Remaining balance: {current_balance}USD ')
                
            elif SelectedOption == 2:
                print(f'You selected option: {SelectedOption}' )
                deposit_amount = float(input('How much would you like to deposit: '))
                current_balance += deposit_amount 
                print(f'Deposit successful. Updated balance: {current_balance}USD')

            elif SelectedOption == 3:
                print("You selected option: {SelectedOption}")
                input('What issue would you like to report: ')
                print('Thank you for contacting us. Stay safe.')

            elif SelectedOption == 4:
                print("You selected option: {SelectedOption}")
                # Add other services here
        
            else:
                print("Selected option is invalid. Please try again.")

            print()
            menu()
            SelectedOption = int(input('Please select an option: '))

        print("Thank you for using our services. Have a great day!")

    else:
        print('Password incorrect. Please try again.')

else:
    print('Username not found. Please try again.')

