#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:39:40 2019

@author: willy
"""

import time
import user as us
import pandas as pd

import utils_fonctions as utils_fcts

def test_user_on_file(user_number=200):
    """ tester la classe user avec injection de 200 users
    """
    for number in range(user_number):
        user_n = us.User(name="", bank_account="", car_licence="")
        user_id_n = utils_fcts.generate_id()
        name_n = utils_fcts.generate_name()
        bank_acc_n = utils_fcts.generate_bank_account()
        car_lic_n = utils_fcts.generate_car_licence()
        
        user_n._set_user_id(user_id_n)
        user_n._set_name(name_n)
        user_n._set_bank_account(bank_acc_n)
        user_n._set_car_licence(car_lic_n)
        
        user_n.save_user_on_file()
        if number%100 == 0:
            print("{}, {} saved".format(number, user_n))
        
#    # modification de n=20 users
#    path_file="user_data"; file = "user_accounts.csv"
#    df = pd.read_csv(path_file+"/"+file, 
#                     columns=["user_id","name", "car_licence","bank_account"])
#    
#    for user_id in df["user_id"].sample(user_number*0.1):
#        # modifier ces user_id


if __name__ == '__main__':
    start = time.time()
    
    test_user_on_file()
    print("runtime = {}".format(time.time() - start))