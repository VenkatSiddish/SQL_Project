from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Delete Student")
        self.canvas = Canvas(width=1366, height=768, bg='gray')
        self.canvas.pack()
        a = StringVar()
        def ent():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to delete the Student?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='crud',
                                         user='root',
                                         password='')
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from tbl_student where Stud_ID = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","Student Deleted Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Something goes wrong")
        Label(self, text = "Enter Student Id: ",bg='gray',fg='black',font=('Courier new', 15, 'bold')).place(x = 5,y = 40)
        Entry(self,textvariable = a,width = 20).place(x = 210,y = 44)
        Button(self, text='Delete', width=15, font=('arial', 10),command = ent).place(x=200, y = 90)



Rem().mainloop()