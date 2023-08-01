import tkinter as tk
from tkinter import Label, Entry, Button, LabelFrame

def Calculate_Interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    result = round((p * r * t) / 100, 2)
    result_label.config(text=f"Simple Interest: {result}")

# Create the main application window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("400x250")
root.configure(bg="lightgray")

# Heading label
heading_label = Label(root, text="Simple Interest Calculator", font=("Helvetica", 16), bg="lightgray")
heading_label.place(x=80, y=10)

# Principal label and entry
principal_label = Label(root, text="Principal:", bg="lightgray")
principal_label.place(x=50, y=50)
principal_entry = Entry(root)
principal_entry.place(x=150, y=50)

# Rate of Interest label and entry
rate_label = Label(root, text="Rate of Interest:", bg="lightgray")
rate_label.place(x=50, y=80)
rate_entry = Entry(root)
rate_entry.place(x=150, y=80)

# Time label and entry
time_label = Label(root, text="Time:", bg="lightgray")
time_label.place(x=50, y=110)
time_entry = Entry(root)
time_entry.place(x=150, y=110)

# Calculation button
calculation_button = Button(root, text="Calculate", command=Calculate_Interest)
calculation_button.place(x=170, y=150)

# Result frame container
result_frame = LabelFrame(root, text="Result", bg="lightgray", width=300, height=50)
result_frame.place(x=50, y=200)

# Result label inside the result frame container
result_label = Label(result_frame, bg="lightgray")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
