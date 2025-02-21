import csv
import os
from datetime import datetime

DATA_FILE = "../data/transactions.csv"

# Predefined categories
EXPENSE_CATEGORIES = ["Rent", "Food", "Transport", "Entertainment", "Utilities", "Others"]
INCOME_CATEGORIES = ["Salary", "Scholarship", "Freelance", "Investments", "Others"]

def add_transaction(transaction_type, category, amount, description=""):
    """Adds a new transaction (income or expense) to the CSV file."""
    amount = float(amount)
    date = datetime.today().strftime('%Y-%m-%d')
    # GEt the full month name
    month = datetime.today().strftime('%B')
    
    # Validate category
    if transaction_type == "Expense" and category not in EXPENSE_CATEGORIES:
        print(f"Invalid category. Choose from: {', '.join(EXPENSE_CATEGORIES)}")
        return
    if transaction_type == "Income" and category not in INCOME_CATEGORIES:
        print(f"Invalid category. Choose from: {', '.join(INCOME_CATEGORIES)}")
        return

    file_exists = os.path.isfile(DATA_FILE)
    
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if file is empty
        if not file_exists:
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])
        
        writer.writerow([date, transaction_type, category, amount, description])

    print(f"{transaction_type} of ${amount} added to {category}.")

def view_transactions():
    """Displays all transactions from the CSV file."""
    if not os.path.isfile(DATA_FILE):
        print("No transactions found.")
        return

    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        transactions = list(reader)

        if len(transactions) == 1:
            print("No transactions recorded yet.")
            return

        print("\nTransaction History:")
        for row in transactions:
            print(" | ".join(row))