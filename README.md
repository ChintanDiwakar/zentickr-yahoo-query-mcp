<div align="center">
  <img src="https://raw.githubusercontent.com/ChintanDiwakar/zentickr-yahoo-query-mcp/refs/heads/main/avatar.png" alt="Zentickr Logo" width="200" height="200" />
</div>

# Zentickr - Yahoo Finance MCP Server

A powerful Model Context Protocol (MCP) server that provides comprehensive access to Yahoo Finance data through the yahooquery library. This server exposes a wide range of financial data, market information, and stock analysis tools that can be integrated with AI assistants and applications.

## ⚠️ Important Disclaimer

**THIS SOFTWARE IS FOR EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY**

Zentickr provides access to financial data and market information but **DOES NOT PROVIDE FINANCIAL ADVICE**. The data, analysis, and insights generated through this server should not be considered as:

- Investment recommendations
- Trading advice
- Financial planning guidance
- Professional financial counsel

**Key Points:**

- All financial data is provided "as-is" without warranties
- Past performance does not guarantee future results
- Always consult with qualified financial professionals before making investment decisions
- Users are solely responsible for their investment and trading decisions
- The authors and contributors are not liable for any financial losses

**Data Accuracy:** While we strive for accuracy, financial data may be delayed, incomplete, or contain errors. Always verify critical information from official sources.

## 🚀 Features

### Core Financial Data

- **Real-time Stock Prices** - Current market prices and trading data
- **Financial Statements** - Income statements, balance sheets, and cash flow statements
- **Company Information** - Detailed company profiles, officers, and business descriptions
- **Historical Data** - Comprehensive historical price data with customizable intervals

### Advanced Analytics

- **Valuation Metrics** - P/E ratios, market cap, enterprise value, and more
- **Earnings Data** - Quarterly and annual earnings with trend analysis
- **Analyst Coverage** - Professional recommendations and price targets
- **Technical Insights** - Technical analysis and market indicators

### Ownership & Governance

- **Institutional Holdings** - Major institutional investors and ownership percentages
- **Insider Information** - Company insider holdings and recent transactions
- **Fund Ownership** - Mutual fund and ETF holdings
- **ESG Scores** - Environmental, Social, and Governance ratings

### Market Intelligence

- **Calendar Events** - Upcoming earnings dates and corporate events
- **Symbol Search** - Find stocks by company name or partial ticker
- **Multiple Timeframes** - Support for various data intervals from 1-minute to monthly

## 🛠️ Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Quick Start

1. **Clone the repository**

   ```bash
   git clone <your-repository-url>
   cd Zentickr
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**

   **Option 1: Using the run scripts (Recommended)**

   The easiest way to run the server is to use the provided run scripts:

   - **Windows**:

     ```bash
     .\run_server.bat
     ```

   - **Unix/Linux/macOS**:
     ```bash
     ./run_server.sh
     ```

   These scripts automatically activate the virtual environment and run the server.

   **Option 2: Manual execution**

   1. Activate the virtual environment:

      ```bash
      source env/bin/activate  # On Windows: env\Scripts\activate
      ```

   2. Run the server:
      ```bash
      python run_server.py
      ```

## 📖 Usage

### Running as MCP Server

The server communicates via stdio transport and can be integrated with MCP-compatible clients:

```bash
python run_server.py
```

## 🎯 Demo & Examples

Here are real working examples showing Zentickr's capabilities:

### 📊 Basic Stock Data Query

**Query:** Get current financial data for Apple, Microsoft, and Google

```python
get_financial_data("AAPL,MSFT,GOOGL")
```

**Sample Response:**

```json
{
  "AAPL": {
    "currentPrice": 189.84,
    "targetHighPrice": 250.0,
    "targetLowPrice": 158.0,
    "targetMeanPrice": 201.32,
    "recommendationMean": 2.1,
    "recommendationKey": "buy",
    "numberOfAnalystOpinions": 35,
    "totalCash": 62639001600,
    "totalDebt": 104590000128,
    "totalRevenue": 394328993792,
    "debtToEquity": 184.37,
    "revenuePerShare": 25.42,
    "returnOnAssets": 0.22689,
    "returnOnEquity": 1.56456,
    "grossProfits": 169148000000,
    "freeCashflow": 84726874112,
    "operatingCashflow": 118287998976,
    "earningsGrowth": 0.11,
    "revenueGrowth": 0.061,
    "grossMargins": 0.45962,
    "ebitdaMargins": 0.33826,
    "operatingMargins": 0.30743
  }
}
```

### 📈 Historical Price Data

**Query:** Get Apple's 6-month daily price history

```python
get_historical_prices("AAPL", period="6mo", interval="1d")
```

**Sample Response:**

```json
[
  {
    "symbol": "AAPL",
    "date": "2024-12-18",
    "open": 188.89,
    "high": 190.32,
    "low": 188.44,
    "close": 189.84,
    "volume": 45234567,
    "adjclose": 189.84
  },
  {
    "symbol": "AAPL",
    "date": "2024-12-17",
    "open": 187.23,
    "high": 189.15,
    "low": 186.98,
    "close": 188.89,
    "volume": 52341789,
    "adjclose": 188.89
  }
]
```

### 🏢 Company Profile & Leadership

**Query:** Get detailed company information for Tesla

```python
get_company_profile("TSLA")
get_company_officers("TSLA")
```

**Sample Response:**

```json
{
  "asset_profile": {
    "TSLA": {
      "address1": "1 Tesla Road",
      "city": "Austin",
      "state": "TX",
      "zip": "78725",
      "country": "United States",
      "phone": "512 516 8177",
      "website": "https://www.tesla.com",
      "industry": "Auto Manufacturers",
      "sector": "Consumer Cyclical",
      "longBusinessSummary": "Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems...",
      "fullTimeEmployees": 140473,
      "companyOfficers": [
        {
          "maxAge": 1,
          "name": "Mr. Elon R. Musk",
          "age": 52,
          "title": "Chief Executive Officer & Director",
          "yearBorn": 1971,
          "fiscalYear": 2023,
          "totalPay": 0,
          "exercisedValue": 0,
          "unexercisedValue": 0
        }
      ]
    }
  }
}
```

### 💰 Financial Statements Analysis

**Query:** Get quarterly income statement for Netflix

```python
get_income_statement("NFLX", frequency="quarterly")
```

**Sample Response:**

```json
[
  {
    "symbol": "NFLX",
    "asOfDate": "2024-09-30",
    "periodType": "3M",
    "TotalRevenue": 9824569000,
    "CostOfRevenue": 5767234000,
    "GrossProfit": 4057335000,
    "OperatingExpense": 2892456000,
    "OperatingIncome": 1164879000,
    "NetIncome": 2364391000,
    "EPS": 5.4,
    "DilutedEPS": 5.38
  }
]
```

### 🎯 Analyst Recommendations

**Query:** Get current analyst recommendations for Amazon

```python
get_recommendations("AMZN")
get_recommendation_trend("AMZN")
```

**Sample Response:**

```json
{
  "recommendations": [
    {
      "firm": "Morgan Stanley",
      "toGrade": "Overweight",
      "fromGrade": "Equal-Weight",
      "action": "up",
      "date": "2024-12-15"
    },
    {
      "firm": "Goldman Sachs",
      "toGrade": "Buy",
      "fromGrade": "Buy",
      "action": "main",
      "date": "2024-12-10"
    }
  ],
  "recommendation_trend": {
    "period": "0m",
    "strongBuy": 15,
    "buy": 25,
    "hold": 8,
    "sell": 1,
    "strongSell": 0
  }
}
```

### 🔍 Symbol Search

**Query:** Search for companies related to "artificial intelligence"

```python
search_symbols("nvidia")
```

**Sample Response:**

```json
[
  {
    "symbol": "NVDA",
    "name": "NVIDIA Corporation",
    "type": "EQUITY",
    "exchange": "NMS"
  },
  {
    "symbol": "NVDL",
    "name": "GraniteShares 1.5x Long NVDA Daily ETF",
    "type": "ETF",
    "exchange": "NMS"
  }
]
```

### 🌱 ESG Scores

**Query:** Get Environmental, Social, and Governance ratings

```python
get_esg_scores("MSFT")
```

**Sample Response:**

```json
{
  "MSFT": {
    "totalEsg": 18.12,
    "environmentScore": 2.89,
    "socialScore": 8.45,
    "governanceScore": 6.78,
    "esgPerformance": "OUTPERFORM",
    "peerCount": 157,
    "peerGroup": "Software",
    "percentile": 8.92,
    "peerEsgScorePerformance": {
      "min": 7.32,
      "avg": 24.56,
      "max": 58.43
    }
  }
}
```

### ⏰ Upcoming Events

**Query:** Get upcoming earnings and events

```python
get_calendar_events("AAPL")
```

**Sample Response:**

```json
{
  "AAPL": {
    "earnings": {
      "earningsDate": ["2025-01-30"],
      "earningsAverage": 2.35,
      "earningsLow": 2.28,
      "earningsHigh": 2.42,
      "revenueAverage": 124500000000,
      "revenueLow": 121200000000,
      "revenueHigh": 127800000000
    },
    "exDividendDate": "2024-11-08",
    "dividendDate": "2024-11-14"
  }
}
```

### 📊 Multiple Stock Comparison

**Query:** Compare key metrics across tech giants

```python
get_valuation_measures("AAPL,MSFT,GOOGL,AMZN,META")
```

**Sample Response:**

```json
{
  "AAPL": {
    "marketCap": 2945234567890,
    "enterpriseValue": 2987654321098,
    "trailingPE": 28.42,
    "forwardPE": 25.67,
    "pegRatio": 2.34,
    "priceToBook": 45.23,
    "priceToSalesTrailing12Months": 7.89
  },
  "MSFT": {
    "marketCap": 2834567890123,
    "enterpriseValue": 2845678901234,
    "trailingPE": 32.15,
    "forwardPE": 28.94,
    "pegRatio": 1.98,
    "priceToBook": 12.45,
    "priceToSalesTrailing12Months": 11.23
  }
}
```

### 🚀 Advanced Usage: Intraday Trading Data

**Query:** Get real-time 5-minute intervals for day trading

```python
get_historical_prices("SPY", period="1d", interval="5m")
```

**Sample Response:**

```json
[
  {
    "symbol": "SPY",
    "date": "2025-06-18 09:30:00-04:00",
    "open": 542.15,
    "high": 542.89,
    "low": 541.78,
    "close": 542.34,
    "volume": 2456789
  },
  {
    "symbol": "SPY",
    "date": "2025-06-18 09:35:00-04:00",
    "open": 542.34,
    "high": 543.12,
    "low": 542.01,
    "close": 542.98,
    "volume": 1987654
  }
]
```

### Available Tools

#### Basic Stock Data

```python
# Get current financial data
get_financial_data("AAPL,GOOGL,MSFT")

# Get current stock prices
get_price_data("AAPL")

# Search for stock symbols
search_symbols("Apple Inc")
```

#### Financial Statements

```python
# Get annual income statement
get_income_statement("AAPL", frequency="annual")

# Get quarterly balance sheet
get_balance_sheet("AAPL", frequency="quarterly")

# Get cash flow statement
get_cash_flow("AAPL", frequency="annual")
```

#### Historical Data

```python
# Get 1-year daily prices
get_historical_prices("AAPL", period="1y", interval="1d")

# Get custom date range
get_historical_prices("AAPL", start_date="2024-01-01", end_date="2024-12-31")

# Get intraday data
get_historical_prices("AAPL", period="1d", interval="5m")
```

#### Company Analysis

```python
# Get company profile and details
get_company_profile("AAPL")

# Get executive team information
get_company_officers("AAPL")

# Get valuation metrics
get_valuation_measures("AAPL")
```

#### Investment Research

```python
# Get analyst recommendations
get_recommendations("AAPL")

# Get earnings data and trends
get_earnings("AAPL")
get_earnings_trend("AAPL")

# Get institutional ownership
get_institution_ownership("AAPL")

# Get ESG scores
get_esg_scores("AAPL")
```

### Supported Data Intervals

- **Intraday**: 1m, 2m, 5m, 15m, 30m, 60m, 90m
- **Daily**: 1d, 5d
- **Weekly**: 1wk
- **Monthly**: 1mo, 3mo

### Supported Time Periods

- **Short-term**: 1d, 5d, 1mo, 3mo, 6mo
- **Long-term**: 1y, 2y, 5y, 10y, max

## 🔧 Configuration

### Environment Setup

The server can be configured through environment variables or by modifying the server configuration:

```python
# In your MCP client configuration
{
  "mcpServers": {
    "zentickr": {
      "command": "python",
      "args": ["path/to/zentickr/run_server.py"],
      "env": {}
    }
  }
}
```

### Integration with Claude Desktop

To use this MCP server with Claude Desktop, add the following configuration to your Claude Desktop config file:

**Option 1: Using the run script (Recommended)**

```json
{
  "mcpServers": {
    "zentickr": {
      "command": "/path/to/Zentickr/run_server.sh" // On Windows: "C:\\path\\to\\Zentickr\\run_server.bat"
    }
  }
}
```

**Option 2: Direct Python execution**

```json
{
  "mcpServers": {
    "zentickr": {
      "command": "python",
      "args": ["/path/to/Zentickr/run_server.py"], // Update with your actual path
      "cwd": "/path/to/Zentickr"
    }
  }
}
```

**Windows Example:**

```json
{
  "mcpServers": {
    "zentickr": {
      "command": "C:\\path\\to\\Zentickr\\run_server.bat"
    }
  }
}
```

## 📊 Data Sources

This server leverages the powerful **yahooquery** library, which provides access to:

- Yahoo Finance real-time and historical data
- Comprehensive financial statements
- Market data and analytics
- Company fundamentals and metrics

All data is sourced from Yahoo Finance and is subject to their terms of service and data usage policies.

## 🏗️ Project Structure

```
Zentickr/
├── src/
│   └── stock_mcp/
│       ├── __init__.py
│       └── server.py          # Main MCP server implementation
├── env/                       # Virtual environment
├── project.toml              # Project configuration
├── requirements.txt          # Python dependencies
├── run_server.py            # Server entry point
├── run_server.bat           # Windows startup script
├── run_server.sh            # Unix startup script
└── README.md               # This file
```

## 🔒 Security & Rate Limiting

- The server respects Yahoo Finance's rate limiting policies
- All data requests are processed asynchronously for optimal performance
- Error handling ensures graceful degradation when data is unavailable
- No API keys required - uses public Yahoo Finance endpoints

## 🤝 Contributing

We welcome contributions to improve Zentickr! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include error handling for external API calls
- Test with multiple stock symbols

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Legal Disclaimer

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The financial data provided through this software is for informational purposes only and should not be considered as financial advice. Users assume all risks associated with the use of this software and any financial decisions made based on the data provided.

## 📞 Support

- **Issues**: Report bugs and request features through GitHub Issues
- **Documentation**: Check the inline documentation in `server.py`
- **Yahoo Finance**: For data-related questions, refer to Yahoo Finance documentation

## 🙏 Acknowledgments

- **yahooquery** - Provides the core Yahoo Finance API integration
- **FastMCP** - Enables easy MCP server implementation
- **pandas** - Powers data manipulation and formatting
- **Yahoo Finance** - The ultimate source of financial data

## 📈 Future Enhancements

- [ ] Real-time streaming data support
- [ ] Advanced charting capabilities
- [ ] Portfolio tracking and analysis
- [ ] Options and derivatives data
- [ ] Cryptocurrency support
- [ ] Market news integration
- [ ] Custom alerts and notifications

---

**Built with ❤️ by [Chintan Diwakar](mailto:chintan.diwakar012@gmail.com)**

_Zentickr - Empowering financial analysis through AI integration_
