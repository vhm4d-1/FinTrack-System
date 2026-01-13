import re
import pandas as pd
import os

class TransactionParser:
    """
    Automated parser to convert Banking SMS logs into 
    structured financial data using Regular Expressions.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = []
        
        # Category Map (Can be expanded)
        self.category_map = {
            # Education
            'SCHOOL': 'Education', 'UNIVERSITY': 'Education', 'ACADEMY': 'Education', 'COURSERA': 'Education',
            'EDX': 'Education', 'UDEMY': 'Education',
            
            # Fuel & Transport
            'SHELL': 'Fuel', 'PSO': 'Fuel', 'TOTAL': 'Fuel', 'PARCO': 'Fuel', 
            'BYKEA': 'Transport', 'UBER': 'Transport', 'INDRIVE': 'Transport', 
            'CAREEM': 'Transport', 'AIRBLUE': 'Transport',
            
            # Food & Dining
            'FOODPANDA': 'Food', 'MCDONALDS': 'Food', 'SAVOUR': 'Food', 'KFC': 'Food', 
            'HARDDEES': 'Food', 'SUBWAY': 'Food', 'RESTAURANT': 'Food', 'CAFE': 'Food',
            
            # Shopping & E-Commerce
            'DARAZ': 'Shopping', 'ELO': 'Shopping', 'GUL AHMED': 'Shopping', 'KHAADI': 'Shopping', 
            'ALFATAH': 'Shopping', 'CARREFOUR': 'Shopping', 'STORES': 'Shopping',
            
            # Health & Utilities
            'PHARMACY': 'Health', 'HOSPITAL': 'Health', 'MEDICAL': 'Health',
            'LESCO': 'Utilities', 'SNGPL': 'Utilities', 'PTCL': 'Utilities', 'STORM FIBER': 'Utilities'
        }

    def parse_logs(self):
        """
        Processes the text file and extracts transaction details.
        """
        print(f"--- System: Reading logs from {self.file_path} ---")
        
        if not os.path.exists(self.file_path):
            print(f"Error: File '{self.file_path}' does not exist.")
            return pd.DataFrame()

        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    # Regex explanation:
                    # Rs\.\s?([\d,]+\.\d+) -> Captures digits and commas (e.g., 45,000.00)
                    # spent at\s([\w\s]+)\son -> Captures the vendor name until the word 'on'
                    # ([\d]{2}-[A-Z]{3}) -> Captures the date (e.g., 02-OCT)
                    match = re.search(r"Rs\.\s?([\d,]+\.\d+)\sspent at\s([\w\s]+)\son\s([\d]{2}-[A-Z]{3})", line)
                    
                    if match:
                        # 1. Clean and convert Amount
                        amount_str = match.group(1).replace(',', '')
                        amount = float(amount_str)
                        
                        # 2. Extract and clean Vendor
                        vendor = match.group(2).strip()
                        
                        # 3. Extract Date
                        date = match.group(3)
                        
                        # 4. Categorization Logic
                        category = 'Other'
                        for key in self.category_map:
                            if key in vendor.upper():
                                category = self.category_map[key]
                                break
                        
                        self.transactions.append({
                            'Date': date,
                            'Vendor': vendor,
                            'Amount': amount,
                            'Category': category
                        })
            
            df = pd.DataFrame(self.transactions)
            print(f"--- System: Successfully processed {len(df)} transactions ---")
            return df
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return pd.DataFrame()