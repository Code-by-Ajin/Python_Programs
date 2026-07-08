import tkinter as tk
from tkinter import ttk
import time

class ProfessionalStopwatch:
    """
    A professional, iOS-style Stopwatch application with Lap and Split tracking.
    """
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Pro Stopwatch")
        self.root.geometry("400x600")
        self.root.configure(bg="#1c1c1e")
        self.root.resizable(False, False)

        # --- State Variables ---
        self.running: bool = False
        self.start_time: float = 0.0
        self.elapsed_time: float = 0.0
        self.last_lap_time: float = 0.0
        self.lap_count: int = 0
        self._timer_id: str = None

        self._setup_ui()
        self._update_button_states()

    def _setup_ui(self):
        """Initializes the user interface components."""
        
        # 1. Main Time Display
        self.time_var = tk.StringVar(value="00:00:00.00")
        self.time_label = tk.Label(
            self.root, 
            textvariable=self.time_var, 
            font=("Helvetica", 48, "bold"), 
            bg="#1c1c1e", 
            fg="#ffffff"
        )
        self.time_label.pack(pady=(40, 40))

        # 2. Controls Frame (Buttons)
        controls_frame = tk.Frame(self.root, bg="#1c1c1e")
        controls_frame.pack(fill="x", padx=40, pady=(0, 30))
        
        # Configure grid to space buttons evenly
        controls_frame.columnconfigure(0, weight=1)
        controls_frame.columnconfigure(1, weight=1)

        # Button styling using a standard consistent size and flat relief
        btn_font = ("Helvetica", 14, "bold")
        
        self.btn_lap_reset = tk.Button(
            controls_frame, text="Lap", font=btn_font, width=8, height=2,
            bg="#333333", fg="#ffffff", activebackground="#444444", 
            activeforeground="#ffffff", relief="flat", borderwidth=0,
            command=self.handle_lap_reset
        )
        self.btn_lap_reset.grid(row=0, column=0, sticky="w")

        self.btn_start_stop = tk.Button(
            controls_frame, text="Start", font=btn_font, width=8, height=2,
            bg="#0b8457", fg="#ffffff", activebackground="#0c9c66", 
            activeforeground="#ffffff", relief="flat", borderwidth=0,
            command=self.handle_start_stop
        )
        self.btn_start_stop.grid(row=0, column=1, sticky="e")

        # 3. Laps Display (Treeview)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                        background="#2c2c2e", foreground="#ffffff", 
                        fieldbackground="#2c2c2e", borderwidth=0, font=("Helvetica", 12))
        style.configure("Treeview.Heading", 
                        background="#1c1c1e", foreground="#8e8e93", 
                        borderwidth=0, font=("Helvetica", 12, "bold"))
        style.map("Treeview", background=[("selected", "#3a3a3c")])

        # Frame for Treeview and Scrollbar
        list_frame = tk.Frame(self.root, bg="#1c1c1e")
        list_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        self.tree = ttk.Treeview(list_frame, columns=("Lap", "Split", "Total"), show="headings", selectmode="none")
        self.tree.heading("Lap", text="Lap")
        self.tree.heading("Split", text="Split Time")
        self.tree.heading("Total", text="Total Time")
        
        self.tree.column("Lap", width=60, anchor="center")
        self.tree.column("Split", width=140, anchor="center")
        self.tree.column("Total", width=140, anchor="center")
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _format_time(self, elapsed: float) -> str:
        """Converts float seconds into HH:MM:SS.ms string."""
        mins, secs = divmod(int(elapsed), 60)
        hours, mins = divmod(mins, 60)
        # Get 2 digits for hundredths of a second
        millisecs = int((elapsed - int(elapsed)) * 100)
        
        if hours > 0:
            return f"{hours:02d}:{mins:02d}:{secs:02d}.{millisecs:02d}"
        else:
            return f"{mins:02d}:{secs:02d}.{millisecs:02d}"

    def _update_button_states(self):
        """Updates button text and colors based on current state (mimicking iOS)."""
        if self.running:
            # When running: Stop & Lap
            self.btn_start_stop.config(text="Stop", bg="#d93a30", activebackground="#ff453a")
            self.btn_lap_reset.config(text="Lap", state="normal")
        else:
            # When paused/stopped: Start & Reset
            self.btn_start_stop.config(text="Start", bg="#0b8457", activebackground="#0c9c66")
            
            if self.elapsed_time > 0:
                self.btn_lap_reset.config(text="Reset", state="normal")
            else:
                self.btn_lap_reset.config(text="Lap", state="disabled") # Disable if 0.00

    def handle_start_stop(self):
        """Toggles the timer on and off."""
        if not self.running:
            # Start
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self._update_display()
        else:
            # Stop / Pause
            self.running = False
            if self._timer_id:
                self.root.after_cancel(self._timer_id)
                self._timer_id = None
        
        self._update_button_states()

    def handle_lap_reset(self):
        """Handles either lapping the time or resetting the clock."""
        if self.running:
            # Record a Lap
            self.lap_count += 1
            current_total = self.elapsed_time
            split_time = current_total - self.last_lap_time
            self.last_lap_time = current_total
            
            str_total = self._format_time(current_total)
            str_split = self._format_time(split_time)
            
            # Insert at the top of the treeview (index 0)
            self.tree.insert("", 0, values=(f"{self.lap_count:02d}", str_split, str_total))
        else:
            # Reset the clock
            self.elapsed_time = 0.0
            self.last_lap_time = 0.0
            self.lap_count = 0
            self.time_var.set("00:00.00")
            
            # Clear all laps from Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            self._update_button_states()

    def _update_display(self):
        """Core loop that updates the time label while the stopwatch is running."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.time_var.set(self._format_time(self.elapsed_time))
            # Schedule next update in 10 milliseconds for smooth hundredths-of-a-second tracking
            self._timer_id = self.root.after(10, self._update_display)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProfessionalStopwatch(root)
    print("Starting Pro Stopwatch GUI. If the window does not appear, check your display environment.")
    root.mainloop()
