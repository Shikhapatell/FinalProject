#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:12:32 2022

@author: shikhapatel
"""

class TransactionItem: 
    def __init__(self, new_id, new_name, new_qty, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__quantity = new_qty
        self.__price = new_price
    
    def get_id(self): 
        return self.__id
        
        
    def set_id(self, new_id): 
        self.__id = new_id
        
        
    def get_name(self): 
        return self.__name
        
        
    def set_name(self,new_name): 
        self.__name = new_name
        
        
    def get_qty(self): 
        return self.__quantity
        
        
    def set_qty(self,new_qty): 
        self.__quantity = new_qty
        
        
    def get_price(self): 
        return self.__price
        
        
    def set_price(self,new_price): 
        self.__price = new_price
        
        
    def calc_cost(): 
        print()
        
        
        
    def __str__(self): 
        print()
        