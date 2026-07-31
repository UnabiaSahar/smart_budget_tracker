import sys
from budget_tracker import BudgetTracker

def print_header(title):
    print("="*50)
    print(f"{title:^50}")
    print("="*50)

def main():
    print_header("Welcome to the Budget Tracker")
    tracker = BudgetTracker()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Valid Categories")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            print_header("Add Expense")
            try:    
                date = input("Enter date (YYYY-MM-DD): ")
                category = input(f"Enter category ({', '.join(tracker.categories)}): ")
                amount = float(input("Enter amount: ").strip())
                description = input("Enter description: ")

            
                tracker.add_expense(date, category, amount, description)
                print("Expense added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            print_header("View Monthly Summary")
            try:
                year = int(input("Enter year (YYYY): "))
                month = int(input("Enter month (MM): "))

                summary, total_expense = tracker.monthly_summary(year, month)
                if summary is None:
                   print(f"No expenses found for {year}-{month:02d}.")
                else:
                   print(f"\nMonthly Summary for {year}-{month:02d}:")
                   print(summary)
                   print(f"Total Expense: {total_expense:.2f}")
            except ValueError:
                print("Invalid input. Please enter valid year and month.")

        elif choice == '3':
            print_header("Valid Categories")
            print(f"Valid Categories: {', '.join(tracker.categories)}")

        elif choice == '4':
            print("Exiting the Budget Tracker. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    