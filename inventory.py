#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:12:30 2022

@author: shikhapatel
"""

class Inventory: 
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price
        
        
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name
        
    def get_stock(self):
        return self.__stock
        
    def get_price(self):
        return self.__price
        
    def restock(self,new_stock):
        self.__stock = new_stock
        
    def purchase(self,purch_qty):
        print()
        
    def __str__(self): 
        var = format(self.__id, '5') +  format(self.__name, '30')+ "$" + format(str(self.__price), '5') + format(str(self.__stock), '11')
        return var
        
        
        