import logging
# import log_asmenys

logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def dalyba(a, b):
    return a / b

a = 10
b = 5

padalinom = dalyba(a, b)
logging.debug(f"Dalyba: {a} / {b} = {padalinom}")