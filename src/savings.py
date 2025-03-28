import csv
import os

DATA_FILE = "../data/transactions.csv"
GOAL_FILE = "../data/savings_goal.txt"

def set_savings_goal(goal_amount):
    with open(GOAL_FILE, "w") as file:
        file.write(str(goal_amount))
    print(f"Savings goal of ${goal_amount} set successfully!")

def check_savings_progress():
    if not os.path.exists(GOAL_FILE):
        print("No savings goal set yet.")
        return

    with open(GOAL_FILE, "r") as file:
        goal = float(file.read())

    total_income = 0
    total_expense = 0

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                _, _, transaction_type, _, amount, _ = row
                amount = float(amount)
                if transaction_type == "Income":
                    total_income += amount
                elif transaction_type == "Expense":
                    total_expense += amount

    savings = total_income - total_expense
    remaining = goal - savings

    print("\nSavings Progress:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Current Savings: ${savings:.2f}")
    print(f"Savings Goal: ${goal:.2f}")
    print(f"Amount Left to Reach Goal: ${remaining:.2f}" if remaining > 0 else " Goal reached!")

