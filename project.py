import mysql.connector
import bcrypt
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    port=3306,
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS mykolo_db")
cursor.execute("USE mykolo_db")
print("Connected to mykolo database!")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        balance DECIMAL(10, 2) DEFAULT 0.00,
        account_number VARCHAR(10) NOT NULL UNIQUE
    )
    """
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(10) NOT NULL,
    transaction_type VARCHAR(20) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    description VARCHAR(255),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

#Simple Banking System
exp=int(input("welcome to myKolo App\n Enter your choice\n 1.Login\n 2.Create Account\n 3.Reset Password\n 4.Exit\nEnter Option: "))

 

users = {
    "john.doe@example.com": {"name": "John Doe", 
    "password": "password123", 
    "balance": 1000,
    "account_number": "1000000001",
    "transactions": []
    },

    "jane.doe@example.com":{
        "name": "Jane Doe",
        "password": "jane123",
        "balance": 5000,
        "account_number": "1000000002",
        "transactions": []
    },

    "jack.jill@example.com":{
        "name": "Jack Jill",
        "password": "jack012",
        "balance": 10000,
        "account_number": "1000000003",
        "transactions": []
    }
}

if exp == 1:
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    cursor.execute(
        """
        SELECT account_number, name, email, password, balance
        FROM users
        WHERE email = %s
        """,
        (email,)
    )

    user = cursor.fetchone()
    
    if user:
        stored_password = user[3]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password.encode("utf-8")
        ):
            print("Login successful!")

            while True:
                print("\n===== myKolo Main Menu =====")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transfer")
                print("4. Check Balance")
                print("5. Transaction History")
                print("6. View Profile")
                print("7. Change Password")
                print("8. Logout")
                choice = input("Enter your choice: ")
            #Deposit  
                if choice == "1":
                    try:
                        amount = float(input("Enter the amount to deposit: "))
                
                        if amount <= 0:
                            print(f"Deposit amount must be greater than 0.")
                        else:
                            users[email]["balance"] += amount
                            users[email]["transactions"].append(f"Deposited: ${amount}")
                            print(f"Deposited ${amount} successfully!")
                            print(f"New balance: ${users[email]['balance']}")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                #Withdraw
                elif choice == "2":
                    try:
                        amount = float(input("Enter the amount to withdraw: "))
                
                        if amount <= 0:
                            print("Withdrawal amount must be greater than 0.")
                        elif amount > users[email]["balance"]:
                            print("Insufficient funds.")
                        else:
                            users[email]["balance"] -= amount
                            users[email]["transactions"].append(f"Withdrew: ${amount}")
                            print(f"Withdrew ${amount} successfully!")
                            print(f"New balance: ${users[email]['balance']}")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                 #Transfer
                elif choice == "3":
                    try:
                        recipient_account_number = input("Enter the recipient's account number: ")
                        amount = float(input("Enter the amount to transfer: "))
                        recipient_email = None
                        for user_email in users:
                            if users[user_email]["account_number"] == recipient_account_number:
                                recipient_email = user_email
                                break
                        if recipient_email is None:
                            print("Invalid recipient account number")
                        elif recipient_email == email:
                            print("You cannot transfer to your own account.")
                        elif amount <= 0:
                            print("Transfer amount must be greater than 0.")
                        elif amount > users[email]["balance"]:
                            print("Insufficient balance for the transfer.")
                        else:
                            users[email]["balance"] -= amount
                            users[recipient_email]["balance"] += amount
                            users[email]["transactions"].append(f"Transferred: ${amount} to {recipient_email}")
                            users[recipient_email]["transactions"].append(f"Received: ${amount} from {email}")
                            print(f"Transferred ${amount} to {recipient_email} successfully!")
                            print(f"New balance: ${users[email]['balance']}")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                #Check Balance
                elif choice == "4":
                    print(f"Your current balance is: ${users[email]['balance']}")
                #Transaction History
                elif choice == "5":
                    print("Transaction History:")
                    for transaction in users[email]["transactions"]:
                        print(transaction)
                #View Profile
                elif choice == "6":
                    print(f"Name: {users[email]['name']}")
                    print(f"Email: {email}")
                    print(f"Account Number: {users[email]['account_number']}")
                    print(f"Balance: ${users[email]['balance']}")
            #Change Password
                elif choice == "7":
                    current_password = input("Enter your current password: ")
                    if current_password == users[email]["password"]:
                        new_password = input("Enter your new password: ")
                        users[email]["password"] = new_password
                        print("Password changed successfully!")
                    else:
                        print("Incorrect current password.")
            #Logout
                elif choice == "8":     
                    print("Logging out...")
                    break
            else:
                print("Incorrect password. Please try again.")

   

if exp == 2:
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    #check if email already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        print("Email already exists.")
    else:
        #generate account number
        cursor.execute("SELECT COUNT(*) FROM users")
        result = cursor.fetchone()
        num_users = result[0] 
        account_number = str(1000000000 + num_users + 1)
        #Hash password
        hashed_password=bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        #save user to database
        sql = """INSERT INTO users (name, email, password, balance, account_number) VALUES (%s, %s, %s, %s, %s)"""
        
        values = (
            name,
            email,
            hashed_password,
            0,
            account_number
        )
        cursor.execute(sql, values)
        conn.commit()
    
    print(f"Account created successfully! Your account number is {account_number}")
if exp == 3:
    email = input("Enter your email: ")
    if email in users:
        new_password = input("Enter your new password: ")
        users[email]["password"] = new_password
        print("Password reset successfully!")
    else:
        print("Email not found. Please try again.")
if exp == 4:
    print("Exiting mykolo app. Goodbye!")

import mysql.connector
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    port=3306,
)

cursor = conn.cursor()
       


        
                
