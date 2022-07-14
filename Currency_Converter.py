#Importing required libraries for GUI and database connection
#Tkinter is the inbuilt python module that is used to create GUI applications
import tkinter as tk 
from tkinter import *
import tkinter.messagebox
import mysql.connector

#Database Connection to get allowed pairs for conversion
mydb = mysql.connector.connect(
    host="localhost",
    user="Nishit",
    password="Apply@2021",
    database="fxrates"
)

#fetiching the currency pairs from database
mycursor = mydb.cursor()
mycursor.execute("SELECT currency_code FROM fxrates.iso_currency ")
myresult = mycursor.fetchall()
#initalise an empty list to convert each row returned as Tuple from the database and have a clean list
CurrenyCode_list=[]
for ccode in myresult:
    CurrenyCode_list.append(ccode[0])

#The GUI
#Intializing main window object named root
root = tk.Tk()

#Setting the title, background color and the size for the the main window
root.title("Global Currency Converter")
root.configure(background='#e6e5e5')
root.geometry("700x400")

#Initializing string variables for the currencies and setting their onscreen labels
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
variable1.set("Currency")
variable2.set("Currency")


#Function To For Real Time Currency Conversion 
def RealTimeCurrencyConversion():
    #Importing the conversion library functions Forex Python
    #Forex Python is a Free Foreign exchange rates and currency conversion package.
    #Features: List all currency rates. Get historical rates since 1999.
    #Convert amount from one currency to other.(‘USD 10$’ to INR). etc.
    #Documentation: http://forex-python.readthedocs.io/en/latest/usage.html 
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()
    
    #reading the from and to currency inputs given by the user
    from_currency = variable1.get()
    to_currency = variable2.get()
    
    #validate the inputs before starting the conversion process
    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter a valid amount.")
 
    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    #all inputs validated, start the conversion process 
    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
    #clean the converted amount field if any old value is present and populate with the fresh calculated value
        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, str(new_amount))
 
#clearing all the data entered by the user
def ClearAll():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
 

#Setting the display labels
Label_1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
Label_1.grid(row=2, column=0)
 
Label_1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
Label_1.grid(row=3, column=0)
 
Label_1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
Label_1.grid(row=4, column=0)
 
Label_1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
Label_1.grid(row=8, column=0)

#setting blank labels to create some space onscreen and increase readability
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0)
 
Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0)

#define amount fields
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=3)
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=3)

#Display the currencies fetched from database in the onscreen dropdowns
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
FromCurrency_option.grid(row=3, column=3, ipadx=45) #ipadx to add some spaces, to improve readability
ToCurrency_option.grid(row=4, column=3, ipadx=45)

#Add buttons and set their commands to call the pre-defined functions 
Label_1 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", bg="lightblue", fg="white",
                 command=RealTimeCurrencyConversion)
Label_1.grid(row=6, column=3)
 
Label_1 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", bg="lightblue", fg="white",
                 command=ClearAll)
Label_1.grid(row=10, column=3)
 
# Calling mainloop method which is used when the application is ready to run.
# It tells the code to keep displaying 
root.mainloop()
