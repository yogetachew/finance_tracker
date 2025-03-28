import csv
import os

DATA_FILE = "../data/transactions.csv"

# Set budget limits per category (You can change these)
BUDGET_LIMITS = {
    "Rent": 500,
    "Food": 200,
    "Transport": 150,
    "Entertainment": 50,
    "Utilities": 100,
    "Others": 100
}

def calculate_budget():
    """Calculates remaining budget per category."""
    if not os.path.isfile(DATA_FILE):
        print("No transactions found.")
        return
    
    spent = {category: 0 for category in BUDGET_LIMITS}

    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            _, _, transaction_type, category, amount, _ = row
            if transaction_type == "Expense" and category in spent:
                spent[category] += float(amount)

    print("\nMonthly Budget Status:")
    for category, limit in BUDGET_LIMITS.items():
        remaining = limit - spent[category]
        status = "Within Budget" if remaining >= 0 else "Over Budget!"
        print(f"{category}: ${remaining:.2f} left ({status})")

