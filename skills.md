# Agent Skills Document

This repository contains a local Model Context Protocol (MCP) server designed to augment AI models with deterministic financial math and live market data.

## Engineered Capabilities
This agent exposes the following tools via FastMCP:

1. **`calculate_roi`**: Bypasses LLM math hallucination by calculating exact Return on Investment percentages based on initial and final values.
2. **`calculate_compound_interest`**: Projects future asset valuation using standard compounding formulas.
3. **`get_live_crypto_price`**: Gives the AI "sight" into current market conditions by reaching out to the public CoinGecko API to fetch real-time cryptocurrency prices in NZD. 
4. **`get_live_oil_price`**: Interfaces with the Yahoo Finance API (yfinance) to pull traditional commodity market data, specifically tracking live WTI and Brent crude oil prices per barrel in USD.
5. **`get_company_news`**: Pulls the top 5 most recent financial news headlines for any given market ticker, allowing the LLM to perform real-time qualitative sentiment analysis alongside its quantitative price evaluations.

## Technical Architecture
- **Language:** Python
- **Framework:** Anthropic FastMCP
- **External Dependencies:** `requests` (REST API integration), `yfinance` (Traditional market data and news API)
- **Use Case:** Demonstrates applied Agent Engineering by providing an LLM with specific, secure tools to retrieve data it cannot access through its static training weights.
