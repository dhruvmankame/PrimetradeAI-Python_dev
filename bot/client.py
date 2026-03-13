import os

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv

from bot.logging_config import get_logger

_CLIENT = None
_FUTURES_TESTNET_URL = "https://testnet.binancefuture.com/fapi"


def get_client() -> Client:
	global _CLIENT

	if _CLIENT is not None:
		return _CLIENT

	logger = get_logger()
	load_dotenv()

	api_key = os.getenv("BINANCE_API_KEY")
	api_secret = os.getenv("BINANCE_API_SECRET")

	if not api_key or not api_secret:
		logger.error("Missing BINANCE_API_KEY or BINANCE_API_SECRET in environment")
		raise EnvironmentError("Missing Binance API credentials in .env file")

	try:
		client = Client(api_key, api_secret)
		client.FUTURES_URL = _FUTURES_TESTNET_URL
		client.FUTURES_DATA_URL = _FUTURES_TESTNET_URL
		client.futures_ping()
	except (BinanceAPIException, BinanceRequestException) as exc:
		logger.error("Failed to connect to Binance Futures Testnet: %s", exc)
		raise ConnectionError("Unable to connect to Binance Futures Testnet") from exc

	logger.info("Connected to Binance Futures Testnet")
	_CLIENT = client
	return _CLIENT
