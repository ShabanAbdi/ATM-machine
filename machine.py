balance = 1000.00
pin = 2099
transactions = []
import time

print("Enter your PIN number:")
entered_pin = int(input("PIN: "))

if entered_pin == pin:
    choice = 0

    while choice != 5:
        
        print("ATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        choice = int(input ("Choose an option: "))
        if choice == 1:
         print(f"Your current balance is: KES {balance:.2f}")
        elif choice == 2:
           deposit_amount = float(input("Enter deposit amount: "))
           balance += deposit_amount
           transactions.append((f"Deposit, {deposit_amount:.2f}"))
           print(f"Deposit successful, your new balance is: KES {balance:.2f}")
        elif choice == 3:
           print(f"Remaining Balance: KES {balance:.2f}")
           time.sleep(2)
           withdraw_amount = float(input("How much would you like to withdraw? "))
           if withdraw_amount < 50:
            print("Minimum withdrawal amount is KES 50!")
           elif withdraw_amount <= balance:
              balance = balance - withdraw_amount
              transactions.append((f"Withdrawal, {withdraw_amount:.2f}"))
              print(f"Withdrawal successful, your new balance is: KES {balance:.2f}")
           else:
              time.sleep(2)  # Pause for 2 seconds before displaying the message
              print("Insufficient funds.")
        elif choice == 4:
           for transaction in transactions[-5:]:  # Display last 5 transactions
            print(transaction)
        elif choice == 5:
           print("Thankyou for Banking with us, Have a Good Day!!")
        time.sleep(3)      # Pause for 3 seconds indicating the end of the session
else:
    print("Incorrect PIN. Access denied.")
