import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def format_currency(value):
    if value is None or value == "N/A":
        return "N/A"

    try:
        value = float(value)

        if value >= 1_000_000_000_000:
            return f"${value / 1_000_000_000_000:.2f}T"
        elif value >= 1_000_000_000:
            return f"${value / 1_000_000_000:.2f}B"
        elif value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"
        else:
            return f"${value:,.2f}"
    except:
        return "N/A"


def format_percentage(value):
    if value is None or value == "N/A":
        return "N/A"

    try:
        return f"{value * 100:.2f}%"
    except:
        return "N/A"


def format_number(value):
    if value is None or value == "N/A":
        return "N/A"

    try:
        return f"{float(value):,.2f}"
    except:
        return "N/A"


def get_score(pe_ratio, profit_margin, revenue_growth, debt_to_equity):
    score = 0

    # Valuation score
    if pe_ratio is not None:
        if pe_ratio < 20:
            score += 25
        elif pe_ratio < 35:
            score += 18
        elif pe_ratio < 50:
            score += 10
        else:
            score += 5

    # Profitability score
    if profit_margin is not None:
        if profit_margin > 0.20:
            score += 25
        elif profit_margin > 0.10:
            score += 18
        elif profit_margin > 0.05:
            score += 10
        else:
            score += 5

    # Growth score
    if revenue_growth is not None:
        if revenue_growth > 0.15:
            score += 25
        elif revenue_growth > 0.07:
            score += 18
        elif revenue_growth > 0:
            score += 10
        else:
            score += 5

    # Debt score
    if debt_to_equity is not None:
        if debt_to_equity < 50:
            score += 25
        elif debt_to_equity < 100:
            score += 18
        elif debt_to_equity < 200:
            score += 10
        else:
            score += 5

    return score


def score_interpretation(score):
    if score >= 80:
        return "Strong fundamentals based on the selected metrics."
    elif score >= 60:
        return "Moderate fundamentals with some strengths and risks."
    elif score >= 40:
        return "Mixed fundamentals. More research would be needed."
    else:
        return "Weak fundamentals based on the selected metrics."


def analyze_stock(ticker_symbol):
    print("\nSmartStock Analyzer")
    print("-------------------")
    print("Educational stock analysis tool. This is not financial advice.\n")

    stock = yf.Ticker(ticker_symbol)
    info = stock.info

    if not info or "longName" not in info:
        print("Could not find reliable information for this ticker.")
        return

    company_name = info.get("longName")
    sector = info.get("sector")
    industry = info.get("industry")
    current_price = info.get("currentPrice")
    market_cap = info.get("marketCap")
    pe_ratio = info.get("trailingPE")
    forward_pe = info.get("forwardPE")
    profit_margin = info.get("profitMargins")
    revenue_growth = info.get("revenueGrowth")
    dividend_yield = info.get("dividendYield")
    debt_to_equity = info.get("debtToEquity")
    fifty_two_week_high = info.get("fiftyTwoWeekHigh")
    fifty_two_week_low = info.get("fiftyTwoWeekLow")
    target_price = info.get("targetMeanPrice")

    print("Company Overview")
    print("----------------")
    print(f"Ticker: {ticker_symbol}")
    print(f"Company Name: {company_name}")
    print(f"Sector: {sector}")
    print(f"Industry: {industry}")

    print("\nKey Investment Metrics")
    print("----------------------")
    print(f"Current Price: {format_currency(current_price)}")
    print(f"Market Cap: {format_currency(market_cap)}")
    print(f"P/E Ratio: {format_number(pe_ratio)}")
    print(f"Forward P/E: {format_number(forward_pe)}")
    print(f"Profit Margin: {format_percentage(profit_margin)}")
    print(f"Revenue Growth: {format_percentage(revenue_growth)}")
    print(f"Dividend Yield: {format_percentage(dividend_yield)}")
    print(f"Debt-to-Equity: {format_number(debt_to_equity)}")
    print(f"52-Week High: {format_currency(fifty_two_week_high)}")
    print(f"52-Week Low: {format_currency(fifty_two_week_low)}")
    print(f"Analyst Target Price: {format_currency(target_price)}")

    score = get_score(pe_ratio, profit_margin, revenue_growth, debt_to_equity)

    print("\nEducational Investment Quality Score")
    print("------------------------------------")
    print(f"Score: {score}/100")
    print(score_interpretation(score))

    print("\nSimple Analysis Summary")
    print("-----------------------")

    if pe_ratio is not None:
        if pe_ratio > 40:
            print("- The company appears highly valued based on its P/E ratio.")
        elif pe_ratio > 25:
            print("- The company has a moderate-to-high valuation.")
        else:
            print("- The company has a relatively lower valuation based on P/E ratio.")

    if profit_margin is not None:
        if profit_margin > 0.20:
            print("- Profit margins are strong, which may suggest good profitability.")
        elif profit_margin > 0.10:
            print("- Profit margins are reasonable.")
        else:
            print("- Profit margins are low, which may require more research.")

    if revenue_growth is not None:
        if revenue_growth > 0.10:
            print("- Revenue growth appears strong.")
        elif revenue_growth > 0:
            print("- Revenue is growing, but at a moderate pace.")
        else:
            print("- Revenue growth is negative, which may be a risk factor.")

    if debt_to_equity is not None:
        if debt_to_equity > 150:
            print("- Debt levels appear high based on debt-to-equity.")
        elif debt_to_equity > 75:
            print("- Debt levels are moderate.")
        else:
            print("- Debt levels appear relatively controlled.")

    print("\nHistorical Price Chart")
    print("----------------------")

    historical_data = stock.history(period="1y")

    if historical_data.empty:
        print("No historical data available.")
    else:
        historical_data["50-Day Moving Average"] = historical_data["Close"].rolling(window=50).mean()
        historical_data["200-Day Moving Average"] = historical_data["Close"].rolling(window=200).mean()

        plt.figure(figsize=(10, 6))
        plt.plot(historical_data.index, historical_data["Close"], label="Closing Price")
        plt.plot(historical_data.index, historical_data["50-Day Moving Average"], label="50-Day Moving Average")
        plt.plot(historical_data.index, historical_data["200-Day Moving Average"], label="200-Day Moving Average")

        plt.title(f"{ticker_symbol} Stock Price - 1 Year")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)

        chart_filename = f"{ticker_symbol}_stock_chart.png"
        plt.savefig(chart_filename)
        plt.show()

        print(f"Chart saved as: {chart_filename}")

    print("\nFinal Note")
    print("----------")
    print("This project is for educational and data analysis purposes only.")
    print("It does not provide financial advice or buy/sell recommendations.")


def main():
    ticker_symbol = input("Enter a stock ticker symbol, for example MSFT, AAPL, NVDA, or TSLA: ")
    ticker_symbol = ticker_symbol.upper().strip()

    if ticker_symbol == "":
        print("Please enter a valid ticker symbol.")
        return

    analyze_stock(ticker_symbol)


if __name__ == "__main__":
    main()
