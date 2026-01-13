fimport sys
import os

try:
    from src.parser import TransactionParser
    from src.generator import ReportGenerator
except ImportError:
    print("Error: Could not find the 'src' folder or its files.")
    print("Ensure you have __init__.py in the src directory.")
    sys.exit(1)

def run_fintrack_pipeline():
    """
    This is the main orchestrator function that connects the 
    Parsing logic with the PDF Generation logic.
    """
    print("==========================================")
    print("   FinTrack: Expense Analytics System     ")
    print("==========================================")

    # Defining paths
    data_file = "data/sms_logs.txt"
    report_name = "Final_Spending_Report.pdf"

    # STEP 1: PARSING
    print("\n[Step 1] Initializing Data Parser...")
    parser = TransactionParser(data_file)
    df = parser.parse_logs()

    # Checking if the dataframe has data
    if df.empty:
        print("\n[!] Technical Alert: No transactions were extracted.")
        print("Please ensure 'sms_logs.txt' follows the bank format.")
        return

    # STEP 2: ANALYTICS & VISUALS
    print("\n[Step 2] Processing Analytics and Generating Charts...")
    generator = ReportGenerator(df)
    
    chart_success = generator.create_visuals()
    
    if not chart_success:
        print("[!] Error: Failed to generate the data visualization.")
        return

    # STEP 3: PDF EXPORT
    print(f"\n[Step 3] Exporting results to {report_name}...")
    try:
        generator.generate_pdf(report_name)
        print("\n[Success] Report generated successfully!")
        print(f"Location: {os.path.abspath(report_name)}")
    except Exception as e:
        print(f"\n[!] PDF Error: An error occurred during export: {e}")

    print("\n==========================================")
    print("       Process Execution Finished         ")
    print("==========================================")

if __name__ == "__main__":
    # Wrap in a try-block to catch keyboard interruptions 
    try:
        run_fintrack_pipeline()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")