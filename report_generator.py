# report_generator.py
# A script to automatically analyze transaction data and generate a PDF summary report.

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime

# --- Configuration ---
# Define filenames and settings here for easy modification.
INPUT_CSV_FILE = 'transactions.csv'
CHART_OUTPUT_FILE = 'expense_chart.png'


def analyze_data(csv_path):
    """Reads the CSV and calculates key financial metrics."""
    print("Reading and analyzing data...")
    df = pd.read_csv(csv_path)

    # Calculate totals
    total_revenue = df[df['Type'] == 'Revenue']['Amount'].sum()
    total_expenses = df[df['Type'] == 'Expense']['Amount'].sum()
    net_profit = total_revenue - total_expenses

    # We'll return the calculated data and the DataFrame for use in other functions.
    financial_data = {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "net_profit": net_profit
    }
    return financial_data, df


def create_visual(data_frame, output_path):
    """Generates and saves a bar chart of expenses by category."""
    print(f"Creating visual and saving to {output_path}...")

    # Isolate and group expense data
    expense_by_category = data_frame[data_frame['Type'] == 'Expense'].groupby('Category')['Amount'].sum()

    # Create the plot
    plt.figure(figsize=(10, 6))
    expense_by_category.plot(kind='bar', color='skyblue')
    plt.title('Expenses by Category')
    plt.ylabel('Amount ($)')
    plt.xlabel('Category')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjusts plot to ensure everything fits without overlapping

    # Save the figure to a file
    plt.savefig(output_path)
    plt.close()  # Close the plot to free up memory


def create_pdf(financial_data, chart_path):
    """Creates a PDF report with the financial summary and the expense chart."""
    report_date = datetime.now().strftime("%Y-%m-%d")
    pdf_filename = f"Financial_Report_{report_date}.pdf"
    print(f"Generating PDF report: {pdf_filename}...")

    pdf = FPDF()
    pdf.add_page()

    # --- Report Header ---
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 20, f"Financial Report - {report_date}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    # --- Financial Summary ---
    pdf.set_font('Arial', '', 16)
    pdf.cell(0, 15, f"Total Revenue: ${financial_data['total_revenue']:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 15, f"Total Expenses: ${financial_data['total_expenses']:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 15, f"Net Profit: ${financial_data['net_profit']:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(10)  # Add a little vertical space before the chart

    # --- Chart Section ---
    pdf.image(chart_path, x=10, y=None, w=190)

    # Save the final PDF
    pdf.output(pdf_filename)
    print("Report generation complete.")


def main():
    """Main function to orchestrate the report generation process."""
    try:
        # Step 1: Analyze the data from the CSV
        financial_summary, df = analyze_data(INPUT_CSV_FILE)

        # Step 2: Create the chart based on the data
        create_visual(df, CHART_OUTPUT_FILE)

        # Step 3: Combine the summary and chart into a PDF
        create_pdf(financial_summary, CHART_OUTPUT_FILE)

    except FileNotFoundError:
        print(f"Error: Input file '{INPUT_CSV_FILE}' not found. Please ensure it is in the same directory.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# This is a standard Python convention to make the script runnable.
if __name__ == "__main__":
    main()