import logging

# Configuring Logging
logging.basicConfig(
    filename="data_preprocessor.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s: %(message)s",
    datefmt="%b %d %Y %I:%M:%S %p",
    level=logging.INFO
)


def get_logger():
    """
    Returns configured logger instance.
    """
    return logging.getLogger("DataPreprocessor")