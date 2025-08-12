# Create a UI calculator using tkinter

import tkinter as tk

# Create a window
root = tk.Tk()
root.title("Ui Calculator")
root.geometry("300x400")

# Enter Widget show the expression

display = tk.Entry(root,font=("Arial",18),borderwidth=5,relief="ridge",justify='right')
display.grid(row=0,column=0,columnspan=4,ipadx=8,ipady=15,padx=10,pady=10)

# Create a button on grid

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons using loop 
for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i][j], font=("Arial", 14), width=5, height=2)
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        
        
# Show the UI         
root.mainloop()