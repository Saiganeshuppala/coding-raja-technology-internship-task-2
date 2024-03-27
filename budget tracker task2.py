import json
import os
from datetime import datetime

TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "r") as file:
            return json.load(file)
    else:
        return {"income": [], "expenses": []}

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

def record_income(transactions):
    amount = float(input("Enter income amount: "))
    category = input("Enter income category: ")
    transactions["income"].append({"amount": amount, "category": category, "date": str(datetime.now())})
    save_transactions(transactions)
    print("Income recorded successfully.")

def record_expense(transactions):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    transactions["expenses"].append({"amount": amount, "category": category, "date": str(datetime.now())})
    save_transactions(transactions)
    print("Expense recorded successfully.")

def calculate_budget(transactions):
    total_income = sum(transaction["amount"] for transaction in transactions["income"])
    total_expenses = sum(transaction["amount"] for transaction in transactions["expenses"])
    remaining_budget = total_income - total_expenses
    return remaining_budget

def analyze_expenses(transactions):
    expense_categories = {}
    for transaction in transactions["expenses"]:
        category = transaction["category"]
        amount = transaction["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    print("Expense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount}")

def main():
    transactions = load_transactions()

    while True:
        print("\nOptions:")
        print("1. Record Income")
        print("2. Record Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            record_income(transactions)
        elif choice == "2":
            record_expense(transactions)
        elif choice == "3":
            remaining_budget = calculate_budget(transactions)
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == "4":
            analyze_expenses(transactions)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
