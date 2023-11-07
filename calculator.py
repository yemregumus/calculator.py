import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for input and output
entry = tk.Entry(root, width=20, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)

# Define button layout
button_labels = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    "C",
    "=",
    "+",
]

# Create and arrange buttons
row = 1
col = 0
buttons = []
for label in button_labels:
    button = tk.Button(root, text=label, width=5, height=2, font=("Helvetica", 12))
    button.grid(row=row, column=col)
    buttons.append(button)
    col += 1
    if col > 3:
        col = 0
        row += 1


# Function to handle button clicks
def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


# Bind button click events to the function
for button in buttons:
    button.bind("<Button-1>", button_click)

# Start the main loop
root.mainloop()
