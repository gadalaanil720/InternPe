import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='white')
clock_label.pack(fill='both', expand=True)

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Initial call to update_time to start the clock
update_time()

# Run the application
root.mainloop()