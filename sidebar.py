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
        def radio():
                File_object = open(savefile, "a")
                variable1 = ask_custom_string("Radial Selector", "Enter variable name")
                variable = ask_custom_string("Radial Selector", "Enter text to display")
                insertvalue = ask_custom_string("Radial Selector", "Enter value to insert")
                insertlist=insertvalue.split(',')
                insert = ", ".join(f"'{word}'" for word in insertlist)
                program1 = str(variable1 +" = st.sidebar.radio('"+variable+"',[")
                program2 = str(insert)
                program3 = str("])      #bosco created Radial Selector"+variable1+"\n")
                File_object.write(program1+program2+program3)
                print("✓")
        def CreateVideo():
                File_object = open(savefile, "a")
                url = ask_custom_string("Input", "Enter Video URL")
                program1 = str("st.sidebar.video("+url+")#      bosco created URL Video: "+url+"\n")
                File_object.write(program1)
                print("✓")
        def Createurl():
                File_object = open(savefile, "a")
                url = ask_custom_string("Input", "Enter URL")
                text = ask_custom_string("Input", "Enter text")
                program1 = str("st.sidebar.write('"+text+" [link]("+url+")')#      bosco created url: "+text+"\n")
                File_object.write(program1)
                print("✓")

        def Createnav():
                File_object = open(savefile, "a")
                content = ask_custom_string("Input", "navbar contents(use '' and ,)")
                program1 = str("page = (["+content+"])\nst.sidebar.write(page)\n")
                File_object.write(program1)
                print("✓")

        def linkbutton():
                File_object = open(savefile, "a")
                content1 = ask_custom_string("Input", "Enter URL Use # for in-website titles,headings\nElse use https://website name")
                content2 = ask_custom_string("Input", "Enter Button Text")
                program1 = str("st.sidebar.link_button('"+content2+"', '"+content1+"') #      bosco created link button: "+content2+"\n")
                File_object.write(program1)
                print("✓")

        def areatext():
                File_object = open(savefile, "a")
                Var = ask_custom_string("Input", "Enter Text Area Name")
                heading = ask_custom_string("Input", "Enter Text Area Heading")
                text = ask_custom_string("Input", "Enter Text")
                program1 = str(Var+'=st.sidebar.text_area("'+heading+'","'+text+'")#      bosco created text area: '+heading+'\n')
                File_object.write(program1)
                print("✓")

        def divider():
                File_object = open(savefile, "a")
                program1 = str("st.sidebar.divider()#      bosco created: divider\n")
                File_object.write(program1)
                print("✓")

        def code():
                File_object = open(savefile, "a")
                inpoot = ask_custom_string("Input", "Enter Code")
                program1 = str("st.sidebar.markdown('''\n")
                program2 = str(inpoot)
                program3 = str("\n''', unsafe_allow_html=True)")
                File_object.write("#bosco started writing code\n"+program1+program2+program3+"\n #bosco finished writing code\n")
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
                program1 = str(var+sets+value+"#        bosco changed/declared var: "+var+"\n")
                File_object.write(program1)
                print("✓")
               
        def CreateGroup():
                variable = ask_custom_string("Input", "Enter Header")
                File_object = open(savefile, "a")
                program1 = str("st.sidebar.header('"+variable+"')#      bosco created header: "+variable+"\n")
                File_object.write(program1)
                print("✓")

        def CreateSubGroup():
                variable = ask_custom_string("Input", "Enter Sub-Header")
                File_object = open(savefile, "a")
                program1 = str("st.sidebar.subheader('"+variable+"')#      bosco created sub header: "+variable+"\n")
                File_object.write(program1)
                print("✓")

        def createtitle():
                variable = ask_custom_string("Input", "Enter Title")
                File_object = open(savefile, "a")
                program1 = str("st.sidebar.title('"+variable+"')#      bosco created title: "+variable+"\n")
                File_object.write(program1)
                print("✓")

        def Createtext():
                variable = ask_custom_string("Input", "Enter text")
                if variable == "variable":
                        i = ask_custom_string("Input", "Enter variable name")
                        File_object = open(savefile, "a")
                        program1 = str("st.sidebar.write("+i+")#        bosco created text-var: "+i+"\n")
                        File_object.write(program1)
                        print("✓")
                else:
                        File_object = open(savefile, "a")
                        program1 = str("st.sidebar.write('"+variable+"')#        bosco created text: "+variable+"\n")
                        File_object.write(program1)
                        print("✓")

        def Createimage():
                File_object = open(savefile, "a")
                variable = ask_custom_string("Input", "Enter Path to image","file_dialog")
                size = ask_custom_string("Input", "Enter size(width)")
                program1 = str("st.sidebar.image(Image.open('"+variable+"'),width="+size+")#        bosco created image:"+variable+"\n")
                File_object.write(program1)
                print("✓")

        def hookoutput():
                variable = ask_custom_string("Input", "Enter text")
                if variable == "variable":
                        i = ask_custom_string("Input", "Enter variable name")
                        File_object = open(savefile, "a")
                        program1 = str("st.sidebar.success("+i+")#        bosco created output:"+i+"\n\n")
                        File_object.write(program1)
                        print("✓")
                else:
                        File_object = open(savefile, "a")
                        program1 = str("st.sidebar.success('"+variable+"')#        bosco created text-var:"+variable+"\n\n")
                        File_object.write(program1)
                        print("✓")

        def hookimage():
                File_object = open(savefile, "a")
                variable = input("image path")
                size = input("image size")
                program1 = str("        st.sidebar.image(Image.open('"+variable+"'),width="+size+")#        bosco created image:"+variable+"\n")
                File_object.write(program1)
                print("✓")

        def streamlitcheckbox():
                File_object = open(savefile, "a")
                variable = ask_custom_string("Input", "Enter Checkbox name")
                program1 = str(variable+" = st.sidebar.checkbox('"+variable+"')#        bosco created checkbox"+variable+"\n")
                File_object.write(program1)
                print("✓")

        def selector():
                File_object = open(savefile, "a")
                variable1 = ask_custom_string("Selector Box", "Enter variable name")
                variable = ask_custom_string("Selector Box", "Enter text to display")
                insertvalue = ask_custom_string("Selector Box", "Enter value to insert")
                insertlist=insertvalue.split(',')
                insert = ", ".join(f"'{word}'" for word in insertlist)
                program1 = str(variable1 +" = st.sidebar.selectbox('"+variable+"',[")
                program2 = str(insert)
                program3 = str("])      #bosco created selector"+variable1+"\n")
                File_object.write(program1+program2+program3)
                print("✓")

        def navbar12():
                File_object = open(savefile, "a")
                variable1 = ask_custom_string("Create Navbar", "Enter variable name")
                variable = ask_custom_string("Selector Box", "Enter text to display")
                insertvalue = ask_custom_string("Selector Box", "Enter value to insert")
                insertlist=insertvalue.split(',')
                insert = ", ".join(f"'{word}'" for word in insertlist)
                program1 = str("with st.sidebar.sidebar:")
                program2 = str()
                program3 = str("])      #bosco created selector"+variable1+"\n")
                File_object.write(program1+program2+program3)
                print("✓")

        def ifstate():
                File_object = open(savefile, "a")
                variables = ask_if_string("Check Input From Button , Checkbox , Selector etc.", savefile)
                if variables == "create":
                        changevar()
                        
                        condition = ask_custom_string("Check Var", "condition ==,<=,>=,!=,(leave empty for checkboxes or buttons), ")
                        choice = ask_custom_string("Check Var", "value (leave empty for checkboxes or buttons),(use '' for string)")
                        program1 = str("if "+variables+""+condition+""+choice+":      #if/checkvar: "+variables+"\n")
                        File_object.write(program1)
                      
                else:
                        
                        condition = ask_cond_string("Check Var Condition",savefile)
                        choice = ask_custom_string("Check Var", "value (leave empty for checkboxes or buttons),(use '' for string)")
                        program1 = str("if "+variables+""+condition+""+choice+":      #bosco created if/checkvar: "+variables+"\n")
                        File_object.write(program1)
                print("✓")

        def thenperform():
                File_object = open(savefile, "a")
                program1 = str("        ")
                File_object.write(program1)
                print("✓")

        def button_gui():
                File_object = open(savefile, "a")
                name = ask_custom_string("Input", "Enter Button Text")
                program1 = str(name+" = st.sidebar.button('"+name+"')      #bosco created button: "+name+"\n")
                File_object.write(program1)
                print("✓")

                

        def elsee():
                File_object = open(savefile, "a")
                File_object.write("else:"+"      #else: \n")
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

                Inputobject = ask_remove_string("Remove", "Line Numbers(select view if bosco dont know line no)")
                
                with open(savefile, 'w') as fp:
                    for number, line in enumerate(lines):
                        if number not in Inputobject:
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

        
