import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("arthmaticApp")

def add(a,b):
    result = a + b
    logger.debug(f"Addition of {a} & {b} is {result}")
    return result

def trueDivision(a,b):
    try:
        result = a/b
        logger.debug(f"Division of {a} & {b} is {result} \n")
        return result
    except ZeroDivisionError:
        logger.error("Division by Zero, Invalid. \n")
        return None



add(2,5)
trueDivision(22,34)

