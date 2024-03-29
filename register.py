#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Oct 25, 2019 08:14:32 PM IST  platform: Linux
import os
import sys
from subprocess import call
import MySQLdb

import requests
import json

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import messagebox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import register_support

def click_home():
	global root
	root.destroy()
	root = None
	
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    register_support.set_Tk_var()
    top = registration (root)
    register_support.init(root, top)
    root.mainloop()

w = None
def create_registration(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    register_support.set_Tk_var()
    top = registration (w)
    register_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_registration():
    global w
    w.destroy()
    w = None

class registration:
    def register_farmer(self):
        URL = 'https://www.way2sms.com/api/v1/sendCampaign'
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage, mob):
            req_params = {
            'apikey':'AINXY3O3QCM8XEWBOETF8LUS0AOGFKZY',
            'secret':'FU51KAO5TWL15RJT',
            'usetype':'stage',
            'phone': '91' + mob,
            'message':'You are successfully registered with Being A Farmer',
            'senderid':'farmer'
            }
            return requests.post(reqUrl, req_params)
        l = []
        firstname = self.first_name.get()
        lastname = self.last_name.get()
        gender = self.TCombobox1.get()
        village = self.vill.get()
        mob = self.mob.get()
        aid = self.mob_6.get()
        edu = self.edu.get()
        l.append(firstname)
        l.append(lastname)
        l.append(gender)
        l.append(village)
        l.append(mob)
        l.append(aid)
        l.append(edu)
        for i in l:
            if len(i) == 0:
                
                messagebox.showerror("Registration failure", "All fields are mandatory")
                return
        if not len(l[4]) == 10:
            
            messagebox.showerror("Registration failure", "10 digit Mobile Number required")
            return
        elif not len(l[5]) == 12:
            
            messagebox.showerror("Registration failure", "12 digit Aadhaar Number required")
            return
        try:
            self.cursor_reg.execute("INSERT INTO farmer VALUES (%s, %s, %s, %s, %s, %s, %s)",(aid, firstname, lastname, village, edu, gender, mob))
            self.db_reg.commit()
            
            messagebox.showinfo("Registration Success", firstname + " " + lastname + " is Successfully registered")
            response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text', mob)
            print(response.text)
        except:
            
            messagebox.showerror("Registration failure", "Already Registered")
    def __init__(self, top=None):
    	
        try:
            self.db_reg = MySQLdb.connect("localhost","shivam","","FARMER")
            self.cursor_reg = self.db_reg.cursor()
        except:
    	    print('error')

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family gothic -size 15 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("725x573+391+117")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(0, 0)
        top.title("Registration")
        top.configure(background="#abd8d8")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.345, rely=0.035, height=65, width=229)
        self.Label1.configure(activebackground="#a9ed9f")
        self.Label1.configure(background="#93d891")
        self.Label1.configure(font="-family {gothic} -size 15")
        self.Label1.configure(text='''Register Here''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.124, rely=0.192, height=25, width=99)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(font="-family {gothic} -size 15")
        self.Label2.configure(text='''First Name''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.414, rely=0.192, height=25, width=99)
        self.Label3.configure(activebackground="#61ed6f")
        self.Label3.configure(background="#e0ccce")
        self.Label3.configure(font="-family {gothic} -size 15")
        self.Label3.configure(text='''Last Name''')

        self.gender = tk.Label(top)
        self.gender.place(relx=0.124, rely=0.314, height=25, width=99)
        self.gender.configure(activebackground="#f9f9f9")
        self.gender.configure(font="-family {gothic} -size 15")
        self.gender.configure(text='''Gender''')

        self.village = tk.Label(top)
        self.village.place(relx=0.124, rely=0.454, height=25, width=99)
        self.village.configure(activebackground="#f9f9f9")
        self.village.configure(font="-family {gothic} -size 15")
        self.village.configure(text='''Village''')

        self.mobile_no = tk.Label(top)
        self.mobile_no.place(relx=0.124, rely=0.576, height=25, width=99)
        self.mobile_no.configure(activebackground="#f9f9f9")
        self.mobile_no.configure(font="-family {gothic} -size 15")
        self.mobile_no.configure(text='''Mobile No''')

        self.education = tk.Label(top)
        self.education.place(relx=0.414, rely=0.576, height=25, width=99)
        self.education.configure(activebackground="#f9f9f9")
        self.education.configure(font="-family {gothic} -size 15")
        self.education.configure(text='''Education''')

        self.first_name = tk.Entry(top)
        self.first_name.place(relx=0.124, rely=0.244,height=27, relwidth=0.229)
        self.first_name.configure(background="white")
        self.first_name.configure(font=font9)
        self.first_name.configure(selectbackground="#c4c4c4")

        self.last_name = tk.Entry(top)
        self.last_name.place(relx=0.414, rely=0.244,height=27, relwidth=0.229)
        self.last_name.configure(background="white")
        self.last_name.configure(font=font9)
        self.last_name.configure(selectbackground="#c4c4c4")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.vill = tk.Entry(top)
        self.vill.place(relx=0.124, rely=0.506,height=27, relwidth=0.229)
        self.vill.configure(background="white")
        self.vill.configure(font=font9)
        self.vill.configure(selectbackground="#c4c4c4")

        self.mob = tk.Entry(top)
        self.mob.place(relx=0.124, rely=0.628,height=27, relwidth=0.229)
        self.mob.configure(background="white")
        self.mob.configure(font=font9)
        self.mob.configure(selectbackground="#c4c4c4")

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.124, rely=0.698, height=25, width=99)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(font="-family {gothic} -size 15")
        self.Label2_1.configure(text='''Aadhaar No''')

        self.mob_6 = tk.Entry(top)
        self.mob_6.place(relx=0.124, rely=0.75,height=27, relwidth=0.298)
        self.mob_6.configure(background="white")
        self.mob_6.configure(font=font9)
        self.mob_6.configure(selectbackground="#c4c4c4")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.124, rely=0.838, height=32, width=68)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(background="#1cd83b")
        self.Button1.configure(font="-family {gothic} -size 15")
        self.Button1.configure(text='''Home''')
        self.Button1.configure(command=click_home)

        self.Button1_7 = tk.Button(top)
        self.Button1_7.place(relx=0.814, rely=0.838, height=32, width=88)
        self.Button1_7.configure(activebackground="#f9f9f9")
        self.Button1_7.configure(background="#1cd83b")
        self.Button1_7.configure(font="-family {gothic} -size 15")
        self.Button1_7.configure(text='''Register''')
        self.Button1_7.configure(command=self.register_farmer)   

        self.edu = ttk.Combobox(top)
        self.edu.place(relx=0.414, rely=0.628, relheight=0.044, relwidth=0.217)
        self.value_list = ['Uneducated','4th','7th','10th','12th','B.Agri.',]
        self.edu.configure(values=self.value_list)
        self.edu.configure(font=font9)
        self.edu.configure(state='readonly')
        self.edu.configure(takefocus="")

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.124, rely=0.384, relheight=0.044
                , relwidth=0.217)
        self.value_list = ['Male','Female','other',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(font=font9)
        self.TCombobox1.configure(state='readonly')
        self.TCombobox1.configure(textvariable=register_support.combobox)
        self.TCombobox1.configure(background="#ffffff")
        self.TCombobox1.configure(takefocus="")

if __name__ == '__main__':
    vp_start_gui()





