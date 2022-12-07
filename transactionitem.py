#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:12:32 2022

@author: shikhapatel
"""
#This class is for an item that a user wants to buy or return

class TransactionItem: 
    
    #object attributes
    def __init__(self, user_id, name, price, quantity):
        self.__id = user_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
    
   #Accessor methods
    def get_id(self):
       return self.__id
       
    def get_name(self):
       return self.__name
       
    def get_stock(self):
       return self.__quantity
       
    def get_price(self):
       return self.__price
   
    
   #mutator methods
    def set_id(self, new_id): 
        self.__id = new_id
        
        
    def set_name(self,new_name): 
        self.__name = new_name
        
        
  
   
    def set_qty(self,new_qty): 
       
        self.__quantity =  new_qty 
        
   
    def set_price(self,new_price): 
        self.__price = new_price
     
    #calculating cost of transaction
    def calc_cost(self):
        return self.__quantity * self.__price
 
    #string method    
    def __str__(self): 
        var = format(self.__id.rstrip("\n"), '5') +  format(self.__name.rstrip("\n"), '35')+ "$" + format(str(self.__price), '10') + format(str(self.__quantity), '10')
        return var
        