from typing import Optional

import typer

from bot.client import get_client
from bot.orders import place_limit_order, place_market_order
from bot.validators import (
	validate_order_type,
	validate_price,
	validate_quantity,
	validate_side,
	validate_symbol,
)

app = typer.Typer(add_completion=False)


@app.command()
def main(
	symbol: str = typer.Argument(..., help="Trading symbol, e.g., BTCUSDT"),
	side: str = typer.Argument(..., help="Order side: BUY or SELL"),
	order_type: str = typer.Argument(..., help="Order type: MARKET or LIMIT"),
	quantity: float = typer.Argument(..., help="Order quantity"),
	price: Optional[float] = typer.Argument(None, help="Limit price (LIMIT only)"),
) -> None:
	try:
		symbol = validate_symbol(symbol)
		side = validate_side(side)
		order_type = validate_order_type(order_type)
		quantity = validate_quantity(quantity)
		price = validate_price(price, order_type)

		print("## Order Request Summary")
		print(f"Symbol: {symbol}")
		print(f"Side: {side}")
		print(f"Type: {order_type}")
		print(f"Quantity: {quantity}")
		if order_type == "LIMIT":
			print(f"Price: {price}")

		client = get_client()
		if order_type == "MARKET":
			response = place_market_order(client, symbol, side, quantity)
		else:
			response = place_limit_order(client, symbol, side, quantity, price)

		print("\n## Response")
		print(f"Order ID: {response.get('orderId', 'N/A')}")
		print(f"Status: {response.get('status', 'N/A')}")
		print(f"Executed Quantity: {response.get('executedQty', 'N/A')}")

		avg_price = response.get("avgPrice")
		if not avg_price:
			avg_price = response.get("averagePrice", "N/A")
		print(f"Average Price: {avg_price}")
	except ValueError as exc:
		typer.secho(f"Input error: {exc}", fg=typer.colors.RED)
		raise typer.Exit(code=1)
	except EnvironmentError as exc:
		typer.secho(str(exc), fg=typer.colors.RED)
		raise typer.Exit(code=1)
	except RuntimeError as exc:
		typer.secho(f"Order failed: {exc}", fg=typer.colors.RED)
		raise typer.Exit(code=1)
	except Exception as exc:
		typer.secho(f"Unexpected error: {exc}", fg=typer.colors.RED)
		raise typer.Exit(code=1)


if __name__ == "__main__":
	app()
