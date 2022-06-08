import math

import logging

logging.basicConfig(filename='aritmetika.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def sum(*args):
    total = 0
    for x in args:
        total += x
    logging.info(f"suma: {total}")
    return total

sum(2, 5, 6)


def square_root(x: int) -> float:
    logging.info(f"square: {math.sqrt(x)}")
    return math.sqrt(x)
    
square_root(9)


def len_sentence(x: str) ->int:
    logging.info(f"len of sentence: {len(x)}")
    return len(x)

len_sentence('heloooo')


def devide(x: int, y: int) -> float:
    logging.info(f"devide: {x/y}")
    return x/y

devide(15,3)
