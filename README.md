# Automated Financial Report Generator

A Python script that automatically reads financial transaction data from a CSV file, performs a basic analysis, and generates a polished PDF report with a summary and a visual chart.



## Overview

This project is designed to automate the repetitive task of creating simple financial summaries. It's a practical demonstration of data analysis with Pandas, visualization with Matplotlib, and report generation with FPDF2. It serves as an excellent portfolio piece for showcasing core Python skills in a business context.

## Features

-   **Data Analysis**: Calculates total revenue, total expenses, and net profit from a list of transactions.
-   **Data Visualization**: Generates a bar chart visualizing expenses broken down by category.
-   **PDF Generation**: Compiles the financial summary and the chart into a clean, professional PDF document.
-   **Human-Readable Code**: Structured with clear functions and comments for easy understanding and maintenance.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.x
-   Git

### Installation

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/YourUsername/Financial-Report-Generator.git](https://github.com/YourUsername/Financial-Report-Generator.git)
    cd Financial-Report-Generator
    ```

2.  **Create and activate a virtual environment**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1.  **Prepare your data**: Make sure you have a `transactions.csv` file in the project root directory. The file must contain `Type`, `Category`, and `Amount` columns. An example format is:
    ```csv
    Date,Type,Category,Amount
    2025-08-01,Expense,Office Supplies,150
    2025-08-02,Revenue,Client A,2500
    ```
2.  **Run the script**: Execute the main script from your terminal.
    ```sh
    python report_generator.py
    ```

The script will then generate a chart image (`expense_chart.png`) and your final PDF report in the same directory.

## Sample Output

After running the script, you will find a PDF file named `Financial_Report_YYYY-MM-DD.pdf`. The report will contain:

-   A clear title with the date of generation.
-   A summary of total revenue, expenses, and net profit.
-   The bar chart visualizing expenses by category.
