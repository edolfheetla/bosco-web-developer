import customtkinter as ctk
import ast
root = ctk.CTk()
root.title("Bosco Web Developer")
root.geometry("400x800")
root.resizable(False, True)

def get_objects(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    
    tree = ast.parse(file_content)
    variable_names = set()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            variable_names.add(node.id)
    
    return list(variable_names)

class CustomInputDialog(ctk.CTkToplevel):
    def __init__(self, master, title, prompt):
        super().__init__(master)
        
        self.title(title)
        self.geometry("420x200")
        self.resizable(False, False)
        
        self.prompt_label = ctk.CTkLabel(self, text=prompt, font=("Arial", 14))
        self.prompt_label.pack(pady=20)
        
        self.entry = ctk.CTkEntry(self, width=300)
        self.entry.pack(pady=10)
        
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)
        
        self.ok_button = ctk.CTkButton(self.button_frame, text="OK", command=self.on_ok)
        self.ok_button.pack(side=ctk.LEFT, padx=10)
        
        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancel", command=self.on_cancel)
        self.cancel_button.pack(side=ctk.LEFT, padx=10)
        
        self.result = None
        
    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()
        
    def on_cancel(self):
        self.destroy()

def ask_custom_string(title, prompt):
    dialog = CustomInputDialog(root, title, prompt)
    root.wait_window(dialog)
    return dialog.result

def ask_credit():
    new_window = ctk.CTkToplevel()
    new_window.title("Credits")
    new_window.geometry("700x400")
    label = ctk.CTkLabel(master=new_window, text="The App Was Made By",font=("Copperplate Gothic",20))
    label.pack(pady=20)
    labe2 = ctk.CTkLabel(master=new_window, text="S i b a n g s h u - K u n d u",font=("Felix Titling",42,"bold"))
    labe2.pack(pady=5)
    labe4 = ctk.CTkLabel(master=new_window, text="Of Class X-B",font=("Copperplate Gothic",28))
    labe4.pack(pady=0)
    labe3 = ctk.CTkLabel(master=new_window, text="For India International School\nAnnual Exhibition 2024",font=("Copperplate Gothic",20))
    labe3.pack(pady=20)

def warning():
    new_window = ctk.CTkToplevel()
    new_window.title("Information")
    new_window.geometry("400x300")
    label = ctk.CTkLabel(master=new_window, text="✓",font=("Arial",40))
    label.pack(pady=20)
    labe2 = ctk.CTkLabel(master=new_window, text="After this you have to create an object\n that will be displayed if the above conditions meet\n from main menu",font=("Arial",15))
    labe2.pack(pady=20)

def insert_warning():
    new_window = ctk.CTkToplevel()
    new_window.title("Warning")
    new_window.geometry("400x300")
    label = ctk.CTkLabel(master=new_window, text="✓",font=("Arial",40))
    label.pack(pady=20)
    labe2 = ctk.CTkLabel(master=new_window, text="this func removes lines from this file to another\n for temporary storage uncheck or select inserted to\n place lines back in position\n",font=("Arial",15))
    labe2.pack(pady=20)

class CustomIfDialog(ctk.CTkToplevel):
    def __init__(self, master, title,savefile):
        super().__init__(master)
        
        self.title(title)
        self.geometry("420x200")
        self.resizable(False, False)
        
        self.prompt_label = ctk.CTkLabel(self, text="Check Input from Checkbox,Button,Selectbox,Text Area", font=("Arial", 14))
        self.prompt_label.pack(pady=20)

        variable_names = get_objects(savefile)
        
        self.entry = ctk.CTkOptionMenu(self, values=variable_names)
        self.entry.pack(pady=10)
        
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)
        
        self.ok_button = ctk.CTkButton(self.button_frame, text="OK", command=self.on_ok)
        self.ok_button.pack(side=ctk.LEFT, padx=10)
        
        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancel", command=self.on_cancel)
        self.cancel_button.pack(side=ctk.LEFT, padx=10)
        
        self.result = None
        
    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()
        
    def on_cancel(self):
        self.destroy()

def ask_if_string(title,savefile):
    dialog = CustomIfDialog(root, title,savefile)
    root.wait_window(dialog)
    return dialog.result

class CustomCondDialog(ctk.CTkToplevel):
    def __init__(self, master, title,savefile):
        super().__init__(master)
        
        self.title(title)
        self.geometry("420x300")
        self.resizable(False, False)
        
        self.prompt_label = ctk.CTkLabel(self, text="condition ==,<=,>=,!=,(leave empty for checkboxes or buttons)\n==(is equal to)\n <= or >= (less than or greater than)\n !=(not equal to)", font=("Arial", 14))
        self.prompt_label.pack(pady=20)

        condition_=['','==','<=','>=','!=']
        
        self.entry = ctk.CTkOptionMenu(self, values=condition_)
        self.entry.pack(pady=10)

        self.prompt_label = ctk.CTkLabel(self, text="after this you have to create an object\n that will be displayed if the above conditions meet\n from main menu", font=("Arial", 14))
        self.prompt_label.pack(pady=20)
        
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)
        
        self.ok_button = ctk.CTkButton(self.button_frame, text="OK", command=self.on_ok)
        self.ok_button.pack(side=ctk.LEFT, padx=10)
        
        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancel", command=self.on_cancel)
        self.cancel_button.pack(side=ctk.LEFT, padx=10)
        
        self.result = None
        
    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()
        
    def on_cancel(self):
        self.destroy()

def ask_cond_string(title,savefile):
    dialog = CustomCondDialog(root, title,savefile)
    root.wait_window(dialog)
    return dialog.result

class CustomRemoveDialog(ctk.CTkToplevel):
    def __init__(self, master, title, prompt):
        super().__init__(master)

        self.entry = ctk.StringVar()
        
        self.title(title)
        self.geometry("420x250")
        self.resizable(False, False)
        
        self.prompt_label = ctk.CTkLabel(self, text="Remove From :", font=("Arial", 14))
        self.prompt_label.pack(pady=5)
        
        self.From = ctk.CTkEntry(self, width=300)
        self.From.pack(pady=5)

        self.prompt_label = ctk.CTkLabel(self, text="Remove To :", font=("Arial", 14))
        self.prompt_label.pack(pady=5)

        self.To = ctk.CTkEntry(self, width=300)
        self.To.pack(pady=5)

        
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)
        
        self.ok_button = ctk.CTkButton(self.button_frame, text="OK", command=self.on_ok)
        self.ok_button.pack(side=ctk.LEFT, padx=10)
        
        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancel", command=self.on_cancel)
        self.cancel_button.pack(side=ctk.LEFT, padx=10)
        
        self.result = None
        
    def on_ok(self):
        self.handle = int(self.From.get())
        self.handle2 = int(self.To.get())
        self.value = range(self.handle,self.handle2+1)
        self.entry = set(self.value)
        self.result = self.entry
        self.destroy()
        
    def on_cancel(self):
        self.destroy()

def ask_remove_string(title, prompt):
    dialog = CustomRemoveDialog(root, title, prompt)
    root.wait_window(dialog)
    return dialog.result
