print("=" * 40)
print("💰 Personal Finance Tracker 💰")
print("=" * 40)

transactions = []

def add_transaction():
    print("\n💰 Add Transaction 💰\n")
    income_or_expense = input("💰 Is this an ➕ Income or ⬛ Expense? (i/e): ")
    amount = float(input("💰 Enter the amount (₹): "))
    category = input("💰 Enter the category: ")
    transaction = {"amount": amount, "category": category, "income_or_expense": income_or_expense}  
    transactions.append(transaction)
    print(f"💰 Transaction added successfully! 💰")

def view_transactions():
    print("\n💰 View Transactions 💰\n")
    for transaction in transactions:
        print(f"💰 {transaction['amount']} - {transaction['category']}")

def view_summary():
    print("\n💰 View Summary 💰")
    total_income = sum(transaction["amount"] for transaction in transactions if transaction["income_or_expense"] == "i")
    total_expenses = sum(transaction["amount"] for transaction in transactions if transaction["income_or_expense"] == "e")
    net_balance = total_income + total_expenses

    print(f"💰 Total Income: ₹{total_income:.2f}")
    print(f"💰 Total Expenses: ₹{abs(total_expenses):.2f}")
    print(f"💰 Net Balance: ₹{net_balance:.2f}")

def main():
    print("\n💰 Welcome to the Personal Finance Tracker! 💰")
    print("💰 Track your income, expenses, and savings with ease! 💰")

    while True:
        print("\n💰 Main Menu 💰")
        print("1. 📝 Add Transaction")
        print("2. 🗒️ View Transactions")
        print("3. 📊 View Summary")
        print("4. 🚪 Exit")

        choice = input("💰 Enter your choice (1-4): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("💰 Thank you for using the Personal Finance Tracker! 💰")
            break

if __name__ == "__main__":
    main()
