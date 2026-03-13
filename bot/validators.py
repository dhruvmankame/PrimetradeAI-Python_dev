from typing import Optional


def validate_symbol(symbol: str) -> str:
	value = symbol.strip()
	if not value or not value.isupper():
		raise ValueError("Symbol must be uppercase (e.g., BTCUSDT)")
	return value


def validate_side(side: str) -> str:
	value = side.strip().upper()
	if value not in {"BUY", "SELL"}:
		raise ValueError("Side must be BUY or SELL")
	return value


def validate_order_type(order_type: str) -> str:
	value = order_type.strip().upper()
	if value not in {"MARKET", "LIMIT"}:
		raise ValueError("Order type must be MARKET or LIMIT")
	return value


def validate_quantity(quantity: float) -> float:
	try:
		value = float(quantity)
	except (TypeError, ValueError) as exc:
		raise ValueError("Quantity must be a positive number") from exc

	if value <= 0:
		raise ValueError("Quantity must be a positive number")
	return value


def validate_price(price: Optional[float], order_type: str) -> Optional[float]:
	if order_type == "LIMIT":
		if price is None:
			raise ValueError("Price is required for LIMIT orders")
		try:
			value = float(price)
		except (TypeError, ValueError) as exc:
			raise ValueError("Price must be a positive number") from exc
		if value <= 0:
			raise ValueError("Price must be a positive number")
		return value

	if price is not None:
		raise ValueError("Price is only applicable for LIMIT orders")
	return None
