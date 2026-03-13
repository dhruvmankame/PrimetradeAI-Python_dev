import logging
import os

LOG_DIR = "logs"
LOG_FILE_PATH = os.path.join(LOG_DIR, "trading_bot.log")


def setup_logging() -> logging.Logger:
	os.makedirs(LOG_DIR, exist_ok=True)

	logger = logging.getLogger("trading_bot")
	if logger.handlers:
		return logger

	logger.setLevel(logging.INFO)

	formatter = logging.Formatter(
		"%(asctime)s | %(levelname)s | %(name)s | %(message)s"
	)

	file_handler = logging.FileHandler(LOG_FILE_PATH)
	file_handler.setFormatter(formatter)

	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(formatter)

	logger.addHandler(file_handler)
	logger.addHandler(stream_handler)

	return logger


def get_logger() -> logging.Logger:
	return setup_logging()
