from logger import logging

def mult(a,b):
    logging.debug("OPR: Multiplication is next opr ")
    return(a*b)

logging.debug("CALL: Fuction is being call")
mult(4,699)