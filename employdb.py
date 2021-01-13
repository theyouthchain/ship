# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:54:41 2021

@author: ACER
"""


import sqlite3  
  
con = sqlite3.connect("shipping.db")  
print("Database opened successfully")  
  
con.execute("create table  shipping(id INTEGER PRIMARY KEY AUTOINCREMENT, total_weight TEXT NOT NULL, total_cases TEXT UNIQUE NOT NULL,total_quantity TEXT NOT NULL, in_cost TEXT NOT NULL,collecting_cost TEXT NOT NULL,best_shipping_cost TEXT NOT NULL,best_carrier TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()