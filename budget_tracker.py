import os
from pathlib import Path
import pandas as pd
from datetime import datetime

class BudgetTracker:
    def __init__(self, dir = "data", file_name = "budget_data.csv"):
        self.dir = Path(dir)
        self.file_path = self.dir / file_name
        self.columns = ['Timestamp', 'Date', 'Category', 'Amount', 'Description']
        self.categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Misc']

        self.__init__storage()

    def __init__storage(self):
        self.dir.mkdir(exist_ok=True)
        if not self.file_path.exists():
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.file_path, index=False)
    def load_data(self)-> pd.DataFrame:
        df = pd.read_csv(self.file_path)
        df["Amount"] = pd.to_numeric(df["Amount"], errors='coerce').fillna(0.0)
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        return df

    def add_expense(self, date: str, category:str, amount: float, description: str)->bool:
        if category not in self.categories:
            raise ValueError(f"Invalid category. Choose from: {', '.join(self.categories)}")

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            
        new_expense = {
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Date': date,
            'Category': category,
            'Amount': amount,
            'Description': description
        }

        df = self.load_data()
        df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
        df.to_csv(self.file_path, index=False)
        return True

    def monthly_summary(self, year: int, month: int):
        df = self.load_data()
        if df.empty:
            return None, 0.0

        mask = (df['Date'].dt.year == year) & (df['Date'].dt.month == month)
        monthly_data = df[mask]
        if monthly_data.empty:
            return None, 0.0

        total_expense = monthly_data['Amount'].sum()
        summary = monthly_data.groupby('Category')['Amount'].agg(['sum', 'count']).rename(columns={'sum': 'Total Amount', 'count': 'Transactions'})

        return summary, total_expense