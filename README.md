# smartstock-investment-analysis
Educational Python stock analysis tool that generates company metrics, investment scores, and price charts for research purposes.
# SmartStock Analyzer: Investment Research Dashboard

SmartStock Analyzer is an educational Python project that allows users to enter a stock ticker symbol and generate a beginner-friendly investment research summary.

The project analyzes company information, valuation metrics, profitability, revenue growth, debt levels, analyst target price, and historical stock performance using Python.

This project was created as part of my learning journey in Data Science, business analytics, and investment research.

## Project Purpose

The goal of this project is to practice using Python for financial data analysis and to better understand the types of metrics investors may review when analyzing a public company.

The project is designed for educational purposes only and does not provide financial advice, buy/sell recommendations, or investment recommendations.

## Features

- Search a company by stock ticker symbol
- Display company overview information
- Show key investment metrics
- Analyze valuation, profitability, growth, and debt levels
- Generate an educational investment quality score
- Create a simple written analysis summary
- Generate a 1-year stock price chart
- Display 50-day and 200-day moving averages
- Save the generated chart as an image file

## Tools and Technologies Used

- Python
- yfinance
- pandas
- matplotlib
- VS Code
- GitHub

## Metrics Analyzed

The project uses publicly available financial data to display metrics such as:

- Current stock price
- Market capitalization
- P/E ratio
- Forward P/E ratio
- Profit margin
- Revenue growth
- Dividend yield
- Debt-to-equity ratio
- 52-week high and low
- Analyst target price

## Educational Investment Quality Score

The project calculates a simple educational score based on selected financial metrics:

- Valuation
- Profitability
- Revenue growth
- Debt levels

The score is not a recommendation. It is only a simplified way to practice comparing company fundamentals.

## Example Use Case

A user can enter a stock ticker such as:

```text
NVDA
