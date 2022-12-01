#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:12:30 2022

@author: shikhapatel
"""

class Inventory: 
    def __init__(self, user_id, name, price, stock):
        self.__id = user_id
        self.__name = name
        self.__stock = stock
        self.__price = price
        
        
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name
        
    def get_stock(self):
        return self.__stock
        
    def get_price(self):
        return self.__price
        
    def restock(self,new_stock):
        if 0 < new_stock: 
            self.__stock += new_stock
            return True 
        else: 
            return False 
            
        
    def purchase(self,purch_qty):
        if self._stock - purch_qty >= 0: 
            self._stock -= purch_qty
            return True 
        else: 
            return False 
        
    def __str__(self): 
        var = format(self.__id.rstrip("\n"), '5') +  format(self.__name.rstrip("\n"), '35')+ "$" + format(str(self.__price), '10') + format(str(self.__stock), '10')
        return var
        
        
        