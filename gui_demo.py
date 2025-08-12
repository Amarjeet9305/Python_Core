import tkinter as tk

# Create main window

root = tk.Tk()
root.title("My Application")
root.geometry("450x200")

# First Name Label and Entry
tk.Label(root, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
fname = tk.Entry(root, width=30)
fname.grid(row=0, column=1, padx=5, pady=5)

# Last Name Label and Entry

tk.Label(root, text="Last Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
lname = tk.Entry(root, width=30)
lname.grid(row=1, column=1, padx=5, pady=5)

# Output Label

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=1, pady=5)

# Submit Button using lambda (no user-defined function)
tk.Button(
    root,
    text="Submit",
    command=lambda: result_label.config(text=f"Welcome, {fname.get()} {lname.get()}!")
).grid(row=2, column=1, pady=10)

# Start GUI loop
root.mainloop()
