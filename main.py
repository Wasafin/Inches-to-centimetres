import tkinter as tk
from tkinter import messagebox

# Conversion factor from inches to centimeters
INCH_TO_CM = 2.54

# Function to perform the conversion and display the result
def convert_to_cm():
    try:
        # Get the value from the entry field
        inches = float(entry.get())
        # Convert inches to centimeters
        cm = inches * INCH_TO_CM
        # Display the result in a message box
        messagebox.showinfo("Result", f"{inches} inches is equal to {cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

# Create the main application window
root = tk.Tk()
root.title("Inch to Centimeter Converter")

# Create a label for the input
label = tk.Label(root, text="Enter length in inches:")
label.pack(pady=10)

# Create an entry widget to get input from the user
entry = tk.Entry(root)
entry.pack(pady=5)

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

# Run the application
root.mainloop()
