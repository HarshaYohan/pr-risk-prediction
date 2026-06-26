"""Logging helpers."""
import logging


def get_logger(name: str = "pr_risk", level: int = logging.INFO) -> logging.Logger:
    """Create or return a basic project logger."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        )
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
