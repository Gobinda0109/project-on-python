
from tkinter import *
from tkinter import messagebox as m
from PIL import Image,ImageTk
import mysql.connector
from mysql.connector import connection
from tkinter import ttk



class PCBuild:
    def __init__(self,root):
        self.root=root
        self.storeName = "PC BUILDING GUIDE"
        titleLabel = Label(root, text=self.storeName, font=('Arial bold', 30), bd=2)
        titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)
        self.j=0
        self.k=0
        self.l=0

        idLabel = Label(root, text="B_ID", font=('Arial bold', 15))
        nameLabel = Label(root, text="U_ID", font=('Arial bold', 15))
        priceLabel = Label(root, text="BUDGET", font=('Arial bold', 15))
        idLabel.grid(row=1, column=4, padx=10, pady=10)
        nameLabel.grid(row=2, column=4, padx=10, pady=10)
        priceLabel.grid(row=3, column=4, padx=10, pady=10)


        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.entryB_Id = Entry(root, width=25, textvariable=self.var1, bd=5, font=('Arial bold', 15))
        self.entryU_Id = Entry(root, width=25, textvariable=self.var2, bd=5, font=('Arial bold', 15))
        self.entryPrice = Entry(root, width=25, textvariable=self.var3, bd=5, font=('Arial bold', 15))

        self.entryB_Id.grid(row=1, column=5, columnspan=3, padx=5, pady=5)
        self.entryU_Id.grid(row=2, column=5, columnspan=3, padx=5, pady=5)
        self.entryPrice.grid(row=3, column=5, columnspan=3, padx=5, pady=5)

        print(self.entryB_Id.get(), self.entryU_Id.get(), self.entryPrice.get())

        buttonUpdate = Button(
            root, text="SHOW RECOMMENDATION", padx=5, pady=5, width=25,
            bd=5, font=('Arial', 15), bg="BLUE", command=self.Show)
        buttonUpdate.grid(row=4, column=6, columnspan=1)
        buttoninfo = Button(
            root, text="HOW TO USE", padx=5, pady=5, width=25,
            bd=5, font=('Arial', 15), bg="BLUE", command=self.Info)
        buttoninfo.grid(row=6, column=6, columnspan=1)

    def Info(self):
        root = Tk()
        root.title("PC Building Guide")
        root.iconbitmap('Icons-Land-Vista-Hardware-Devices-Computer.ico')
        T = Text(root, height=5, width=52)
        Fact = """*** for build type 1 for intel and 2 for amd\n*** for user type 1 is basic 2 is gamer and 3 is for prefessional
                        """
        T.grid(row=5, column=4, padx=10, pady=10)
        T.insert(tk.END, Fact)

    def Show(self):
        root = Tk()
        root.title("PC Building Guide")
        root.iconbitmap('Icons-Land-Vista-Hardware-Devices-Computer.ico')
        root.geometry("600x620+440+90")
        host = "localhost"
        user = "root"
        password = "tokan0109"
        dbname = "PCbuild"

        def create_connection(host_name, user_name, user_password, db_name):
            connection = None
            try:
                connection = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    passwd=user_password,
                    database=db_name
                )
                print("Database Connection Established")
            except:
                print("Error Connecting from Database")
            return connection



        self.j = int(self.entryB_Id.get())
        self.k = int(self.entryU_Id.get())
        self.l = int(self.entryPrice.get())
        print(self.entryB_Id.get(),self.entryU_Id.get(), self.entryPrice.get())
        print(type(self.entryB_Id.get()),type(self.entryU_Id.get()),type(self.entryPrice.get()))
        my_tree = ttk.Treeview(root)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", foreground="blue", font=('Arial bold', 15))

        my_tree['columns'] = ("CPU", "GPU", "RAM")
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("CPU", anchor=W, width=200)
        my_tree.column("GPU", anchor=W, width=200)
        my_tree.column("RAM", anchor=W, width=100)
        my_tree.heading("CPU", text="CPU", anchor=W)
        my_tree.heading("GPU", text="GPU", anchor=W)
        my_tree.heading("RAM", text="RAM", anchor=W)
        connection = create_connection(host, user, password, dbname)
        cursor = connection.cursor()
        value = (self.j,self.k,self.l)
        query = ("SELECT cpu,gpu,ram FROM PCspecs where b_id=%s and u_id=%s and p_id<=%s") % value
        cursor.execute(query)

        i = 0
        for ro in cursor:
            my_tree.insert('', i, text="", values=(ro[0], ro[1], ro[2]))
            i = i + 1

        my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 15))
        my_tree.grid(row=1, column=20, columnspan=4, rowspan=5, padx=10, pady=10)
        root.mainloop()



def clicked():
    a=txt1.get()
    b=txt2.get()

    validation={'name':'Gobinda','password':'1999'}
    for i in range (1):
        if (a==validation['name']):
            if (b==validation['password']):

                M_window.destroy()
                root = Tk()
                root.title("PC Building Guide")
                root.iconbitmap('Icons-Land-Vista-Hardware-Devices-Computer.ico')
                root.geometry("600x620+440+90")
                ob = PCBuild(root)
                root.mainloop()





            else:
                m.showinfo("validation","invalid")
        else:
            m.showinfo("validation","invalid")




import tkinter as tk

M_window=tk.Tk()
M_window.resizable(0,0)
M_window.title('PC Building Guide')
p=PhotoImage(file='BG.png')
q=PhotoImage(file='button_2.png')

M_window.iconbitmap('Icons-Land-Vista-Hardware-Devices-Computer.ico')
M_window.geometry('600x620+440+90')
my_canvas = Canvas(M_window)
my_canvas.pack(fill=BOTH, expand=True)
my_canvas.create_image(0,0,image=p,anchor=NW)
my_canvas.create_text(200,150,text="USERNAME :",fill="green",font=("times new roman",30))
my_canvas.create_text(200,250,text="PASSWORD :",fill="green",font=("times new roman",30))


txt1=tk.Entry(M_window,width=20)
txt1.place(x=340,y=140)

txt2=tk.Entry(M_window,width=20,show="*")
txt2.place(x=340,y=240)
bt1=tk.Button(M_window,image=q,borderwidth=0,command=clicked)
bt1.place(x=250,y=400)

M_window.mainloop()

