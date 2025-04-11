import csv
import os
import matplotlib.pyplot as plt
from collections import defaultdict

DATA_FILE = "../data/transactions.csv"

def expense_pie_chart():
    """Shows a pie chart of expenses by category."""
    if not os.path.exists(DATA_FILE):
        print("⚠ No transaction data available.")
        return

    category_totals = defaultdict(float)

    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            _, _, transaction_type, category, amount, _ = row
            if transaction_type == "Expense":
                category_totals[category] += float(amount)

    if not category_totals:
        print("⚠ No expense data found.")
        return

    labels = category_totals.keys()
    sizes = category_totals.values()

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Expenses by Category")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

def savings_line_graph():
    """Displays a line graph of cumulative savings over time."""
    if not os.path.exists(DATA_FILE):
        print("⚠ No transaction data available.")
        return

    dates = []
    savings = []
    total_income = 0
    total_expense = 0

    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            date, _, transaction_type, _, amount, _ = row
            amount = float(amount)
            if transaction_type == "Income":
                total_income += amount
            elif transaction_type == "Expense":
                total_expense += amount

            current_savings = total_income - total_expense
            dates.append(date)
            savings.append(current_savings)

    if not dates:
        print("⚠ No transactions found to display.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(dates, savings, marker="o")
    plt.title("Savings Over Time")
    plt.xlabel("Date")
    plt.ylabel("Savings ($)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
