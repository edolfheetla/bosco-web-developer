import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from customstring import*
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

with open("share.txt", 'r') as original_file:
                s = original_file.readlines()
savefile = listToString(s)
try:
        
        #Input = input("Enter Function ")

        def Createurl():
                File_object = open(savefile, "a")
                url = ask_custom_string("Input", "Enter URL")
                program1 = str("st.write('check out this [link]("+url+")')#url"+url+"\n")
                File_object.write(program1)
                print("✓")

        def Createnav():
                File_object = open(savefile, "a")
                content = ask_custom_string("Input", "navbar contents(use '' and ,)")
                program1 = str("page = st_navbar(["+content+"])\nst.write(page)\n")
                File_object.write(program1)
                print("✓")

        def linkbutton():
                File_object = open(savefile, "a")
                content1 = ask_custom_string("Input", "Enter URL")
                content2 = ask_custom_string("Input", "Enter Button Text")
                program1 = str("st.link_button('"+content2+"', '"+content1+"') #link button "+content2+"\n")
                File_object.write(program1)
                print("✓")

        def areatext():
                File_object = open(savefile, "a")
                text = ask_custom_string("Input", "Enter Text")
                explanation = ask_custom_string("Input", "Enter variable")
                program1 = str(text+'=st.text_area("'+explanation+'","'+text+'")#text area'+text+'\n')
                File_object.write(program1)
                print("✓")

        def divider():
                File_object = open(savefile, "a")
                program1 = str("st.divider()#divider\n")
                File_object.write(program1)
                print("✓")

        def code():
                File_object = open(savefile, "a")
                inpoot = ask_custom_string("Input", "Enter Code")
                program1 = str("st.markdown('''\n")
                program2 = str(inpoot)
                program3 = str("\n''', unsafe_allow_html=True)")
                File_object.write("#code\n"+program1+program2+program3+"\n #code\n")
                print("✓")

        def intvar():
                File_object = open(savefile, "a")
                var = input("Enter var name ")
                program1 = str(var+"=0\n")
                File_object.write(program1)
                print("✓")

        def changevar():
                File_object = open(savefile, "a")
                var = ask_custom_string("change/declare var", "Enter variable name")
                sets = ask_custom_string("change/declare var", "==(is equal to) +=(increase by value) -=(decrease by value) =(declare variable) ''(create string)")
                value = ask_custom_string("change/declare var", "Enter value")
                program1 = str(var+sets+value+"#change/declare var"+var+"\n")
                File_object.write(program1)
                print("✓")
               
        def CreateGroup():
                variable = ask_custom_string("Input", "Enter Header")
                File_object = open(savefile, "a")
                program1 = str("st.header('"+variable+"')#Header\n")
                File_object.write(program1)
                print("✓")

        def CreateSubGroup():
                variable = ask_custom_string("Input", "Enter Sub-Header")
                File_object = open(savefile, "a")
                program1 = str("st.subheader('"+variable+"')#sub header\n")
                File_object.write(program1)
                print("✓")

        def createtitle():
                variable = ask_custom_string("Input", "Enter Title")
                File_object = open(savefile, "a")
                program1 = str("st.title('"+variable+"')#title"+variable+"\n")
                File_object.write(program1)
                print("✓")

        def Createtext():
                variable = ask_custom_string("Input", "Enter text(type variable to use variable)")
                if variable == "variable":
                        i = ask_custom_string("Input", "Enter variable name")
                        File_object = open(savefile, "a")
                        program1 = str("st.write("+i+")\n")
                        File_object.write(program1)
                        print("✓")
                else:
                        File_object = open(savefile, "a")
                        program1 = str("st.write('"+variable+"')\n")
                        File_object.write(program1)
                        print("✓")

        def Createimage():
                File_object = open(savefile, "a")
                variable = ask_custom_string("Input", "Enter Path to image")
                size = ask_custom_string("Input", "Enter size(width)")
                program1 = str("st.image(Image.open('"+variable+"'),width="+size+")\n")
                File_object.write(program1)
                print("✓")

        def hookoutput():
                variable = ask_custom_string("Input", "Enter text(type variable to use variable)")
                if variable == "variable":
                        i = ask_custom_string("Input", "Enter variable name")
                        File_object = open(savefile, "a")
                        program1 = str("st.success("+i+")#output\n")
                        File_object.write(program1)
                        print("✓")
                else:
                        File_object = open(savefile, "a")
                        program1 = str("st.success('"+variable+"')#output\n")
                        File_object.write(program1)
                        print("✓")

        def hookimage():
                File_object = open(savefile, "a")
                variable = input("image path")
                size = input("image size")
                program1 = str("        st.image(Image.open('"+variable+"'),width="+size+")#image\n")
                File_object.write(program1)
                print("✓")

        def checkbox():
                File_object = open(savefile, "a")
                variable = ask_custom_string("Input", "Enter Checkbox name")
                program1 = str(variable+" = st.checkbox('"+variable+"')#checkbox"+variable+"\n")
                File_object.write(program1)
                print("✓")

        def selector():
                File_object = open(savefile, "a")
                variable1 = ask_custom_string("Input", "Enter variable name")
                variable = ask_custom_string("Input", "Enter text to display")
                insertvalue = ask_custom_string("Input", "Enter value to insert (use '' and ,)")
                program1 = str(variable1 +" = st.selectbox('"+variable+"',["+insertvalue+"])#selector"+variable1+"\n")
                File_object.write(program1)
                print("✓")

        def ifstate():
                File_object = open(savefile, "a")
                variables = ask_custom_string("Check Var", "object to be checked(type create to make new variables)")
                if variables == "create":
                        changevar()
                        variable = ask_custom_string("Check Var", "if object variable")
                        choice = ask_custom_string("Check Var", "value (leave empty for checkboxes or buttons)(use '')")
                        condition = ask_custom_string("Check Var", "condition ==,<=,>=,!=,(leave empty for checkboxes or buttons), ")
                        program1 = str("if "+variables+""+condition+""+choice+":#if/checkvar\n")
                        File_object.write(program1)
                        
                else:
                        choice = ask_custom_string("Check Var", "value (leave empty for checkboxes or buttons)(use '')")
                        condition = ask_custom_string("Check Var", "condition ==,<=,>=,!=,(leave empty for checkboxes or buttons), ")
                        program1 = str("if "+variables+""+condition+""+choice+":#if/checkvar\n")
                        File_object.write(program1)

                print("✓")

        def perform():
                File_object = open(savefile, "a")
                program1 = str("        ")
                File_object.write(program1)
                print("✓")

        def button_gui():
                File_object = open(savefile, "a")
                name = ask_custom_string("Input", "Enter Button Text")
                program1 = str(name+" = st.button('"+name+"')#button"+name+"\n")
                File_object.write(program1)
                print("✓")

                

        def elsee():
                File_object = open(savefile, "a")
                program1 = ask_custom_string("Input", "If the above conditions aren't met")
                perform()
                if program1 =="":
                        program1=="pass"
                File_object.write(program1+" #else\n")
                print("✓")

        def split_file():

            actual_line = ask_custom_string("Integer Input", "Line Number(select view if you dont know line no)")
            start_line = actual_line+1
            with open(savefile, 'r') as original_file:
                lines = original_file.readlines()
                
            with open('temp.txt', 'w') as new_file:
                new_file.writelines(lines[start_line-1:])

            with open(savefile, 'w') as original_file:
                original_file.writelines(lines[:start_line-1])

            print("✓")

        def insert():
                lines = []
                line_count = 0
                with open(savefile, 'r') as fp:
                    lines = fp.readlines()

                actual_line = int(ask_custom_string("Integer Input", "Line Number(select view if you dont know line no)"))
                start_line = actual_line+1
                with open(savefile, 'r') as original_file:
                        lines = original_file.readlines()
                
                with open('temp.txt', 'w') as new_file:
                        new_file.writelines(lines[start_line-1:])

                with open(savefile, 'w') as original_file:
                        original_file.writelines(lines[:start_line-1])

                print("✓")

        def remove():
                lines = []
                with open(savefile, 'r') as fp:
                    lines = fp.readlines()

                Inputobject = int(input("object number to remove "))
                Inputobj = 0
                Inputobj == Inputobject

                with open(savefile, 'w') as fp:
                    for number, line in enumerate(lines):
                        if number not in [Inputobject]:
                            fp.write(line)
                print("✓")

        def inserted():
                lines = []
                start_line = 1
                with open('temp.txt', 'r') as original_file:
                        lines = original_file.readlines()
                        
                with open(savefile, 'a') as new_file:
                        new_file.writelines(lines[start_line-1:])

                with open('temp.txt', 'w') as original_file:
                        original_file.writelines(lines[:start_line-1])

                print("✓")                
                

        '''
        if Input == "create header":
                variable = input("header name ")
                CreateGroup()

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
                checkbox()

        if Input == "create selector":
                selector()

        if Input == "check input":
                ifstate()

        if Input == "insert line":
                print("this func removes lines from this file to another for temporary storage use command inserted to place lines back in position\n")
                insert()

        if Input == "inserted":
                inserted()

        if Input == "perform":
                perform()

        if Input == "create button":
                button()

        if Input == "else":
                elsee()

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
                        print(f"{i}: {line}", end='')  
                
        with open('code.txt', 'a') as new_file:
                new_file.writelines(Input+"\n")
                '''
except:
        print("Error")

        
