import subprocess


package_name = "tkinter"
subprocess.run(["pip", "install", package_name])





import tkinter as tk
from tkinter import messagebox

def execute_python_file():
    
    subprocess.Popen(["python", r"C:\Users\VICTUS\Control.py"])

def execute_scrcpy():
    
    try:
        subprocess.Popen([r"C:\scrpy\scrcpy-win64-v2.4\scrcpy.exe"])
    except FileNotFoundError:
        messagebox.showerror("Error", "scrcpy executable not found")


root = tk.Tk()
root.title("Executable Buttons")


def on_enter(event):
    event.widget.config(bg='blue')

def on_leave(event):
    event.widget.config(bg='SystemButtonFace')


button1 = tk.Button(root, text="Coversion to Grayscale", command=execute_python_file)
button1.config(width=20, height=2)
button1.grid(row=0, column=0, padx=10, pady=10)
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

button2 = tk.Button(root, text="Projection Mobile to Laptop", command=execute_scrcpy)
button2.config(width=20, height=2)
button2.grid(row=0, column=1, padx=10, pady=10)
button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)


root.mainloop()


