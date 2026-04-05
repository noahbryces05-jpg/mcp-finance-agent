from mcp.server.fastmcp import FastMCP
import requests

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

# 5. Run the server (with a test print right before it)
if __name__ == "__main__":
    # This line tests the API to prove it works before starting the server
    print("\n--- TESTING API CONNECTION ---")
    print(get_live_crypto_price("ethereum"))
    print("------------------------------\n")
    
    # This line officially starts the MCP server
    mcp.run()