from mcp.server.fastmcp import FastMCP
import requests
import yfinance as yf

# 1. Initialize the Server
mcp = FastMCP("FinanceAndMarketAgent")

# 2. Tool: Calculate Return on Investment
@mcp.tool()
def calculate_roi(initial_investment: float, final_value: float) -> str:
    """Calculates the Return on Investment (ROI) for an asset as a percentage."""
    roi = ((final_value - initial_investment) / initial_investment) * 100
    return f"The Return on Investment is {roi:.2f}%"

# 3. Tool: Calculate Compound Interest
@mcp.tool()
def calculate_compound_interest(principal: float, rate: float, years: int) -> str:
    """Calculates the future value of an investment using compound interest."""
    future_value = principal * ((1 + (rate / 100)) ** years)
    return f"The future value after {years} years is ${future_value:,.2f}"

# 4. Tool: Live Cryptocurrency Pricing
@mcp.tool()
def get_live_crypto_price(asset_id: str) -> str:
    """Fetches the current live price of a given cryptocurrency in New Zealand Dollars (NZD)."""
    coin = asset_id.lower()
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=nzd"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if coin in data:
            price = data[coin]["nzd"]
            return f"The current live price of {asset_id} is ${price:,.2f} NZD."
        else:
            return f"Sorry, I couldn't find live data for '{asset_id}'. Please check the coin name."
    except Exception as e:
        return "Error: Could not connect to the live market API."

# 5. Tool: Live Commodities Pricing (Oil)
@mcp.tool()
def get_live_oil_price(oil_type: str) -> str:
    """Fetches the current live price of crude oil per barrel in USD. Valid inputs are 'WTI' or 'Brent'."""
    ticker = "CL=F" if oil_type.upper() == "WTI" else "BZ=F"
    name = "WTI Crude" if oil_type.upper() == "WTI" else "Brent Crude"
    
    try:
        commodity = yf.Ticker(ticker)
        todays_data = commodity.history(period="1d")
        price = todays_data['Close'].iloc[0]
        return f"The current live price of {name} Oil is ${price:.2f} USD per barrel."
    except Exception as e:
        return f"Error: Could not fetch data for {oil_type}. Please ensure you request 'WTI' or 'Brent'."

# 6. Tool: Company News & Sentiment Analysis
@mcp.tool()
def get_company_news(ticker: str) -> str:
    """Fetches the top 5 most recent financial news headlines for a specific company or asset ticker to assist with sentiment analysis."""
    try:
        asset = yf.Ticker(ticker)
        news_items = asset.news
        
        if not news_items:
            return f"No recent news found for {ticker.upper()}."
        
        headlines = []
        for item in news_items[:5]:
            # The yfinance API recently nested news data under a 'content' key
            content = item.get('content', item) 
            title = content.get('title', 'No Title')
            
            # The publisher name is also nested deeper now under 'provider'
            provider = content.get('provider', {}).get('displayName', 'Unknown')
            
            headlines.append(f"- {title} (Source: {provider})")
        
        formatted_news = f"Recent news headlines for {ticker.upper()}:\n" + "\n".join(headlines)
        return formatted_news
    except Exception as e:
        return f"Error fetching news for {ticker}: Please check the ticker symbol."

# 7. Run the server 
if __name__ == "__main__":
    # Testing the APIs before booting the server
    print("\n--- TESTING API CONNECTIONS ---")
    print(get_live_crypto_price("ethereum"))
    print(get_live_oil_price("WTI"))
    print("\n--- TESTING NEWS FETCH ---")
    print(get_company_news("AAPL")) # Fetching Apple news to test
    print("------------------------------\n")
    
    mcp.run()
