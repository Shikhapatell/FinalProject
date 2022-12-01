#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:12:42 2022

@author: shikhapatel
"""

#Laksh & Shikha final project
#hi
import inventory
import transactionitem

def process_inventory(): 
    
    
    file = open("Inventory.txt", "r")
    id_inventory = file.readline().rstrip('\n')
    inventoryDict = {}
    
    #create a list with all of the contents of the file
    while id_inventory!='':
        
        #append grade to list
        name_inventory = file.readline().rstrip('\n')
        stock_inventory = int(file.readline().rstrip('\n'))
        price_inventory = float(file.readline().rstrip('\n'))
        new_inventory = inventory.Inventory(id_inventory,name_inventory,price_inventory, stock_inventory)
        inventoryDict.update({new_inventory.get_id().rstrip('\n'): new_inventory}) 
        
        id_inventory = file.readline() 
    file.close()
    
    return inventoryDict
    
    
def print_inventory(dict_inventory):
    
    
   print(format("ID", "5"), format("Item", '33'), format("Price", '7'), format("Stock", '10'))
    
    #for i in dict_inventory:
        
    
   for i in dict_inventory:
       print(dict_inventory[i])
   print("\nEnter 0 when finished")
    
    
def get_item_id (dict_inventory): 
    
    value = True
    while value: 
        try: 
            item_id = input("Please input the item ID you wish to purchase/return: ")
            
            if float(item_id) == 0: 
                value = False
                break
            
            else:
                if item_id not in dict_inventory: 
                    print("Input was invalid.")
                    value = True
                else: 
                    value = False
            
            
               
        except ValueError:
            print("Input was invalid.")
            value = True
           
    return item_id


def get_quantity (list_inventory, item_id): 
    
    if float(item_id) != 0: 
        item_quantity = float(input("Please enter the desired quantity (negative quantity for return): "))
        return item_quantity
    
    #do we do validate the quanity 
    #when it says new the only new thing is the quantity rigth? 
    
def write_updated_inventory(dict_inventory): 
    file = open("UpdatedInventory.txt", "w")
    for i in dict_inventory: 
        file.write(dict_inventory[i].__str__() + "\n")
        
    
def print_invoice(): 
    #insert code 
    print()
    
    
def main():   
    
    dict_inventory = process_inventory()
    print_inventory(dict_inventory)
    iduser = get_item_id(dict_inventory)
    quanityuser = get_quantity(dict_inventory, iduser)
    
    if iduser in dict_inventory: 
        if iduser != 0: 
            new_transaction = transactionitem.TransactionItem(iduser,dict_inventory[iduser].get_name(),dict_inventory[iduser].get_price(), quanityuser)
            original = dict_inventory[iduser].get_stock()
            updatedQuantity = original - quanityuser
            new_transaction.set_qty(updatedQuantity)
           
            dict_inventory[iduser] = new_transaction 

            write_updated_inventory(dict_inventory)
    
    
    
    
    
main()