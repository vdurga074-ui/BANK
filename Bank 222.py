
from datetime import datetime

balance = float(input("enter initial opening balance :"))
opening_balance = balance
transactions = []

while True:
    print("1 Deposit")
    print("2 Withdrawal")
    print("3 Check balance")
    print("4 Statement")
    print("5 Mini Statemenet (Last N transection)")
    print("6 End-of-Session Ledger Audit Summary")
    print("7 Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transactions.append((datetime.now(), "Deposit", amount))
        else:
            print("Amount must be positive.")
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            transactions.append((datetime.now(), "Withdrawal", amount))
        else:
            print("Invalid amount or insufficient funds.")
    elif choice == "3":
        print(f"Balance: {balance:.2f}")
    elif choice == "4":
        for date, action, amount in transactions:
            print(f"{date}: {action} {amount:.2f}")
        print(f"Current balance: {balance:.2f}")
    elif choice == "5":
        try:
            count = int(input("How many transactions should be shown? "))
            if count < 0:
                print("Enter a non-negative number.")
            else:
                for date, action, amount in transactions[-count:] if count else []:
                    print(f"{date}: {action} {amount:.2f}")
        except ValueError:
            print("Enter a valid whole number.")
    elif choice == "6":
        deposits = sum(amount for _, action, amount in transactions if action == "Deposit")
        withdrawals = sum(amount for _, action, amount in transactions if action == "Withdrawal")
        expected_balance = opening_balance + deposits - withdrawals
        print(f"Opening balance: {opening_balance:.2f}")
        print(f"Total deposits: {deposits:.2f}")
        print(f"Total withdrawals: {withdrawals:.2f}")
        print(f"Calculated balance: {expected_balance:.2f}")
        print(f"Current balance: {balance:.2f}")
        print("Audit: PASSED" if abs(expected_balance - balance) < 0.000001 else "Audit: FAILED")
    elif choice == "7":
        print("TQ for Using this Bank , Have a Nice day!.")
        break
    else:
        print("Invalid option.")
