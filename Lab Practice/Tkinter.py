#Create a tkinter app with menu bar
#file(new,open,save,exit)apps(calc,notepad,google crome)about-msg like name address ,contact msg box which just includes our contact


'''import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title("MyApp")
window.geometry("400x500")
window.config(bg='lightpink')

tkinter.Label(text="Menu Bar",fg='brown',font='Elephant 15').grid()


tkinter.mainloop()'''


import tkinter as tk
from tkinter import messagebox, filedialog
import os
import webbrowser
import subprocess

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))

def exit_app():
    root.destroy()

def open_calculator():
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen('calc.exe')
        else:
            subprocess.Popen(['gnome-calculator'])
    except:
        messagebox.showerror("Error", "Calculator not found!")

def open_notepad():
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen('notepad.exe')
        else:
            subprocess.Popen(['gedit'])
    except:
        messagebox.showerror("Error", "Notepad not found!")

def open_chrome():
    try:
        webbrowser.open('http://www.google.com')
    except:
        messagebox.showerror("Error", "Chrome not found!")

def show_about():
    messagebox.showinfo("About", "Name: Mahek Kothari\nAddress: Gandhinagar, Gujarat\nContact: 9876543210")

def show_contact():
    messagebox.showinfo("Contact Us", "You can contact us at:\nmahek@example.com\nPhone: 9876543210")

# Main window
root = tk.Tk()
root.title("Tkinter App with Menu")
root.geometry("600x400")

# Text area
text_area = tk.Text(root)
text_area.pack(expand=True, fill=tk.BOTH)

# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Apps menu
apps_menu = tk.Menu(menu_bar, tearoff=0)
apps_menu.add_command(label="Calculator", command=open_calculator)
apps_menu.add_command(label="Notepad", command=open_notepad)
apps_menu.add_command(label="Google Chrome", command=open_chrome)
menu_bar.add_cascade(label="Apps", menu=apps_menu)

# About menu
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About Us", command=show_about)
menu_bar.add_cascade(label="About", menu=about_menu)

# Contact menu
contact_menu = tk.Menu(menu_bar, tearoff=0)
contact_menu.add_command(label="Contact", command=show_contact)
menu_bar.add_cascade(label="Contact", menu=contact_menu)

# Set menu bar
root.config(menu=menu_bar)

# Start app
root.mainloop()
