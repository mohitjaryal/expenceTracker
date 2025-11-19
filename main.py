import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Helper functions 

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'description', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (food, transport, etc.): ").strip()
    description = input("Enter description: ").strip()
    amount = input("Enter amount (₹): ").strip()

    expense = {'date': date, 'category': category, 'description': description, 'amount': amount}
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n📋 Expense List:")
    print("-" * 50)
    total = 0
    for e in expenses:
        print(f"{e['date']} | {e['category']:<10} | {e['description']:<20} | ₹{e['amount']}")
        total += float(e['amount'])
    print("-" * 50)
    print(f"Total: ₹{total:.2f}\n")

def search_by_category():
    category = input("Enter category to search: ").strip().lower()
    expenses = load_expenses()
    results = [e for e in expenses if e['category'].lower() == category]
    if results:
        print(f"\nExpenses in '{category}':")
        for e in results:
            print(f"{e['date']} | {e['description']} | ₹{e['amount']}")
    else:
        print("No expenses found for that category.")

# Main program loop 

def main():
    while True:
        print("\nExpense Tracker (₹) ")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_by_category()
        elif choice == '4':
            print("Goodbye! ")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
