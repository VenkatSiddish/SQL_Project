from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add Student')
        self.canvas = Canvas(width=500, height=417, bg='gray')
        self.canvas.pack()
        fname = StringVar()
        lname = StringVar()
        cn = StringVar()
        gender = StringVar()
        add = StringVar()
        c = StringVar()
#verifying input
        def asi():
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='crud',
                                                        user='root',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    first = fname.get()
                    last = lname.get()
                    contact = cn.get()
                    gend = gender.get()
                    address = add.get()
                    course = c.get()
                    self.myCursor.execute("Insert into tbl_student(FirstName,LastName,Gender,Address,ContactNumber,Course) values (%s,%s,%s,%s,%s,%s)",[first,last,gend,address,contact,course])
                    self.conn.commit()
                    messagebox.showinfo("Done","Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                    if ask:
                     self.destroy()
                     os.system('%s %s' % (py, 'Add.py'))
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        Label(self, text='Student Details',bg='gray', fg='white', font=('Courier new', 25, 'bold')).pack()
        Label(self, text='First Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=102)
        Entry(self, textvariable=fname, width=30).place(x=200, y=104)
        Label(self, text='Last Name:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=150)
        Entry(self, textvariable=lname, width=30).place(x=200, y=152)
        Label(self, text='Gender:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=200)
        Entry(self, textvariable=gender, width=30).place(x=200, y=202)
        Label(self, text='Address:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=250)
        Entry(self, textvariable=add, width=30).place(x=200, y=250)
        Label(self, text='Contact Number:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=300)
        Entry(self, textvariable=cn, width=30).place(x=200, y=300)
        Label(self, text='Course:', bg='gray', font=('Courier new', 10, 'bold')).place(x=70, y=350)
        Entry(self, textvariable=c, width=30).place(x=200, y=350)
        Button(self, text="Save", bg='blue', width=15, command=asi).place(x=230, y=380)

Add().mainloop()
