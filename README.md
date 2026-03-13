# Trading Bot CLI (Binance Futures Testnet)

## Project Overview
This project is a CLI trading bot for the Binance Futures Testnet. It supports
MARKET and LIMIT orders, BUY and SELL sides, input validation, structured
logging, and clear console output.

## Setup Instructions
1. Create and activate a Python 3 environment.
2. Install dependencies.
3. Create a `.env` file with your Binance Testnet API keys.

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Create .env File
Create a `.env` file in the project root with the following:
```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

## Run Examples
Market order:
```bash
python cli.py BTCUSDT BUY MARKET 0.01
```

Limit order:
```bash
python cli.py BTCUSDT SELL LIMIT 0.01 65000
```

Logs are written to `logs/trading_bot.log`.
