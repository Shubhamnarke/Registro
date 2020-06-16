from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import sqlite3
import tkinter.messagebox
import csv
import os
root = Tk()
root.title("Registro System")
root.geometry("750x400+300+100")

#style = ttk.Style(root)
#style.configure("lefttab.TNotebook",tabposition = "wn")

db = ('catch.db')
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userdata (id INTEGER PRIMARY KEY , first TEXT,last TEXT,email TEXT, age TEXT,address TEXT,mob_no TEXT,DOB TEXT)")
conn.commit()


def adition():
    if first_name_e.get() == "" or last_name_e.get() == "" or email_e.get() == "" or age_e.get() == "" or phone_e.get() == "" or dob_e.get() == "":
        tkinter.messagebox.showerror("Error","All feeds are requied")
        first_name_e.focus()
    else:

        f_name = str(first_name_e.get())
        l_name = str(last_name_e.get())
        email = str(email_e.get())
        age = str(age_e.get())
        address = str(address_e.get())
        mobile = str(phone_e.get())
        date_birth = str(dob_e.get())
        cur.execute("INSERT INTO userdata (first,last,email,age,address,mob_no,DOB) values (?,?,?,?,?,?,?)",(f_name,l_name,email,age,address,mobile,date_birth))
        tkinter.messagebox.showinfo("Success","Data added successfully")
        conn.commit()
        result = F"Registration Window\n First Name : {f_name} \n Last Name : {l_name} \n email : {email} \n Age : {age} \n Address : {address} \n Mob. no. : {mobile} \n DOB : {date_birth} \n\nSubmitted to databse.."
        scrolled_text.insert(END,result)

        first_name_e.delete(0, END)
        last_name_e.delete(0, END)
        age_e.delete(0, END)
        address_e.delete(0, END)
        dob_e.delete(0, END)
        phone_e.delete(0, END)
        email_e.delete(0, END)
        first_name_e.focus()
        view_all()

def clear():
    first_name_e.delete(0,END)
    last_name_e.delete(0, END)
    age_e.delete(0, END)
    address_e.delete(0, END)
    dob_e.delete(0, END)
    phone_e.delete(0, END)
    email_e.delete(0,END)
    first_name_e.focus()
def clear_fuc():
    scrolled_text.delete("1.0",END)
    first_name_e.focus()
def view_all():
    cur.execute("SELECT * from userdata")
    data = cur.fetchall()
    for i in data:
        tree_view.insert("",END,values = i)
def search_fuc(first):
    global r
    cur.execute(F"SELECT * FROM userdata WHERE first = '{first}'")
    r = cur.fetchall()
    return r
def se():
    name = search_e.get()
    search_fuc(name)
    a = r[0]
    result_3 = F"\t\tInformation\n\n First Name : {a[1]} \n Last Name : {a[2]} \n email : {a[3]} \n Age : {a[4]} \n Address : {a[5]} \n Mob. no. : {a[6]} \n DOB : {a[7]} "
    display_search.insert(END, result_3)
    search_e.delete(0,END)
def clr():
    display_search.delete("1.00",END)
def export_csv():
    os.chdir("E:/New folder")
    file = str(file_name_e.get())
    myfile = file + '.csv'
    with open(myfile,'w') as f:
        writer = csv.writer(f)
        cur.execute("SELECT * from userdata")
        d = cur.fetchall()
        writer.writerow(['ID','first','last','email','age','address','mob_no','DOB'])
        writer.writerows(d)


tab_control = ttk.Notebook(root,style = "lefttab.TNotebook")
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

tab_control.add(tab1,text = F'{"Home " :^20s}')
tab_control.add(tab2,text = F'{"view " :^20s}')
tab_control.add(tab3,text = F'{"Search ": ^20s}')
tab_control.add(tab4,text = F'{"Export " :^20s}')
tab_control.add(tab5,text = F'{"about " :^20s}')
tab_control.pack(expand = 1,fill = "both")

#===============tab1 labels===========================#
first_name_l = Label(tab1,text = "First name ", font = ("Calibri Light" , 11))
first_name_l.place(x = 20,y = 20)

last_name_l = Label(tab1,text = "last name ", font = ("Calibri Light" , 11))
last_name_l.place(x = 20,y = 60)

email_l = Label(tab1,text = "email ", font = ("Calibri Light" , 11))
email_l.place(x = 20,y = 100)

age_l = Label(tab1,text = "Age ", font = ("Calibri Light" , 11))
age_l.place(x = 20,y = 140)

address_l = Label(tab1,text = "Address ", font = ("Calibri Light" , 11))
address_l.place(x = 20,y = 180)

phone_l = Label(tab1,text = "Mob no. ", font = ("Calibri Light" , 11))
phone_l.place(x = 20,y = 220)

dob_e = Label(tab1,text = "Date of birth ", font = ("Calibri Light" , 11))
dob_e.place(x = 20,y = 260)

#==================Entry=================#

first_name_e = Entry(tab1, font = ("Calibri Light" , 12))
first_name_e.place(x = 150,y = 20)

last_name_e = Entry(tab1, font = ("Calibri Light" , 12))
last_name_e.place(x = 150,y = 60)

email_e = Entry(tab1, font = ("Calibri Light" , 12))
email_e.place(x = 150,y = 100)

age_e = Entry(tab1, font = ("Calibri Light" , 12))
age_e.place(x = 150,y = 140)

address_e = Entry(tab1, font = ("Calibri Light" , 12))
address_e.place(x = 150,y = 180)

phone_e = Entry(tab1, font = ("Calibri Light" , 12))
phone_e.place(x = 150,y = 220)

dob_e = Entry(tab1, font = ("Calibri Light" , 12))
dob_e.place(x = 150,y = 260)

scrolled_text = ScrolledText(tab1,width = 30,height = 15)
scrolled_text.place(x = 400 , y = 50)

#=================Tab1 Buttons====================#

add_b = Button( tab1,text = "  Add  ",font = ("Calibri Light" , 12),bg = "steel blue",fg = "white",command = adition)
add_b.place(x = 150,y = 300)

clear_b = Button( tab1,text = "  clear  ",font = ("Calibri Light" , 12),bg = "steel blue",fg = "white",command = clear)
clear_b.place(x = 250,y = 300)

clear_result_b = Button( tab1,text = " 🔄 ",font = ("Calibri Light" , 10),bg = "white",fg = "black",command = clear_fuc)
clear_result_b.place(x = 500,y = 300)

#==========================Tab2   (view)   =============================#

view_all_b = Button( tab2,text = "  View all  ",font = ("Calibri Light" , 10),bg = "steel blue",fg = "white",command = view_all)
view_all_b.place(x = 350,y = 20)

tree_view = ttk.Treeview(tab2,column = ("column1","column2","column3","column4","column5","column6","column7"),show = "headings")
tree_view.heading("#1",text = "First Name")
tree_view.heading("#2",text = "Last Name")
tree_view.heading("#3",text = "em@il")
tree_view.heading("#4",text = "Age")
tree_view.heading("#5",text = "Address")
tree_view.heading("#6",text = "Mob no.")
tree_view.heading("#7",text = "DOB")
tree_view.place(x = 10, y = 50)

#====================Tab3 (Search) ======================#

search_l = Label(tab3,text = "Search Name ", font = ("Calibri Light" , 11))
search_l.place(x = 200,y = 50)

search_e = Entry(tab3, font = ("Calibri Light" , 12))
search_e.place(x = 300,y = 50)

find_b = Button( tab3,text = "  Find  ",font = ("Calibri Light" , 10),bg = "steel blue",fg = "white",command= se)
find_b.place(x = 480,y = 48)

display_search = ScrolledText(tab3,width = 40,height = 10)
display_search.place(x = 210, y = 120)

clear_search_b = Button( tab3,text = "Clear Search",font = ("Calibri Light" , 10),bg = "steel blue",fg = "white",command = clr)
clear_search_b.place(x = 320,y = 300)

#=====================Tab 4 (Export) ===========================#

file_name_l = Label(tab4,text = "File Name ", font = ("Calibri Light" , 11))
file_name_l.place(x = 200,y = 150)

file_name_e = Entry(tab4, font = ("Calibri Light" , 12))
file_name_e.place(x = 300,y = 150)

ex_to_csv = Button( tab4,text = " Export to CSV ",font = ("Calibri Light" , 10),bg = "steel blue",fg = "white",command= export_csv)
ex_to_csv.place(x = 280,y = 200)

ex_to_xls = Button(tab4,text = " Export to XLS ",font = ("Calibri Light" , 10),bg = "steel blue",fg = "white")
ex_to_xls.place(x = 390,y = 200)


root.mainloop()