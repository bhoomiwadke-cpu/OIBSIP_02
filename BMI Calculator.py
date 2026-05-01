# BMI Calculator - Advanced GUI Version
# Save as bmi_gui.py and run: python bmi_gui.py

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Data storage for multiple users
bmi_history = []

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")

        # Save history
        bmi_history.append(bmi)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def show_history():
    if not bmi_history:
        messagebox.showinfo("History", "No BMI records yet!")
        return

    plt.plot(bmi_history, marker='o')
    plt.title("BMI Trend")
    plt.xlabel("Entry")
    plt.ylabel("BMI Value")
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="BMI will appear here")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

history_button = tk.Button(root, text="Show History", command=show_history)
history_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
