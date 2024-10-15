import yfinance as yf
import matplotlib.pyplot as plt

def calculate_percentage_change(current, previous):
    """Calculate percentage change between two periods"""
    if previous == 0:
        return 0
    return ((current - previous) / previous) * 100

def plot_financial_metrics(symbol):
    """Fetch financial data and plot percentage changes for key metrics over time"""
    stock = yf.Ticker(symbol)

    # Fetch financial reports: quarterly financials, balance sheet, and cashflow
    financials = stock.quarterly_financials
    balance_sheet = stock.quarterly_balance_sheet
    cashflow = stock.quarterly_cashflow

    # Adjust the keys based on the inspection
    metrics = {
        "Revenue": financials.loc['Total Revenue'],
        "Net Income": financials.loc['Net Income'],
        "Operating Cash Flow": cashflow.loc['Operating Cash Flow'],  # Adjust based on actual key
        "Total Debt": balance_sheet.loc['Total Debt']
    }

    # Calculate percentage changes for each metric
    percentage_changes = {metric: [] for metric in metrics}

    for metric, values in metrics.items():
        for i in range(1, len(values)):
            current = values[i]
            previous = values[i - 1]
            percentage_change = calculate_percentage_change(current, previous)
            percentage_changes[metric].append(percentage_change)

    # Plot percentage changes over time
    plt.figure(figsize=(12, 8))

    for metric, changes in percentage_changes.items():
        plt.plot(financials.columns[1:], changes, label=metric)  # Skip the first column since it doesn't have a percentage change

    plt.title(f'Percentage Changes in Key Financial Metrics for {symbol}')
    plt.xlabel('Quarter')
    plt.ylabel('Percentage Change (%)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example usage
symbol = "AAPL"  # Apple
plot_financial_metrics(symbol)

symbol = "AAPL"  # Apple
get_earnings_sentiment(symbol)
