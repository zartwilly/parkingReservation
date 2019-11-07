#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:57:48 2019

@author: willy
"""
import random
import string
import pandas as pd

LETTERS = list(string.ascii_uppercase)
DIGITS = list(string.digits)
LETTERS.extend(DIGITS)

url_first_names = 'https://query.data.world/s/xfjzgxtfvtgihxjh24fok3zvhtjh4d'
url_surnames = "https://query.data.world/s/7xtbbuvrdateawh4fbuaibxmsdk2cw"
DF_FIRSTNAMES = pd.read_csv(url_first_names, 
                          names=["col_a", "names", "new_percentage_2013"])
DF_SURNAMES = pd.read_csv(url_surnames, 
                              names=["col_a", "names", "new_percentage_2013"])

def generate_id():
    """ generate user_id 
        format XXXX-0000
    """
    parts = [] 
    for i in range(2):
        parts.append( "".join(random.sample(LETTERS,4)) )
        
    return "-".join(parts)

def generate_name():
    """ generate a user name 
    """
    names = []
    names.extend( random.sample( list(DF_FIRSTNAMES["names"]), 1))
    names.extend( random.sample( list(DF_SURNAMES["names"]), 
                                 random.randint(1,2)))
    return " ".join(names)
    
        
def generate_bank_account():
    """ generate a bank account number
        format XXXX-XXXX-XXXX-XXXX-XXXX
    """
    iban = []
    for i in range(5):
        if i not in [2,3]:
            iban.append( "".join(random.sample(LETTERS,4)) ) 
        else:
            iban.append( "".join(random.sample(DIGITS,4)) )
    
    return "-".join(iban)
        
def generate_car_licence():
    """ generate a car licence
         format XX-000-XX-DD
    """
    parts = []
    for i in range(4):
        if i != 1 and i != 3:
            parts.append( "".join(random.sample(list(string.ascii_uppercase), 2)) ) 
        elif i == 1:
            parts.append( "".join(random.sample(DIGITS, 3)) )
        elif i == 3:
            parts.append( "".join(random.sample(DIGITS, 2)) )
    
    return "-".join(parts)