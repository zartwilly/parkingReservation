#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:20:44 2019

@author: willy
"""

import pathlib
import pandas as pd


class User:
    
    def __init__(self, name, bank_account, car_licence):
        """ initialisation of application's user
        """
        self._name = name
        self._user_id = ""
        self._bank_account = bank_account
        self._car_licence = car_licence
        
    def __repr__(self):
        """ format the information of the user in the cmd interpreter
        """
        return "User: name={}, user_id={}, bank_account={}, car_licence={}"\
                .format(self._name, self._user_id, self._bank_account, 
                        self._car_licence)
                
    def _get_name(self):
        """ return the user's name
        """
        return self._name
    
    def _set_name(self, new_name):
        """ modify the user's name 
        """
        self._name = new_name;
        
    name = property(_get_name, _set_name)
    
    def _get_user_id(self):
        """ return the user's id
        """
        return self._user_id
    
    def _set_user_id(self, new_user_id):
        """ modify the user's id that is a string type
        """
        self._user_id = new_user_id
        
    user_id = property(_get_user_id, _set_user_id)
    
    def _get_bank_account(self):
        """ return the bank account number
        """
        return self._bank_account
    
    def _set_bank_account(self, new_bank_account):
        """ modify the user's id that is a string type
        """
        self._bank_account = new_bank_account
        
    bank_account = property(_get_bank_account, _set_bank_account)
    
    def _get_car_licence(self):
        """ return the car licence number
        """
        return self._car_licence
    
    def _set_car_licence(self, new_car_licence):
        """ modify the car licence that is a string type
        """
        self._car_licence = new_car_licence
        
    car_licence = property(_get_car_licence, _set_car_licence)
    
    def save_user_on_file(self, path_file="user_data"):
        """ save new user on csv file 
        """
        path = pathlib.Path(path_file); path.mkdir(parents=True, exist_ok=True);
        file = "user_accounts.csv"
        df_file = pd.DataFrame(
                    columns=["user_id","name", "car_licence","bank_account"])
        if pathlib.Path(path_file+"/"+file).is_file():
            # file exists
            df_file = pd.read_csv(
                        path_file+"/"+file, 
                        names=["user_id","name", "car_licence","bank_account"])
            if any(df_file["user_id"] == self.user_id):
                ind = df_file[df_file["user_id"] == self.user_id].index
                df_file.loc[ind, "name"] = self.name+"UPDATE";
                df_file.loc[ind, "car_licence"] = self.car_licence+"UPDATE";
                df_file.loc[ind, "bank_account"] = self.bank_account;
#                df_file.loc[ind, ""] = self.;
            else:
                nrow = len(df_file)
                df_file.loc[nrow, "name"] = self.name; 
                df_file.loc[nrow, "user_id"] = self.user_id; 
                df_file.loc[nrow, "car_licence"] = self.car_licence;
                df_file.loc[nrow, "bank_account"] = self.bank_account; 
        else:
            # file don't exists
            nrow = len(df_file)
            df_file.loc[nrow, "name"] = self.name; 
            df_file.loc[nrow, "user_id"] = self.user_id; 
            df_file.loc[nrow, "car_licence"] = self.car_licence;
            df_file.loc[nrow, "bank_account"] = self.bank_account; 
            
        df_file.to_csv(path_file+"/"+file, header=None)
        
    def save_user_on_elk(self):
        """ save user on the ELK index
        """
        pass