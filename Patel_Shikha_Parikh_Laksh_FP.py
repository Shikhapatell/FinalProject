#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:12:42 2022

@author: shikhapatel
"""
#Authors: Laksh Parikh & Shikha Patel
#Date: 12/7/2022
#Assignment: Final Project
#Description: This program keeps track of Inventory and print out transactions

#imported the inventory and transactionitem class
import inventory
import transactionitem


#This function takes the inventory text file and converts it into a dictionary with the key as the item ID
def process_inventory(inventory_file): 
    #reading text file and creating a dictionary
    file = open(inventory_file, "r")
    id_inventory = file.readline().rstrip('\n')
    inventoryDict = {}
    #loop to go through every line of file and assign them to variables that are associated with it
    while id_inventory!='':  
        name_inventory = file.readline().rstrip('\n')
        stock_inventory = float(file.readline().rstrip('\n'))
        price_inventory = float(file.readline().rstrip('\n'))
        #Create an instance of inventory with the above variables as attributes
        new_inventory = inventory.Inventory(id_inventory,name_inventory,price_inventory, stock_inventory)
        #Add instance into dictionary
        inventoryDict.update({new_inventory.get_id().rstrip('\n'): new_inventory}) 
        id_inventory = file.readline() 
    file.close()
    
    return inventoryDict
    
#This function prints the dictionary of inventory objects as a table
def print_inventory(dict_inventory):
   #print table header
   print(format("ID", "5"), format("Item", '33'), format("Price", '7'), format("Stock", '10'))
   #Iterates through dictionary and prints each object
   for i in dict_inventory:
       print(dict_inventory[i])
   print("\nEnter 0 when finished")
    
 #This function prompts the user to enter an item ID and validates it   
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

#This function asks for the quanitity the user wants to buy or return for the previously prompted ID and returns that amount
def get_quantity (list_inventory, item_id): 
    #conditional to check if the id is not 0
    if float(item_id) != 0: 
        item_quantity = float(input("Please enter the desired quantity (negative quantity for return): "))
        return item_quantity
    
#This function writes an updated inventory file when a transaction is made
def write_updated_inventory(dict_inventory): 
    file = open("UpdatedInventory.txt", "w")
    count = 0
    #loop to iterate through dictionary parameter and write text file with same format as inventory file
    for i in dict_inventory: 
            file.write(dict_inventory[i].get_id().rstrip("\n"))
            file.write("\n" + dict_inventory[i].get_name()+"\n")
            file.write(str(dict_inventory[i].get_stock())+"\n")
            file.write(str(dict_inventory[i].get_price())+"\n")
            count+= 4
       
        
#This function prints the invoice at the end of the transaction(s)  
def print_invoice(transaction_dict): 
    print(format("ID", "5"), format("Item", '33'),format("Qty", '8'), format("Price", '8'), format("Total", '11'))

    total = 0
    for i in transaction_dict: 
        
        print(format((i), "6") + format(transaction_dict[i].get_name(), "22")+ format(transaction_dict[i].get_stock(), "15")+format(round(transaction_dict[i].get_price(), 2), "11")+format(round(transaction_dict[i].calc_cost(), 2), "8"))
        total += transaction_dict[i].calc_cost()
   
   
    tax = total * .085
    totaloverall = total + tax
    print("\nPrice: $", format(total,'.2f'), sep="")
    print("Tax: $", format(tax,'.2f'),sep="")
    print("Total: $", format(totaloverall,'.2f'), sep="")
    
    
def main():   
    #initialized new dictionary to store transaction objects
    transaction_dict = {}
    invoice = {}
    #process inventory text file and convert into dictionary of objects
    dict_inventory = process_inventory("Inventory.txt")
    #print dictionary into a table
    print_inventory(dict_inventory)
    #create iduser variable that stores the ID that the user wants
    iduser = get_item_id(dict_inventory)
    #creates quantityuser which gets how much the user wants of the item
    quantityuser = get_quantity(dict_inventory, iduser)
    #conditional to check if the ID of the corresponding item is in the inventory
    if iduser in dict_inventory: 
        #conditional to check if current inventory can support the transaction
        if quantityuser > dict_inventory[iduser].get_stock():
           print("Sorry, we do not have enough stock.")
           print("")    
           
        
        
        #performs transaction  
        if quantityuser <= dict_inventory[iduser].get_stock() and iduser != "0": 
               #creates transactionitem and adds to transaction item dictionary
                
            new_transaction = transactionitem.TransactionItem(iduser,dict_inventory[iduser].get_name(),dict_inventory[iduser].get_price(), quantityuser)
            invoice.update({new_transaction.get_id().rstrip("\n|"):new_transaction})
            transaction_dict.update({new_transaction.get_id().rstrip("\n|"):new_transaction})
            original = dict_inventory[iduser].get_stock() 
            
            updatedQuantity = int(original - quantityuser)
           
        
       
        
            new_transaction.set_qty(updatedQuantity)
            dict_inventory[iduser] = new_transaction
            #updates new inventory
            write_updated_inventory(dict_inventory)
            updatedQuantityinvoice = int(quantityuser)
            
            new_transaction.set_qty(updatedQuantityinvoice)
            dict_inventory = process_inventory("UpdatedInventory.txt")
            
    #loop if there are more transactions
    while True:
    
       
       
        
        print_inventory(dict_inventory)
        iduser = get_item_id(dict_inventory)
        
        #if user enters 0 then invoice is printed
        if iduser == "0":
            print_invoice(transaction_dict)
            break
        
        quantityuser = get_quantity(dict_inventory, iduser)
        if quantityuser > dict_inventory[iduser].get_stock():
           print("Sorry, we do not have enough stock.")
           print("")    
           
        #performs transaction  
        if quantityuser <= dict_inventory[iduser].get_stock() and iduser != "0": 
               #creates transactionitem and adds to transaction item dictionary
                
            new_transaction = transactionitem.TransactionItem(iduser,dict_inventory[iduser].get_name(),dict_inventory[iduser].get_price(), quantityuser)
            invoice.update({new_transaction.get_id().rstrip("\n|"):new_transaction})
            transaction_dict.update({new_transaction.get_id().rstrip("\n|"):new_transaction})
            original = dict_inventory[iduser].get_stock() 
            
            updatedQuantity = int(original - quantityuser)
           
        
       
        
            new_transaction.set_qty(updatedQuantity)
            dict_inventory[iduser] = new_transaction
            #updates new inventory
            write_updated_inventory(dict_inventory)
            updatedQuantityinvoice = int(quantityuser)
            
            new_transaction.set_qty(updatedQuantityinvoice)
            dict_inventory = process_inventory("UpdatedInventory.txt")
            
    
main()