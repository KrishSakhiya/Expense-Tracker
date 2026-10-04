# Expense Tracker (Python + SQLite)

A simple command-line app to track daily expenses.

## Features
- Add an expense with category, description and amount
- View all expenses, newest first
- See total spending by category
- Delete an expense by ID
- Data is stored in a local SQLite database

## Tech used
- Python 3
- SQLite (built into Python, no installation needed)
- Jupyter Notebook (to run and test)

## How to run
Requires Python 3.8 or newer. No extra libraries are needed.

Option 1 - Terminal:

    python expense_tracker.py

Option 2 - Jupyter Notebook:

    %run expense_tracker.py

Choose an option from the menu (1 to 5). Choose 5 to exit.

## What I practiced
- Python functions, loops, dictionaries and input validation
- SQL: CREATE TABLE, INSERT, SELECT, GROUP BY, DELETE
- Using parameterized queries to keep SQL safe
- Git and GitHub for version control

## Ideas to extend
- Filter expenses by month
- Export expenses to CSV
- Set a monthly budget with a warning
