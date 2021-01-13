# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 21:55:38 2021

@author: ACER
"""


from flask import *  
import sqlite3  
  
app = Flask(__name__,static_folder = "static")  
 
@app.route("/")  
def index():  
    return render_template("index.html");  


@app.route("/addshipping")  
def add():  
    return render_template("addshipping.html")

@app.route("/addinventory")  
def addin():  
    return render_template("addinventory.html")

@app.route("/addshippingprice")  
def addsp():  
    return render_template("addshippingprice.html")


@app.route("/addshippingcompanies")  
def addsc():  
    return render_template("addshippingcompanies.html")


@app.route("/additalian")  
def addit():  
    return render_template("additalian.html")

 
@app.route("/savedetailsshipping",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
       # try:  
            total_weight = request.form["total_weight"]  
            total_cases = request.form["total_cases"]  
            total_quantity = request.form["total_quantity"] 
            in_cost = request.form["in_cost"] 
            collecting_cost= request.form["collecting_cost"]
            best_shipping_cost = request.form["best_shipping_cost"]
            best_carrier = request.form["best_carrier"]
            print(total_weight)
            with sqlite3.connect("shipping.db") as con:  
                con.execute("CREATE TABLE IF NOT EXISTS  shipping(id INTEGER PRIMARY KEY AUTOINCREMENT, total_weight TEXT NOT NULL, total_cases TEXT UNIQUE NOT NULL,total_quantity TEXT NOT NULL, in_cost TEXT NOT NULL,collecting_cost TEXT NOT NULL,best_shipping_cost TEXT NOT NULL,best_carrier TEXT NOT NULL)") 
                con.execute("INSERT OR IGNORE into shipping (total_weight,total_cases,total_quantity,in_cost,collecting_cost,best_shipping_cost,best_carrier) values ('{}','{}','{}','{}','{}','{}','{}')".format(total_weight,total_cases,total_quantity,in_cost,collecting_cost,best_shipping_cost,best_carrier))  
                con.commit()  
                msg = "Shipping successfully Added"  
        #except:  
          #  con.rollback()  
          #  msg = "We can not add the shipping to the list"  
        #finally: 
            return render_template("successshipping.html",msg = msg)           


@app.route("/savedetailsinventory",methods = ["POST","GET"])  
def saveDetailsin():  
    msg = "msg"  
    if request.method == "POST":  
       # try:  
            quantity = request.form["quantity"]  
            item_description = request.form["item_description"]  
            sku = request.form["sku"] 
            weight = request.form["weight"] 
            itemspercase= request.form["itemspercase"]
            warehouseposition = request.form["warehouseposition"]
           
           
            with sqlite3.connect("shipping.db") as con:  
                con.execute("CREATE TABLE IF NOT EXISTS  inventory(id INTEGER PRIMARY KEY AUTOINCREMENT, quantity TEXT NOT NULL,item_description TEXT UNIQUE NOT NULL,sku TEXT NOT NULL, weight TEXT NOT NULL,itemspercase TEXT NOT NULL,warehouseposition TEXT NOT NULL)") 
                con.execute("INSERT OR IGNORE into inventory (quantity,item_description,sku,weight,itemspercase,warehouseposition) values ('{}','{}','{}','{}','{}','{}')".format(quantity,item_description,sku,weight,itemspercase,warehouseposition))  
                con.commit()  
                msg = "Shipping successfully Added"  
        #except:  
          #  con.rollback()  
          #  msg = "We can not add the shipping to the list"  
        #finally: 
            return render_template("successinventory.html",msg = msg)           
 
@app.route("/savedetailsshippingprice",methods = ["POST","GET"])  
def saveDetailssp():  
    msg = "msg"  
    if request.method == "POST":  
       # try:  
            idpricelist = request.form["idpricelist"]  
            idprovince = request.form["idprovince"]  
            idsupplier = request.form["idsupplier"]
            five = request.form["5kg"] 
            fifty = request.form["50kg"] 
            hundred= request.form["100kg"]
            onetwenty = request.form["120kg"]
            fixed = request.form["fixed"]
            insurance = request.form["insurance"]
            insmin = request.form["insmin"]
           
           
            with sqlite3.connect("shipping.db") as con:  
                con.execute("CREATE TABLE IF NOT EXISTS  shippingprice(id INTEGER PRIMARY KEY AUTOINCREMENT, idpricelist TEXT NOT NULL,idprovince TEXT UNIQUE NOT NULL,idsupplier TEXT NOT NULL, five TEXT NOT NULL,fifty TEXT NOT NULL,hundred TEXT NOT NULL,onetwenty TEXT NOT NULL,fixed TEXT NOT NULL,insurance TEXT NOT NULL, insmin TEXT NOT NULL)") 
                con.execute("INSERT OR IGNORE into shippingprice (idpricelist,idprovince,idsupplier,five,fifty,hundred,onetwenty,fixed,insurance,insmin) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(idpricelist,idprovince,idsupplier,five,fifty,hundred,onetwenty,fixed,insurance,insmin) )  
                con.commit()  
                msg = "Shipping successfully Added"  
        #except:  
          #  con.rollback()  
          #  msg = "We can not add the shipping to the list"  
        #finally: 
            return render_template("successshippingprice.html",msg = msg) 
        

@app.route("/savedetailsshippingcompanies",methods = ["POST","GET"])  
def saveDetailssc():  
    msg = "msg"  
    if request.method == "POST":  
       # try:  
            idcompany = request.form["idcompany"]  
            companyname = request.form["companyname"]  
       
           
           
            with sqlite3.connect("shipping.db") as con:  
                con.execute("CREATE TABLE IF NOT EXISTS  shippingcompanies(id INTEGER PRIMARY KEY AUTOINCREMENT, idcompany TEXT NOT NULL,companyname TEXT UNIQUE NOT NULL)") 
                con.execute("INSERT OR IGNORE into shippingcompanies (idcompany,companyname) values ('{}','{}')".format(idcompany,companyname))  
                con.commit()  
                msg = "Shipping successfully Added"  
        #except:  
          #  con.rollback()  
          #  msg = "We can not add the shipping to the list"  
        #finally: 
            return render_template("successhippingcompanies.html",msg = msg) 



@app.route("/savedetailsitalian",methods = ["POST","GET"])  
def saveDetailsit():  
    msg = "msg"  
    if request.method == "POST":  
       # try:  
            idcity = request.form["idcity"]  
            city = request.form["city"]  
            idprovince = request.form["idprovince"] 
            province = request.form["province"] 
            region = request.form["region"]
          
           
           
            with sqlite3.connect("shipping.db") as con:  
                con.execute("CREATE TABLE IF NOT EXISTS  italian(id INTEGER PRIMARY KEY AUTOINCREMENT, idcity TEXT NOT NULL,city TEXT UNIQUE NOT NULL,idprovince TEXT NOT NULL, province TEXT NOT NULL,region TEXT NOT NULL)") 
                con.execute("INSERT OR IGNORE into italian (idcity,city,idprovince,province,region) values ('{}','{}','{}','{}','{}')".format(idcity,city,idprovince,province,region))  
                con.commit()  
                msg = "Shipping successfully Added"  
        #except:  
          #  con.rollback()  
          #  msg = "We can not add the shipping to the list"  
        #finally: 
            return render_template("successitalian.html",msg = msg)

        
@app.route("/viewshipping")  
def view():  
    con = sqlite3.connect("shipping.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from shipping")  
    rows = cur.fetchall()  
    return render_template("viewshipping.html",rows = rows)  
 


@app.route("/viewinventory")  
def viewin():  
    con = sqlite3.connect("shipping.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from inventory")  
    rows = cur.fetchall()  
    return render_template("viewinventory.html",rows = rows) 


@app.route("/viewshippingprice")  
def viewsp():  
    con = sqlite3.connect("shipping.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from shippingprice")  
    rows = cur.fetchall()  
    return render_template("viewshippingprice.html",rows = rows) 

 
@app.route("/viewshippingcompanies")  
def viewsc():  
    con = sqlite3.connect("shipping.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from shippingcompanies")  
    rows = cur.fetchall()  
    return render_template("viewshippingcompanies.html",rows = rows)    

@app.route("/viewitalian")  
def viewit():  
    con = sqlite3.connect("shipping.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from italian")  
    rows = cur.fetchall()  
    return render_template("viewitalian.html",rows = rows)

@app.route("/deleteshipping")  
def delete():  
    return render_template("deleteshipping.html")  

 


@app.route("/deleteinventory")  
def deletein():  
    return render_template("deleteinventory.html")  

@app.route("/deleteshippingprice")  
def deletesp():  
    return render_template("deleteshippingprice.html")
 
    
@app.route("/deleteshippingcompanies")  
def deletesc():  
    return render_template("deleteshippingcompanies.html")

@app.route("/deleteitalian")  
def deleteit():  
    return render_template("deleteitalian.html")

@app.route("/deleterecordshipping",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("shipping.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from shipping where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_recordshipping.html",msg = msg)
        
        
@app.route("/deleterecordinventory",methods = ["POST"])  
def deleterecordin():  
    id = request.form["id"]  
    with sqlite3.connect("shipping.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from inventory where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_recordinventory.html",msg = msg)   
        
@app.route("/deleterecordshippingprice",methods = ["POST"])  
def deleterecordsp():  
    id = request.form["id"]  
    with sqlite3.connect("shipping.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from shippingprice where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_recordshippingprice.html",msg = msg)   
        
        
@app.route("/deleterecordshippingcompanies",methods = ["POST"])  
def deleterecordsc():  
    id = request.form["id"]  
    with sqlite3.connect("shipping.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from shippingcompanies where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_recordshippingcompanies.html",msg = msg)          
        
@app.route("/deleterecorditalian",methods = ["POST"])  
def deleterecordit():  
    id = request.form["id"]  
    with sqlite3.connect("shipping.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from italian where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_recorditalian.html",msg = msg)  
        
if __name__ == "__main__":  
    app.run(debug = True)  