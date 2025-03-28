from tracker import add_transaction, view_transactions, EXPENSE_CATEGORIES, INCOME_CATEGORIES
from budget import calculate_budget
from savings import set_savings_goal, check_savings_progress


# Main function to run program
def main():
    while True:
        # Show menu options
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Budget Status")
        print("5. Set Savings Goal")
        print("6. View Savings Progress")
        print("7. Exit")
        
        # Get user input. it is for menu selection
        choice = input("Choose an option: ")

      # Add income transaction
        if choice == "1": 
            print(f"Available Income Categories: {', '.join(INCOME_CATEGORIES)}")
            # Income source
            category = input("Select category: ") 
            # Income amount
            amount = input("Enter amount: ") 
            # Call function to add income
            add_transaction("Income", category, amount)  

      # Add expense transaction
        elif choice == "2":  
            print(f"Available Expense Categories: {', '.join(EXPENSE_CATEGORIES)}")
            # Expense category
            category = input("Select category: ")  
            # Expense amount
            amount = input("Enter amount: ")  
            # Optional description
            description = input("Enter description (optional): ") 
            # Call the function to add expense
            add_transaction("Expense", category, amount, description) 

      # View all transactions
        elif choice == "3":  
            view_transactions()  

        elif choice == "4":
            calculate_budget()
            
        elif choice == "5":
            goal = input("Enter your savings goal amount: ")
            set_savings_goal(goal)

        elif choice == "6":
            check_savings_progress()

        elif choice == "7":
            print("Exiting... Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
          
# Run the program if executed as the main script
if __name__ == "__main__":
    main()