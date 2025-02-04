import csv
import os
from datetime import datetime

DATA_FILE = "../data/transactions.csv"

def add_transaction(transaction_type, category, amount, description=""):
    """Adds a new transaction (income or expense) to the CSV file."""
    amount = float(amount)
    date = datetime.today().strftime('%Y-%m-%d')

    file_exists = os.path.isfile(DATA_FILE)
    
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if file is empty
        if not file_exists:
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])
        
        writer.writerow([date, transaction_type, category, amount, description])

    print(f"✅ {transaction_type} of ${amount} added to {category}.")

def view_transactions():
    """Displays all transactions from the CSV file."""
    if not os.path.isfile(DATA_FILE):
        print("⚠ No transactions found.")
        return

    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        transactions = list(reader)

        if len(transactions) == 1:
            print("⚠ No transactions recorded yet.")
            return

        print("\n📊 Transaction History:")
        for row in transactions:
            print(" | ".join(row))