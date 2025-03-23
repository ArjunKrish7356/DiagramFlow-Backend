import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("my_app")
    logger.setLevel(logging.DEBUG)

    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=1024 * 1024, backupCount=5  # 1 MB per file, keep 5 backups
    )
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Add formatter to handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize the logger
logger = setup_logger()