import customtkinter as ctk

root = ctk.CTk()
root.title("Bosco Web Developer")
root.geometry("400x800")
root.resizable(False, True)

class CustomInputDialog(ctk.CTkToplevel):
    def __init__(self, master, title, prompt):
        super().__init__(master)
        
        self.title(title)
        self.geometry("400x200")
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
    labe2 = ctk.CTkLabel(master=new_window, text="S i b a n g s h u K u n d u",font=("Felix Titling",46,"bold"))
    labe2.pack(pady=5)
    labe4 = ctk.CTkLabel(master=new_window, text="Of Class X-B",font=("Copperplate Gothic",28))
    labe4.pack(pady=0)
    labe3 = ctk.CTkLabel(master=new_window, text="For India International School\nAnnual Exhibition 2024",font=("Copperplate Gothic",20))
    labe3.pack(pady=20)
