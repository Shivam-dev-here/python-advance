import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H-%M-%S'
)

logging.debug("Successful")
logging.info("System working normal")
logging.warning("value expected a list")
logging.error("missing a ','")
logging.critical("function is undefined")