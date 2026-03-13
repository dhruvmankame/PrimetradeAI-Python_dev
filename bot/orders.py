from typing import Any, Dict

from binance.exceptions import BinanceAPIException, BinanceOrderException
from requests.exceptions import RequestException

from bot.logging_config import get_logger


def place_market_order(
	client, symbol: str, side: str, quantity: float
) -> Dict[str, Any]:
	logger = get_logger()
	logger.info("Placing MARKET order %s %s qty=%s", symbol, side, quantity)

	try:
		response = client.futures_create_order(
			symbol=symbol,
			side=side,
			type="MARKET",
			quantity=quantity,
		)
	except (BinanceAPIException, BinanceOrderException) as exc:
		logger.error("Binance API error while placing MARKET order: %s", exc)
		raise RuntimeError("Binance API error while placing MARKET order") from exc
	except RequestException as exc:
		logger.error("Network error while placing MARKET order: %s", exc)
		raise RuntimeError("Network error while placing MARKET order") from exc

	logger.info("Binance response %s", response)
	return response


def place_limit_order(
	client, symbol: str, side: str, quantity: float, price: float
) -> Dict[str, Any]:
	logger = get_logger()
	logger.info(
		"Placing LIMIT order %s %s qty=%s price=%s", symbol, side, quantity, price
	)

	try:
		response = client.futures_create_order(
			symbol=symbol,
			side=side,
			type="LIMIT",
			quantity=quantity,
			price=price,
			timeInForce="GTC",
		)
	except (BinanceAPIException, BinanceOrderException) as exc:
		logger.error("Binance API error while placing LIMIT order: %s", exc)
		raise RuntimeError("Binance API error while placing LIMIT order") from exc
	except RequestException as exc:
		logger.error("Network error while placing LIMIT order: %s", exc)
		raise RuntimeError("Network error while placing LIMIT order") from exc

	logger.info("Binance response %s", response)
	return response
