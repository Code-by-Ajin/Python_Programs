import tkinter as tk
from tkinter import ttk

def convert_number(num_str):
    """Converts an integer to binary."""
    try:
        number = int(num_str)
        # Preserve the sign for negative values and use format() for correct binary output.
        if number < 0:
            return '-' + format(-number, 'b')
        return format(number, 'b')
    except ValueError:
        return "❌ Error: Please enter a valid integer."

def convert_character(char_str):
    """Converts a single character to its 8-bit ASCII binary representation."""
    if len(char_str) != 1:
        return "❌ Error: Please enter exactly ONE character."
    
    # ord() gets the ASCII/Unicode integer value, format() converts to 8-bit binary
    return format(ord(char_str), '08b')

def convert_sentence(sentence_str):
    """Converts a full sentence to binary, separated by spaces."""
    if not sentence_str:
        return "❌ Error: Input cannot be empty."
    
    # Convert each character (including spaces) into binary and join them with a space
    binary_list = [format(ord(char), '08b') for char in sentence_str]
    return ' '.join(binary_list)

class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Converter Pro")
        self.root.geometry("550x550")
        
        # Sleek dark modern background
        self.bg_color = "#1e1e2e" 
        self.root.configure(bg=self.bg_color)
        
        # Title
        title_lbl = tk.Label(
            root, text="Binary Converter", font=("Helvetica", 24, "bold"), 
            bg=self.bg_color, fg="#cba6f7"
        )
        title_lbl.pack(pady=30)

        # Mode Selection Frame
        opt_frame = tk.Frame(root, bg=self.bg_color)
        opt_frame.pack(pady=10)

        tk.Label(
            opt_frame, text="Select Mode:", font=("Helvetica", 12), 
            bg=self.bg_color, fg="#a6adc8"
        ).grid(row=0, column=0, padx=10)
        
        self.mode_var = tk.StringVar(value="Sentence")
        modes = ["Number", "Character", "Sentence"]
        
        # Styling the modern combobox
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="#313244", background="#313244", foreground="#ffffff", borderwidth=0)
        
        self.dropdown = ttk.Combobox(
            opt_frame, textvariable=self.mode_var, values=modes, 
            state="readonly", font=("Helvetica", 12), width=15
        )
        self.dropdown.grid(row=0, column=1, padx=10)

        # Input Frame
        in_frame = tk.Frame(root, bg=self.bg_color)
        in_frame.pack(pady=15)
        
        tk.Label(
            in_frame, text="Enter Input:", font=("Helvetica", 12), 
            bg=self.bg_color, fg="#a6adc8"
        ).pack(anchor="w")
        
        self.input_entry = tk.Entry(
            in_frame, font=("Helvetica", 14), width=40, bg="#313244", 
            fg="#cdd6f4", insertbackground="white", relief="flat"
        )
        self.input_entry.pack(pady=5, ipady=8)

        # Convert Button
        convert_btn = tk.Button(
            root, text="Convert to Binary", font=("Helvetica", 14, "bold"), 
            bg="#89b4fa", fg="#1e1e2e", activebackground="#b4befe", 
            activeforeground="#1e1e2e", relief="flat", command=self.convert, 
            width=20, cursor="hand2"
        )
        convert_btn.pack(pady=20)

        # Output Frame
        out_frame = tk.Frame(root, bg=self.bg_color)
        out_frame.pack(pady=10)
        
        tk.Label(
            out_frame, text="Binary Output:", font=("Helvetica", 12), 
            bg=self.bg_color, fg="#a6adc8"
        ).pack(anchor="w")
        
        self.output_text = tk.Text(
            out_frame, font=("Courier", 13), width=45, height=6, bg="#313244", 
            fg="#a6e3a1", relief="flat", wrap="word", insertbackground="white"
        )
        self.output_text.pack(pady=5)
        self.output_text.config(state="disabled")

    def convert(self):
        """Fetches the input, calls the correct function, and displays output."""
        mode = self.mode_var.get()
        val = self.input_entry.get()
        
        # Route to appropriate conversion logic
        if mode == "Number":
            res = convert_number(val)
        elif mode == "Character":
            res = convert_character(val)
        else:
            res = convert_sentence(val)
            
        # Update the UI Output Box
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, res)
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryConverterApp(root)
    root.mainloop()
