import tkinter as tk

root = tk.Tk()

def on_button_click():
  label.config(text="Button clicked!")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

root.mainloop()
