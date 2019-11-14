#!/usr/bin/env python

import tkinter as tk

root = tk.Tk()
root.resizable(0,0)
root.geometry('725x573+391+117')
root.title("Login")

bg_color = "#c6db4d"
root.configure(background=bg_color)

row = tk.Frame(root, bg=bg_color)
lab = tk.Label(row, width=27, text="Admin Login", font="-family {gothic} -size 40", anchor='n', fg="chocolate", bg=bg_color)
row.pack(side=tk.TOP, fill="both",padx=5, pady=20)
lab.pack(anchor=tk.CENTER)

row1 = tk.Frame(root,bg=bg_color)
lab1 = tk.Label(row1, width=20, text="Email", font="-family {gothic} -size 20", anchor='w',bg=bg_color)
ent1 = tk.Entry(row1, font="-family {gothic} -size 20")
row1.pack(side=tk.TOP, fill=tk.X,padx=5, pady=10)
lab1.pack(side=tk.LEFT)
ent1.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

row2 = tk.Frame(root,bg=bg_color)
lab2 = tk.Label(row2, width=20, text="Password", font="-family {gothic} -size 20", anchor='w',bg=bg_color)
ent2 = tk.Entry(row2, font="-family {gothic} -size 20",show="*")
row2.pack(side=tk.TOP, fill=tk.X,padx=5, pady=10)
lab2.pack(side=tk.LEFT)
ent2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

button_row1 = tk.Frame(root, bg=bg_color)
button1 = tk.Button(button_row1, text="Login", font="-family {gothic} -size 20", command=None)
button_row1.pack(side=tk.TOP, fill=tk.X, padx=100, pady=25)
button1.pack(anchor='n')

root.mainloop()
