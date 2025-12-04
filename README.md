# E-Commerce Data Analysis Project

This project analyzes e-commerce transaction data to generate insights and reports for business intelligence. It uses Python and pandas to process the data and exports results to CSV files for further use, including Power BI dashboards.

## Project Structure

- `data/` — Contains the raw e-commerce data (`E-Commerce.csv`).
- `scripts/` — Python and shell scripts for data cleaning and analysis.
- `reports/exports/` — Generated CSV reports from analysis scripts.
- `reports/powerbi_dashboard.pbix/` — Power BI dashboard files.

## Key Analyses

The main script (`scripts/clean_e-commerce.sh`) performs:
- Most popular products
- Countries with highest number of orders
- Total revenue by country
- Top customers by purchases
- Yearly sales trends
- Top products by sales
- Order cancellations and returns
- Top-selling products
- Total amount spent by each customer
- Monthly sales trends

## How to Run

1. Ensure you have Python and pandas installed.
2. Place the raw data file in the `data/` folder.
3. Run the analysis script:
   ```bash
   python scripts/clean_e-commerce.sh
   ```
4. Find the generated reports in `reports/exports/`.

## Requirements

- Python 3.x
- pandas

## Visualization

Use the Power BI dashboard in `reports/powerbi_dashboard.pbix/` for interactive data exploration.

## License

This project is for educational and analytical purposes.
