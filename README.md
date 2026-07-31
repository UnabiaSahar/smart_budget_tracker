# Smart Budget Tracker

A simple command-line budget tracking application built with Python and pandas.

## Features

- Add expenses with date, category, amount, and description
- View monthly summaries grouped by category
- Data stored locally as a CSV file in the `data/` directory

## Requirements

- Python 3.x
- pandas

Install dependencies:

```bash
pip install pandas
```

## Usage

Run the application:

```bash
python main.py
```

Available options:

1. Add Expense
2. View Monthly Summary
3. View Valid Categories
4. Exit

## Categories

Valid expense categories: Food, Transport, Entertainment, Utilities, Misc

## Data Storage

Expense data is saved to `data/budget_data.csv`. This directory is excluded from version control (see `.gitignore`).
