import customtkinter as ctk
from sidebar import *
from tkinter import simpledialog, messagebox
import re
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

text_var4 = ctk.StringVar(value="Bosco SideBar 2.0")
label1 = ctk.CTkLabel(root,height=50,width=750,textvariable=text_var4, font=("Felix Titling", 25, "bold"), 
                      fg_color="darkslate gray", text_color="white",corner_radius=30)
label1.pack(padx=15, pady=5)

text_var = ctk.StringVar(value="Create Menu")
label2 = ctk.CTkLabel(root,height=30,width=50, textvariable=text_var, font=("Arial", 18, "bold"), 
                      fg_color="gray34", text_color="white",corner_radius=30)
label2.pack(padx=15, pady=5)

selected_value = ctk.StringVar(value="")
options = ["", "create link button", "create header", "create divider", "create url", 
           "create text area", "create button", 'create selector', 'create checkbox', 
           'create output', 'create image', 'create video' , 'create text', 'create title', 'create sub header','create radial selector']
dropdown = ctk.CTkComboBox(root, variable=selected_value, values=options)
dropdown.pack(padx=10, pady=5)

text_var2 = ctk.StringVar(value="Function Menu")
label3 = ctk.CTkLabel(root,height=30,width=50, textvariable=text_var2, font=("Arial", 18, "bold"), 
                      fg_color="gray34", text_color="white",corner_radius=30)
label3.pack(padx=15, pady=5)

selected_value2 = ctk.StringVar(value="")
options2 = ["", "create link button", "create text area", "create button", "check input", 
            "create selector", "insert line", "inserted", "remove object", "control var", 
            "if", "else", "perform", "insert html code","create radial selector"]
dropdown2 = ctk.CTkComboBox(root, variable=selected_value2, values=options2)
dropdown2.pack(padx=10, pady=5)

def checkbox_callback():
    if var.get() == 1:
        insert()
        insert_warning()
    else:
        inserted()

var = ctk.IntVar()
checkbox = ctk.CTkCheckBox(root, text="Insert", variable=var, command=checkbox_callback)
checkbox.pack(pady=5)


text_var3 = ctk.StringVar(value="Edit and Logic Menu")
label4 = ctk.CTkLabel(root,height=30,width=50, textvariable=text_var3, font=("Arial", 18, "bold"), 
                      fg_color="gray34", text_color="white",corner_radius=30)
label4.pack(padx=15, pady=5)

selected_value3 = ctk.StringVar(value="")
options3 = ["", "if", "check input", "else", "remove line", "insert line", "inserted", 
            "perform", "control var"]
dropdown3 = ctk.CTkComboBox(root, variable=selected_value3, values=options3)
dropdown3.pack(padx=10, pady=5)

ifs = ctk.CTkButton(root, text="If / Check Object", command=lambda :[ifstate(),thenperform(),warning()])
ifs.pack(pady=2)

els = ctk.CTkButton(root, text="Else / If Not", command=lambda:[elsee(),thenperform(),warning()])
els.pack(pady=2)

parform = ctk.CTkButton(root, text="Then \n perform action", command=lambda:[thenperform(),warning()])
parform.pack(pady=2)

t = ctk.CTkTextbox(root, width=450, height=500)
savefile = ask_custom_string("Input", "save file","file_dialog")
try:
    with open("share.txt", 'w') as fp:
        fp.writelines(savefile)
except:
    with open("share.txt", 'w') as fp:
        fp.writelines("save.txt")
        savefile = "save.txt"
stylefile = ask_custom_string("Input", "style file","file_dialog")
program = ask_custom_string("Input", "program file","file_dialog")

def view_comments():
    t.delete("1.0", ctk.END)
    try:
        with open(savefile, 'r') as fp:
            lines = fp.readlines()
            comments = []
            comments_str = "Comments Are:\n"
            for i, line in enumerate(lines):
                if '#' in line:
                    comment = line.split('#', 1)[1].strip()
                    comments.append(f"{i}: {comment}")
            comments_str = "Comments Are:\n" + "\n".join(comments)
            t.insert("0.0", comments_str)
            t.pack(side=ctk.TOP, fill=ctk.X)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {savefile} not found")

def view():
    t.delete("1.0", ctk.END)
    try:
        with open(savefile, 'r') as fp:
            lines = fp.readlines()
            moved_lines_str = "Lines Are:\n"
            for i, line in enumerate(lines):
                moved_lines_str += f"{i}: {line}"
            t.insert("0.0", moved_lines_str)
            t.pack(side=ctk.TOP, fill=ctk.X)
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {savefile} not found")

frame = ctk.CTkFrame(root, width=300, height=160, corner_radius=20 , border_width=5)
frame.pack(pady=5, padx=5)

frame.grid_propagate(False)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

def removeview():
    t.pack_forget()

def checkbox_callback1():
    if var1.get() == 1:
        view()
    else:
        removeview()

def checkbox_callback2():
    if var2.get() == 1:
        view_comments()
    else:
        removeview()

var1 = ctk.IntVar()
var2 = ctk.IntVar()
checkbox1 = ctk.CTkCheckBox(frame, text="View </>", variable=var1, command=checkbox_callback1)
checkbox1.grid(row = 0, column = 0,sticky="nsew",padx=20,pady=5)

refresh = ctk.CTkButton(frame, text="Refresh ↻", command=checkbox_callback1,height = 10, width = 10)
refresh.grid(row = 0, column = 0,sticky="e",padx=20,pady=5)

refresh = ctk.CTkCheckBox(frame, text="View #", variable=var2, command=checkbox_callback2,height = 10, width = 10)
refresh.grid(row = 0, column = 0,padx=20,pady=5)

def compiler():
    Inp = savefile
    Inp2 = stylefile
    Input11 = program
    with open(Inp) as f1:
        lines = f1.readlines()

    if Inp2 == "default":
        f1.writelines("import streamlit as st\n")
        f1.writelines("from PIL import Image\n")
        f1.writelines(lines)
    else:
        with open(Inp2) as f2:
            lines2 = f2.readlines()
        with open(Input11, 'w') as f2:
            f2.writelines("import streamlit as st\n")
            f2.writelines("from PIL import Image\n")
            f2.writelines("st.markdown('''\n<style>\n")
            f2.writelines(lines2)
            f2.writelines("</style>\n''', unsafe_allow_html=True)\n")
            f2.writelines(lines)

def perform_action():
    Input = selected_value.get() + selected_value2.get() + selected_value3.get()
    if Input == "create header":
        CreateGroup()
    if Input == "create radial selector":
        radio()
        ifstate()
        thenperform()
        warning()
    if Input == "create video":
        CreateVideo()
    if Input == "create navbar":
        Createnav()
    if Input == "create link button":
        linkbutton()
    if Input == "create divider":
        divider()
    if Input == "create url":
        Createurl()
    if Input == "create sub header":
        CreateSubGroup()
    if Input == "create title":
        createtitle()
    if Input == "create text":
        Createtext()
    if Input == "create image":
        Createimage()
    if Input == "create output":
        hookoutput()
    if Input == "create checkbox":
        streamlitcheckbox()
        ifstate()
        thenperform()
        warning()
    if Input == "create selector":
        selector()
        ifstate()
        thenperform()
        warning()
    if Input == "check input":
        ifstate()
        thenperform()
        warning()
    if Input == "if":
        ifstate()
        thenperform()
        warning()
    if Input == "insert line":
        print("this func removes lines from this file to another for temporary storage use command inserted to place lines back in position\n")
        insert()
        insert_warning()
    if Input == "inserted":
        inserted()
    if Input == "perform":
        thenperform()
        warning()
    if Input == "create button":
        button_gui()
        ifstate()
        thenperform()
        warning()
    if Input == "else":
        elsee()
        thenperform()
        warning()
    if Input == "control var":
        changevar()
    if Input == "remove object":
        remove()
    if Input == "insert html code":
        code()
    if Input == "create text area":
        areatext()
    if Input == "view":
        lines = []
        with open(savefile, 'r') as fp:
            lines = fp.readlines()
            lines_to_move = lines[0:]
            print("Lines are \n")
            for i, line in enumerate(lines_to_move):
                messagebox.showinfo("Lines Are", f"{i}: {line}", end='')
    with open('code.txt', 'a') as new_file:
        new_file.writelines(Input + "\n")

    selected_value==ctk.StringVar(value="")
    dropdown.set("")
    selected_value2==ctk.StringVar(value="")
    dropdown2.set("")
    selected_value3==ctk.StringVar(value="")
    dropdown3.set("")
    success(Input)

button = ctk.CTkButton(frame, text="Perform Selected Action", command=perform_action)
button.grid(sticky="nsew", padx=50,pady=10)

button = ctk.CTkButton(frame, text="Remove Line", command=remove)
button.grid(sticky="nsew", padx=50)

button2 = ctk.CTkButton(frame, text="Compile", command=compiler)
button2.grid(sticky="nsew", padx=50,pady=10)

buttoncr = ctk.CTkButton(root, text="Credit", command=ask_credit)
buttoncr.pack()

root.mainloop()
