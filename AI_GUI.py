import tkinter as tk
from tkinter import messagebox

operator = ["lbs", "pound", "pounds", "kg", "kilo", "kgs", "kilos"]
kilo = ["kg", "kilo", "kgs", "kilos"]
pound = ["lbs", "pound", "pounds"]

def kg_lbs(weight):
    pound = weight * 2.205
    return round(pound, 2)

def lbs_kg(weight):
    kilo = weight / 2.205
    return round(kilo, 2)

def convert_weight():
    start = start_var.get().lower()
    end = end_var.get().lower()
    weight = weight_entry.get()

    if (start in operator) and (end in operator):
        if (start in kilo and end in pound) or (start in pound and end in kilo):
            try:
                weight = float(weight)
                result = 0
                if (start in kilo) and (end in pound):
                    result = kg_lbs(weight)
                    end = "lbs"
                elif (start in pound) and (end in kilo):
                    result = lbs_kg(weight)
                    end = "kgs"
                result_label.config(text=f"Result = {result} {end}")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid weight.")
        else:
            messagebox.showerror("Error", "Please input different operators.")
    else:
        messagebox.showerror("Error", f"Invalid operators. Valid operators are {', '.join(operator)}.")

def reset_fields():
    start_var.set("")
    end_var.set("")
    weight_entry.delete(0, tk.END)
    result_label.config(text="")

def create_gui():
    global start_var, end_var, weight_entry, result_label

    root = tk.Tk()
    root.title("Weight Converter")

    welcome_label = tk.Label(root, text="Welcome to THE CONVERTER", font=("Arial", 16, "bold"))
    welcome_label.pack(pady=10)

    start_label = tk.Label(root, text="Convert From:")
    start_label.pack()

    start_var = tk.StringVar()
    start_entry = tk.Entry(root, textvariable=start_var)
    start_entry.pack()

    end_label = tk.Label(root, text="To:")
    end_label.pack()

    end_var = tk.StringVar()
    end_entry = tk.Entry(root, textvariable=end_var)
    end_entry.pack()

    weight_label = tk.Label(root, text="Weight:")
    weight_label.pack()

    weight_entry = tk.Entry(root)
    weight_entry.pack()

    convert_button = tk.Button(root, text="Convert", command=convert_weight)
    convert_button.pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack()

    reset_button = tk.Button(root, text="Reset", command=reset_fields)
    reset_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()