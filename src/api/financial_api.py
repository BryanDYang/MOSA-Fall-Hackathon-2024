import yfinance as yf

def get_financial_data(ticker):
    """Fetch financial data for a given ticker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            "ticker": ticker,
            "market_cap": info.get("marketCap"),
            "revenue": info.get("totalRevenue"),
            "earnings_growth": info.get("earningsGrowth"),
            "dividend_yield": info.get("dividendYield")
        }
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    financial_data = get_financial_data("AAPL")
    print("Financial Data:", financial_data)
