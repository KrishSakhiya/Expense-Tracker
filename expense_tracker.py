"""
Expense Tracker - a simple command-line app built with Python and SQLite.
Lets you add expenses, view them, see totals by category, and delete entries.
"""

import sqlite3
from datetime import date

DB_NAME = "expenses.db"


def connect():
    """Open the database and create the table if it doesn't exist yet."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL
        )
        """
    )
    return conn


def add_expense(conn):
    category = input("Category (food, travel, books,anything...): ").strip().lower()
    description = input("Description: ").strip()
    try:
        amount = float(input("Amount (Rs): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if amount <= 0:
        print("Amount must be greater than Zero.")
        return
    conn.execute(
        "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
        (date.today().isoformat(), category, description, amount),
    )
    conn.commit()
    print("Expense added.")


def view_expenses(conn):
    rows = conn.execute(
        "SELECT id, date, category, description, amount FROM expenses ORDER BY date DESC, id DESC"
    ).fetchall()
    if not rows:
        print("No expenses yettt.")
        return
    print(f"\n{'ID':<4}{'Date':<12}{'Category':<12}{'Description':<22}{'Amount':>10}")
    print("-" * 60)
    for row_id, d, cat, desc, amt in rows:
        print(f"{row_id:<4}{d:<12}{cat:<12}{desc[:20]:<22}{amt:>10.2f}")


def category_summary(conn):
    rows = conn.execute(
        "SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC"
    ).fetchall()
    if not rows:
        print("No expenses yet.")
        return
    print("\nSpending by category")
    print("-" * 30)
    for cat, total in rows:
        print(f"{cat:<15}{total:>12.2f}")
    grand_total = sum(total for _, total in rows)
    print("-" * 30)
    print(f"{'TOTAL':<15}{grand_total:>12.2f}")


def delete_expense(conn):
    try:
        expense_id = int(input("Enter the ID to delete: "))
    except ValueError:
        print("Please enter a valid ID number.")
        return
    cur = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    print("Deleted." if cur.rowcount else "No expense found with that ID.")


def main():
    conn = connect()
    menu = {
        "1": ("Add expense", add_expense),
        "2": ("View all expenses", view_expenses),
        "3": ("Spending by category", category_summary),
        "4": ("Delete an expense", delete_expense),
    }
    while True:
        print("\n=== Expense Tracker ===")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice][1](conn)
        else:
            print("Invalid choice, try again.")
    conn.close()


if __name__ == "__main__":
    main()