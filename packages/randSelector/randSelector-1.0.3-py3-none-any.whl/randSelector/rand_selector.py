#!/usr/bin/env python

""" Description: class selects random item from a data set and its probability """

from random import choices
from random import uniform
from random import seed
from collections import Counter

__author__ = "Syed Hamza Rafique"
__copyright__ = "Copyright 2022, MS Test"
__version__ = "1.0.0"
__email__ = "hamzah_shah@hotmail.com"
__status__ = "Production"


def gen_uniform_rand_num(seed_num):
    """ generates random number between 0 and 1 using a uniform distribution"""
    seed(seed_num)

    return uniform(0, 1)


def select_rand_item(prob_data_set, seed_num):
    """ selects random number from the prob_data_set using associated probababilities"""        

    if type(prob_data_set) is not tuple:
        raise TypeError('Only tuples of tuples allowed as input')

    if not prob_data_set:
        raise TypeError('empty tuple')

        
    numbers = []
    probabillities = []
    rand_num = gen_uniform_rand_num(seed_num=seed_num)

    # test for valid data
    for data in prob_data_set:

        if type(data) is not tuple or len(data) != 2:
            raise TypeError('Only tuples (num, probability) are allowed as inputs')
        
        num, prob = data
        probabillities.append(prob)

        if not 0 <= prob <= 1:
            raise ValueError('probabillities can only be in rand [0:1]')


    if sum(probabillities) != 1:
        raise ValueError('sum of probablities cant be > 1')


    # select num from list based on associated probability
    cumsum = 0   
    for data in prob_data_set:

        num, prob = data            
        cumsum += prob
        if cumsum >= rand_num:
            return [num, prob]

    return [num, prob] 
    



def ref_py_lib_method(prob_data_set, seed_num):
    """python reference function to compare with select_rand_item for correctness """

    if type(prob_data_set) is not tuple:
        raise TypeError('Only tuples')

    if not prob_data_set:
        raise TypeError('empty tuple')

    numbers = []
    probabilities = []

    for data in prob_data_set:

        if type(data) is not tuple or len(data) != 2:
            raise TypeError('Only tuples (num, probability) are allowed as inputs')
        
        num, prob = data

        if not 0 <= prob <= 1:
            raise ValueError('probabilities can only be in rand [0:1]')


        numbers.append(num)
        probabilities.append(prob)

    if sum(probabilities) != 1:
        raise ValueError('sum of probablities cant be > 1')

    seed(seed_num)
    item = choices(numbers, probabilities)
    index = numbers.index(item[0])


    return  [item[0], probabilities[index]];