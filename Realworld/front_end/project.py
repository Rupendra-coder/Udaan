from tkinter import *
from tkinter import ttk

class Main_Interface(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.geometry('950x500')
        self.root.title('Registration')
        self.back = PhotoImage(file='back1.png')
        self.searchimg = PhotoImage(file='search.png')
        self.MainFrame = Frame(self.root, bg='#f0f8ff')
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.MainFrame.place(x=0, y=0, width=950, height=900)
        Heading = Label(self.MainFrame, text='Udaan', font=('ariel', 20, 'bold'), fg='#0262AC')
        Heading.place(x=0, y=0)
        Heading1 = Label(self.MainFrame, text='Comfortable And Safe Journey', font=('ariel', 10, 'bold'), fg='#0262AC')
        Heading1.place(x=0, y=50)
        logo = Label(self.MainFrame, image=self.back, bg='aliceblue')
        logo.place(x=50, y=80)
        search_by = Label(self.MainFrame, text='Search By', font=('ariel', 15)).place(x=500, y=20)
        txt_Search = Entry(self.MainFrame, width=15, font=('ariel', 13), textvariable=self.search_txt, bd=5,
                           relief=GROOVE)
        txt_Search.place(x=715, y=50)
        self.search_by = StringVar()

        combo_Search = ttk.Combobox(self.MainFrame, textvariable=self.search_by, width=20, font=('ariel', 13),
                                    state='readonly')
        combo_Search['values'] = ('Airline_Name', 'Departure_City')
        combo_Search.place(x=500, y=53)
        showallbtn = Button(self.MainFrame, text='Show All', font=('arial', 13)).place(x=800,y=15)
        clearbtn = Button(self.MainFrame, text='Clear', font=('arial', 13)).place(x=740, y=15)

        ############Table and Picture in Main Frame##################
        LtsOffer = Label(self.MainFrame, text='Latest Offer', font=('arial', 20, 'bold'), bg='aliceblue').place(x=720,
                                                                                                                y=150)
        self.offerimg = PhotoImage(file='offer.png')
        logo = Label(self.MainFrame, image=self.offerimg, bg='aliceblue').place(x=650, y=190)
        Title = Label(self.MainFrame, text='Today Schedule', font=('ariel', 20, 'bold'), fg='#87ceeb')
        Title.place(x=25, y=150)
        self.ShowDetailFrame = Frame(self.MainFrame, bg='#0262AC')
        self.ShowDetailFrame.place(x=25, y=200, height=250, width=600)
        scroll_x = Scrollbar(self.ShowDetailFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.ShowDetailFrame, orient=VERTICAL, bg='white')
        self.Flight_Table = ttk.Treeview(self.ShowDetailFrame,
                                         columns=('aName', 'from', 'to', 'dTime', 'aTime'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Flight_Table.xview)
        scroll_y.config(command=self.Flight_Table.yview)
        self.Flight_Table.heading('aName', text='Air Name')
        self.Flight_Table.heading('from', text='From')
        self.Flight_Table.heading('to', text='To')
        self.Flight_Table.heading('dTime', text='Departure Time')
        self.Flight_Table.heading('aTime', text='Arrival Time')
        self.Flight_Table['show'] = 'headings'
        self.Flight_Table.column('aName', width=100)
        self.Flight_Table.column('from', width=100)
        self.Flight_Table.column('to', width=100)
        self.Flight_Table.column('dTime', width=150)
        self.Flight_Table.column('aTime', width=150)
        self.Flight_Table.pack(fill=BOTH, expand=1)

        ################ Button of Mainframe ###############
        Button_Frame = Frame(self.MainFrame, bd=4, relief=RIDGE, bg='aliceblue')
        Button_Frame.place(x=480, y=90, width=400)
        loginbtn = Button(Button_Frame, text='Login', width=10,command=self.click_login
                          ).grid(row=0, column=0, padx=10, pady=10)
        regstrbtn = Button(Button_Frame, text='Registration', width=10,
                           command=self.click_register).grid(row=0, column=1, padx=10, pady=10)
        schdlbtn = Button(Button_Frame, text='Schedule', width=10,
                          ).grid(row=0, column=2, padx=10, pady=10)
        cnctbtn = Button(Button_Frame, text='Contact', width=10,command=self.click_contact
                         ).grid(row=0, column=3, padx=10, pady=10)
        self.srchbtn = Button(self.MainFrame, image=self.searchimg, width=15, height=20)
        self.srchbtn.config(image=self.searchimg, compound=TOP)
        self.srchbtn.place(x=860, y=50)

    def click_login(self):
        window = Toplevel()
        Login(window)
        self.root.withdraw()

    def click_register(self):
        window = Toplevel()
        Register(window)
        self.root.withdraw()

    def click_contact(self):
        window = Toplevel()
        Contact(window)
        self.root.withdraw()

class Login(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.title('Admin and User Login')
        self.root.geometry('550x350')
        self.loginframe = Frame(self.root)
        self.loginframe.place(x=0, y=0, width=550, height=350)
        Heading = Label(self.loginframe, text='Login', font=('ariel', 20, 'bold'), fg='#0262AC')
        Heading.grid(row=0,column=3)


        self.back=PhotoImage(file='back.png')
        logo=Label(self.loginframe,image=self.back,bg='aliceblue')
        logo.place(x=0,y=150)

        self.UserName = Label(self.loginframe, text='Username : ', bg='aliceblue')
        self.UserName.grid(row=2,column=1)
        self.UserName_entry = Entry(self.loginframe, bd=5,relief=GROOVE)
        self.UserName_entry.grid(row=2,column=2)
        self.password = Label(self.loginframe, text='Password : ', bg='aliceblue')
        self.password.grid(row=3,column=1)
        self.password_entry = Entry(self.loginframe,show='*', bd=5,relief=GROOVE)
        self.password_entry.grid(row=3,column=2)

        ######################Button_Frame##################

        Button_Frame = Frame(self.loginframe, bd=4, relief=RIDGE, bg='aliceblue')
        Button_Frame.place(x=50, y=90, width=330)
        self.adminloginbtn = Button(Button_Frame, text='Admin Login', bg='white',
                                    command=self.click_Admin).grid(row=0,column=0,padx=10, pady=10)
        self.clearbtn = Button(Button_Frame, text='Clear',
                               bg='white').grid(row=0,column=1,padx=10, pady=10)
        self.Userloginbtn = Button(Button_Frame, text='User Login', bg='white',
                                   command=self.click_ULogin).grid(row=0,column=2,padx=10, pady=10)
        self.homebtn = Button(Button_Frame, text='Home', bg='white',
                              command=self.click_home).grid(row=0,column=3,padx=10, pady=10)

    def click_home(self):
        window=Toplevel()
        Main_Interface(window)
        self.root.withdraw()

    def click_Admin(self):
        window = Toplevel()
        Admin(window)
        self.root.withdraw()

    def click_ULogin(self):
        window = Toplevel()
        ULogin(window)
        self.root.withdraw()

class ULogin:
    def __init__(self, root,UserName):
        self.root = root
        self.UserName=UserName
        self.root.geometry('950x550')
        self.root.title('User Page')
        self.Ulogin_frame = Frame(self.root)
        self.Ulogin_frame.place(x=0, y=0, width=950, height=900)
        Heading = Label(self.Ulogin_frame, text='Welcome User', font=('ariel', 20, 'bold'), fg='#0262AC').grid(row=0, column=3)


        Title = Label(self.Ulogin_frame, text='Schedule Table', font=('ariel', 20, 'bold'), fg='#87ceeb')
        Title.place(x=25, y=50)
        self.ShowDetailFrame = Frame(self.Ulogin_frame, bg='#0262AC')
        self.ShowDetailFrame.place(x=25, y=100, height=250, width=900)
        scroll_x = Scrollbar(self.ShowDetailFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.ShowDetailFrame, orient=VERTICAL, bg='white')
        self.Schedule_Table = ttk.Treeview(self.ShowDetailFrame,
                                           columns=('sID', 'fname', 'dtime', 'atime', 'seat', 'dcity', 'descity','status'),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Schedule_Table.xview)
        scroll_y.config(command=self.Schedule_Table.yview)
        self.Schedule_Table.heading('sID', text='Schedule ID')
        self.Schedule_Table.heading('fname', text='Flight Name')
        self.Schedule_Table.heading('dtime', text='Departure Time')
        self.Schedule_Table.heading('atime', text='Arrival Time')
        self.Schedule_Table.heading('seat', text='Seat')
        self.Schedule_Table.heading('dcity', text='Departure City')
        self.Schedule_Table.heading('descity', text='Destination')
        self.Schedule_Table.heading('status', text='Status')


class Admin(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.root.geometry('550x350')
        self.root.title('Admin Page')
        self.Adminframe = Frame(self.root)
        self.Adminframe.place(x=0, y=0, width=550, height=350)
        Heading = Label(self.Adminframe, text='Welcome Admin', font=('ariel', 20, 'bold'), fg='#0262AC')
        Heading.grid(row=0, column=3)

        self.back = PhotoImage(file='Admin.png')
        logo = Label(self.Adminframe, image=self.back, bg='aliceblue')
        logo.place(x=100, y=80)

        #####################Button Frame################

        Button_Frame = Frame(self.Adminframe, bd=4, relief=RIDGE, bg='aliceblue')
        Button_Frame.place(x=5, y=50, height=200)
        flightbtn = Button(Button_Frame, text='Flight', width=10,
                           ).grid(row=1,column=0,padx=10, pady=10)

        schedulebtn = Button(Button_Frame, text='Schedule', width=10,
                             ).grid(row=2,column=0,padx=10, pady=10)
        reportbtn = Button(Button_Frame, text='Report', width=10,
                           ).grid(row=3,column=0,padx=10, pady=10)
        backbtn = Button(Button_Frame, text='Log Out', width=10,
                         command=self.click_home).grid(row=4, column=0,padx=10, pady=10)
    def click_home(self):
        window = Toplevel()
        Login(window)
        self.root.withdraw()

    def click_flight(self):
        window = Toplevel()
        Flight(window)
        self.root.withdraw()


    def click_schedule(self):
        window = Toplevel()
        Schedule(window)
        self.root.withdraw()

    def click_report(self):
        window = Toplevel()
        Report(window)
        self.root.withdraw()




    def click_AP(self):
        window = Toplevel()
        Admin(window)
        self.root.withdraw()

class Flight:
    def __init__(self, root):
        self.root = root
        self.root.geometry('950x550')
        self.root.title('Flight Page')
        self.Flight_frame = Frame(self.root)
        self.Flight_frame.place(x=0, y=0, width=950, height=900)
        Heading = Label(self.Flight_frame, text='Welcome to Flight Page', font=('ariel', 20, 'bold'), fg='#0262AC')
        Heading.grid(row=0, column=3)

        Title = Label(self.Flight_frame, text='Flight Table', font=('ariel', 20, 'bold'), fg='#87ceeb')
        Title.place(x=25, y=50)
        self.ShowDetailFrame = Frame(self.Flight_frame, bg='#0262AC')
        self.ShowDetailFrame.place(x=25, y=100, height=250, width=600)
        scroll_x = Scrollbar(self.ShowDetailFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.ShowDetailFrame, orient=VERTICAL, bg='white')
        self.Flight_Table = ttk.Treeview(self.ShowDetailFrame,
                                         columns=('fid','arName', 'tseat'),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Flight_Table.xview)
        scroll_y.config(command=self.Flight_Table.yview)
        self.Flight_Table.heading('fid', text='Flight ID')
        self.Flight_Table.heading('arName', text='Airlines Name')
        self.Flight_Table.heading('tseat', text='Total Seats')

        self.Flight_Table['show'] = 'headings'
        self.Flight_Table.column('fid', width=200)
        self.Flight_Table.column('arName', width=200)
        self.Flight_Table.column('tseat', width=200)

        self.name = Label(self.Flight_frame, text='Name', font=('ariel', 15)).place(x=0, y=400)
        self.name_entry = Entry(self.Flight_frame, bd=5, relief=GROOVE)
        self.name_entry.place(x=150, y=400)
        self.tseat = Label(self.Flight_frame, text='Total Seat', font=('ariel', 15)).place(x=0, y=430)
        self.tseat_entry = Entry(self.Flight_frame, bd=5, relief=GROOVE)
        self.tseat_entry.place(x=150, y=430)
        self.donebtn = Button(self.Flight_frame, text='Done', width=10).place(x=350, y=490)
        self.backbtn = Button(self.Flight_frame, text='Back', width=10, command=self.click_back).place(x=450, y=490)
        self.updatebtn = Button(self.Flight_frame, text='Update', width=10).place(x=550, y=490)
        self.deletbtn = Button(self.Flight_frame, text='Delete').place(x=650, y=490)

    def click_back(self):
        window = Toplevel()
        Admin(window)
        self.root.withdraw()

class Schedule:
    def __init__(self, root):
        self.root = root
        self.root.geometry('950x550')
        self.root.title('Schedule Page')
        self.Schedule_frame = Frame(self.root)
        self.Schedule_frame.place(x=0, y=0, width=950, height=900)
        Heading = Label(self.Schedule_frame, text='Welcome to Schedule Page', font=('ariel', 20, 'bold'), fg='#0262AC')
        Heading.grid(row=0, column=3)

        Title = Label(self.Schedule_frame, text='Schedule Table', font=('ariel', 20, 'bold'), fg='#87ceeb')
        Title.place(x=25, y=50)
        self.ShowDetailFrame = Frame(self.Schedule_frame, bg='#0262AC')
        self.ShowDetailFrame.place(x=25, y=100, height=250, width=900)
        scroll_x = Scrollbar(self.ShowDetailFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.ShowDetailFrame, orient=VERTICAL, bg='white')
        self.Schedule_Table = ttk.Treeview(self.ShowDetailFrame,
                                        columns=('sID', 'fname', 'dtime', 'atime','dcity','descity','ttime','book','status'),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Schedule_Table.xview)
        scroll_y.config(command=self.Schedule_Table.yview)
        self.Schedule_Table.heading('sID', text='Schedule ID')
        self.Schedule_Table.heading('fname', text='Flight Name')
        self.Schedule_Table.heading('dtime', text='Departure Time')
        self.Schedule_Table.heading('atime', text='Arrival Time')
        self.Schedule_Table.heading('dcity', text='Departure City')
        self.Schedule_Table.heading('descity', text='Destination City')
        self.Schedule_Table.heading('ttime', text='Total Time')
        self.Schedule_Table.heading('book', text='Booked')
        self.Schedule_Table.heading('status', text='Status')

        self.Schedule_Table['show'] = 'headings'
        self.Schedule_Table.column('sID', width=80)
        self.Schedule_Table.column('fname', width=80)
        self.Schedule_Table.column('dtime', width=80)
        self.Schedule_Table.column('atime', width=80)
        self.Schedule_Table.column('dcity', width=80)
        self.Schedule_Table.column('descity', width=85)
        self.Schedule_Table.column('ttime', width=85)
        self.Schedule_Table.column('book', width=85)
        self.Schedule_Table.column('status', width=85)
        self.Schedule_Table.pack(fill=BOTH, expand=1)

        self.name = Label(self.Schedule_frame, text='Flight Name', font=('ariel', 15)).place(x=0, y=350)
        combo_Search = ttk.Combobox(self.Schedule_frame, textvariable=self.flight, width=10, font=('', 13),
                                    state='readonly')
        combo_Search['values'] = flight_name
        combo_Search.place(x=150, y=350)

        self.Dtime = Label(self.Schedule_frame, text='Departure Time', font=('ariel', 15)).place(x=0, y=380)
        self.Dtime_entry = Entry(self.Schedule_frame, bd=5, relief=GROOVE)
        self.Dtime_entry.place(x=150, y=380)
        self.atime = Label(self.Schedule_frame, text='Arrival Time', font=('ariel', 15)).place(x=290, y=380)
        self.atime_entry = Entry(self.Schedule_frame, bd=5, relief=GROOVE)
        self.atime_entry.place(x=450, y=380)
        self.dcity = Label(self.Schedule_frame, text='Departure City', font=('ariel', 15)).place(x=0, y=410)
        self.dcity_entry = Entry(self.Schedule_frame, bd=5, relief=GROOVE)
        self.dcity_entry.place(x=150, y=410)
        self.descity = Label(self.Schedule_frame, text='Destination City', font=('ariel', 15)).place(x=290, y=410)
        self.descity_entry = Entry(self.Schedule_frame, bd=5, relief=GROOVE)
        self.descity_entry.place(x=450, y=410)
        self.ttime = Label(self.Schedule_frame, text='Total Time', font=('ariel', 15)).place(x=0, y=440)
        self.ttime_entry = Entry(self.Schedule_frame, bd=5, relief=GROOVE)
        self.ttime_entry.place(x=150, y=440)
        self.sts = Label(self.Schedule_frame, text='Status', font=('ariel', 15)).place(x=0, y=470)
        self.sts_entry = Entry(self.Schedule_frame, bd=5, relief=GROOVE)
        self.sts_entry.place(x=150, y=470)
        self.donebtn = Button(self.Schedule_frame, text='Done', width=10).place(x=280, y=500)
        self.backbtn = Button(self.Schedule_frame, text='Back', width=10, command=self.click_back).place(x=370, y=500)
        self.deletebtn = Button(self.Schedule_frame, text='Update', width=10).place(x=180, y=500)

    def click_back(self):
        window = Toplevel()
        Admin(window)
        self.root.withdraw()
class Report:
    def __init__(self, root):
        self.root = root
        self.root.geometry('950x550')
        self.root.title('Report Page')
        self.dbconnect=DbConnection()
        self.Report_frame = Frame(self.root)
        self.Report_frame.place(x=0, y=0, width=950, height=550)
        Heading = Label(self.Report_frame, text='Welcome to Report Page', font=('ariel', 20, 'bold'), fg='#0262AC')
        Heading.grid(row=0, column=3)


        #####################For_Airport_Status########################
        Title = Label(self.Report_frame, text='Airline Status', font=('ariel', 15, 'bold'), fg='#87ceeb')
        Title.place(x=25, y=50)
        self.ShowDetailFrame = Frame(self.Report_frame, bg='#0262AC')
        self.ShowDetailFrame.place(x=25, y=100, height=150, width=900)
        scroll_x = Scrollbar(self.ShowDetailFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.ShowDetailFrame, orient=VERTICAL, bg='white')
        self.AP_Table = ttk.Treeview(self.ShowDetailFrame,
                                           columns=('arname','dcity','descity','status','tseat'),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AP_Table.xview)
        scroll_y.config(command=self.AP_Table.yview)
        self.AP_Table.heading('arname', text='Airline Name')
        self.AP_Table.heading('dcity', text='Departure City')
        self.AP_Table.heading('descity', text='Destination City')
        self.AP_Table.heading('tseat', text='Total Seat')
        self.AP_Table.heading('status', text='Status')

        self.AP_Table['show'] = 'headings'
        self.AP_Table.column('arname', width=100)
        self.AP_Table.column('dcity', width=100)
        self.AP_Table.column('descity', width=100)
        self.AP_Table.column('tseat', width=100)
        self.AP_Table.column('status', width=100)
        self.AP_Table.pack(fill=BOTH, expand=1)
        Title = Label(self.Report_frame, text='Total Bookings and Cancelled', font=('ariel', 15, 'bold'), fg='#87ceeb')
        Title.place(x=25, y=250)
        self.ShowDetailFrame = Frame(self.Report_frame, bg='#0262AC')
        self.ShowDetailFrame.place(x=25, y=290, height=100, width=900)
        scroll_x = Scrollbar(self.ShowDetailFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.ShowDetailFrame, orient=VERTICAL, bg='white')
        self.TB_Table = ttk.Treeview(self.ShowDetailFrame,
                                     columns=('fn', 'tb', 'dcity', 'descity', 'sts'),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.TB_Table.xview)
        scroll_y.config(command=self.TB_Table.yview)
        self.TB_Table.heading('fn', text='Flight Name')
        self.TB_Table.heading('tb', text='Total Booking')
        self.TB_Table.heading('dcity', text='Departure City')
        self.TB_Table.heading('descity', text='Destination City')
        self.TB_Table.heading('sts', text='Status')

        self.TB_Table['show'] = 'headings'
        self.TB_Table.column('fn', width=85)
        self.TB_Table.column('tb', width=85)
        self.TB_Table.column('dcity', width=85)
        self.TB_Table.column('descity', width=85)
        self.TB_Table.column('sts', width=85)
        self.TB_Table.pack(fill=BOTH, expand=1)

        # ######################For Total Report##############
        Title = Label(self.Report_frame, text='Report Received', font=('ariel', 15, 'bold'), fg='#87ceeb')
        Title.place(x=25, y=380)
        self.ShowDetailFrame = Frame(self.Report_frame, bg='#0262AC')
        self.ShowDetailFrame.place(x=25, y=420, height=75, width=900)
        scroll_x = Scrollbar(self.ShowDetailFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.ShowDetailFrame, orient=VERTICAL, bg='white')
        self.TC_Table = ttk.Treeview(self.ShowDetailFrame,
                                     columns=('sid', 'name', 'eadrs', 'sbjt', 'msg'),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.TC_Table.xview)
        scroll_y.config(command=self.TC_Table.yview)
        self.TC_Table.heading('sid', text='Schedule ID')
        self.TC_Table.heading('name', text='Name')
        self.TC_Table.heading('eadrs', text='Email Address')
        self.TC_Table.heading('sbjt', text='Subject')
        self.TC_Table.heading('msg', text='Message')

        self.TC_Table['show'] = 'headings'
        self.TC_Table.column('sid', width=100)
        self.TC_Table.column('name', width=100)
        self.TC_Table.column('eadrs', width=100)
        self.TC_Table.column('sbjt', width=100)
        self.TC_Table.column('msg', width=100)
        self.TC_Table.pack(fill=BOTH, expand=1)

    def click_AP(self):
        window = Toplevel()
        Admin(window)
        self.root.withdraw()
class Contact:
    def __init__(self, root):
        self.root = root
        self.root.title('Contact Page')
        self.root.geometry('500x250')
        self.Contact_frame = Frame(self.root)
        self.Contact_frame.place(x=0, y=0, width=400, height=250)
        Heading = Label(self.Contact_frame, text='Contact Page', font=('ariel', 20, 'bold'), fg='#0262AC').grid(row=0,column=1)
        self.Name=StringVar()
        self.Email=StringVar()
        self.Subject=StringVar()
        self.name=Label(self.Contact_frame,text='Name',font=('arial',10)).grid(row=1,column=0)
        self.name_entry=Entry(self.Contact_frame, bd=5,relief=GROOVE,textvariable=self.Name)
        self.name_entry.grid(row=1,column=1)
        self.email=Label(self.Contact_frame,text='Email Address',font=('Arial',10)).grid(row=2,column=0)
        self.email_entry=Entry(self.Contact_frame, bd=5,relief=GROOVE,textvariable=self.Email)
        self.email_entry.grid(row=2,column=1)
        self.subject=Label(self.Contact_frame,text='Subject',font=('arial',10)).grid(row=3,column=0)
        self.subject_entry=Entry(self.Contact_frame, bd=5,relief=GROOVE,textvariable=self.Subject)
        self.subject_entry.grid(row=3,column=1)
        self.message=Label(self.Contact_frame,text='Message',font=('arial',10)).grid(row=4,column=0)
        self.txt_message=Text(self.Contact_frame,width=30,height=4,font=('',10), bd=5,relief=GROOVE)
        self.txt_message.grid(row=4,column=1,sticky=E)
        self.backbtn = Button(self.Contact_frame, text='Back', bd=5,
                           relief=RIDGE, command=self.click_home).grid(row=5, column=0)
        self.sbtbtn = Button(self.Contact_frame, text='Submit', bd=5,
                              relief=RIDGE).grid(row=5, column=2)
        self.clearbtn=Button(self.Contact_frame,text='CLear',command=self.clear, bd=5,
                           relief=RIDGE).grid(row=5,column=1)

        self.back = PhotoImage(file='Contact.png')

        logo = Label(self.Contact_frame, image=self.back, bg='aliceblue')
        # logo.grid(row=1,column=3)
        logo.place(x=300, y=15)

    def clear(self):
        self.Name.set('')
        self.Email.set('')
        self.Subject.set('')
        self.txt_message.delete('1.0', END)

    def click_home(self):
        window = Toplevel()
        Main_Interface(window)
        self.root.withdraw()
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Register Page')
        self.root.geometry('500x300')
        self.Register_frame = Frame(self.root)
        self.Register_frame.place(x=0, y=0, width=450, height=350)
        Heading = Label(self.Register_frame, text='User Registration', font=('ariel', 20, 'bold'), fg='#0262AC').grid(row=0,column=1)

        self.back = PhotoImage(file='Register.png')
        logo = Label(self.Register_frame, image=self.back, bg='aliceblue')
        logo.place(x=280, y=10)

        self.Username=StringVar()
        self.Firstname=StringVar()
        self.Lastname = StringVar()
        self.Contact=StringVar()
        self.Address = StringVar()
        self.Password = StringVar()
        self.ConfirmPassword=StringVar()

        uname=Label(self.Register_frame,text='User Name',font=('arial',10)).grid(row=1,column=0)
        uname_entry=Entry(self.Register_frame,textvariable=self.Username, bd=5,relief=GROOVE)
        uname_entry.grid(row=1,column=1)
        fname = Label(self.Register_frame, text='First Name', font=('arial', 10)).grid(row=2, column=0)
        fname_entry = Entry(self.Register_frame,textvariable=self.Firstname, bd=5,relief=GROOVE)
        fname_entry.grid(row=2, column=1)
        lname = Label(self.Register_frame, text='Last Name', font=('arial', 10)).grid(row=3, column=0)
        lname_entry = Entry(self.Register_frame,textvariable=self.Lastname, bd=5,relief=GROOVE)
        lname_entry.grid(row=3, column=1)
        cno=Label(self.Register_frame,text='Contact No',font=('arial',10)).grid(row=4,column=0)
        cno_entry=Entry(self.Register_frame,textvariable=self.Contact, bd=5,relief=GROOVE)
        cno_entry.grid(row=4,column=1)
        adrs=Label(self.Register_frame,text='Address',font=('arial',10)).grid(row=5,column=0)
        adrs_entry=Entry(self.Register_frame,textvariable=self.Address, bd=5,relief=GROOVE)
        adrs_entry.grid(row=5,column=1)
        pwd=Label(self.Register_frame,text='Password',font=('arial',10)).grid(row=6,column=0)
        pwd_entry=Entry(self.Register_frame,show='*',textvariable=self.Password, bd=5,relief=GROOVE)
        pwd_entry.grid(row=6,column=1)
        cpwd=Label(self.Register_frame,text='Confirm Password',font=('arial',10)).grid(row=7,column=0)
        cpwd_entry=Entry(self.Register_frame,show='*',textvariable=self.ConfirmPassword, bd=5,relief=GROOVE)
        cpwd_entry.grid(row=7,column=1)
        rgrbtn=Button(self.Register_frame,text='Register').grid(row=8,column=2)
        backbtn=Button(self.Register_frame,text='Back',command=self.click_home).grid(row=8,column=0)
        clearbtn=Button(self.Register_frame,text='Clear',command=self.clear).grid(row=8,column=1)
    def clear(self):
        self.Username.set('')
        self.Firstname.set('')
        self.Lastname.set('')
        self.Contact.set('')
        self.Address.set('')
        self.Password.set('')
        self.ConfirmPassword.set('')

    def click_home(self):
        window = Toplevel()
        Main_Interface(window)
        self.root.withdraw()





window = Tk()
Main_Interface(window)
window.mainloop()
