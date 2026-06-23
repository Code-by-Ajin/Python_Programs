import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            entry_var.set(result)
            expression = str(result)
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""
entry_var = tk.StringVar()

entry = tk.Entry(root, textvar=entry_var, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 0, 0
for btn in buttons:
    b = tk.Button(button_frame, text=btn, font="Arial 15", width=5, height=2)
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col += 1
    if col == 4:
        row += 1
        col = 0

root.mainloop() 
