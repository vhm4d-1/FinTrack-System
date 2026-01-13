# FinTrack: Automated Expense Analyzer for Pakistani Banking

## Project Overview
FinTrack is a financial literacy tool built in Python to solve a common problem in the Pakistani banking ecosystem: the lack of integrated, visual spending analytics in local banking apps. 

While most banks provide transaction alerts via SMS, they do not offer a consolidated view of spending habits. This project automates the extraction of data from these unstructured text alerts, categorizes expenses, and generates a professional PDF financial report.

## Key Features
- **Regex Parsing Engine:** Uses Python's `re` module to identify and extract currency, vendor names, and dates from unstructured bank SMS strings.
- **Automated Categorization:** Employs a mapping logic to sort transactions into categories such as *Education*, *Fuel*, *Food*, and *Shopping*.
- **Data Visualization:** Utilizes `Matplotlib` to generate a pie chart distribution of expenses.
- **PDF Generation:** Compiles findings into a portable `Financial_Report.pdf` using the `ReportLab` library.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Data Handling:** Pandas
- **Visualization:** Matplotlib
- **Reporting:** ReportLab
- **Architecture:** Modular, Object-Oriented Programming (OOP)

## 📂 Project Structure
```text
D:/python/
├── main.py               # The orchestrator script
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── data/
│   └── sms_logs.txt      # Input data (Bank SMS formats)
└── src/
    ├── __init__.py       # Package marker
    ├── parser.py         # Regex and Categorization logic
    └── generator.py      # Charting and PDF logic