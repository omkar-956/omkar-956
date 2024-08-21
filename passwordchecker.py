import tkinter as tk
from tkinter import ttk, messagebox
import re


def assess_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[\W_]', password))

    if length < 8:
        length_strength = "Weak"
    elif length < 12:
        length_strength = "Moderate"
    else:
        length_strength = "Strong"

    criteria_met = sum([has_upper, has_lower, has_digit, has_special])

    if length_strength == "Weak" or criteria_met < 2:
        overall_strength = "Weak"
    elif length_strength == "Moderate" and criteria_met == 2:
        overall_strength = "Moderate"
    elif length_strength == "Moderate" and criteria_met > 2:
        overall_strength = "Strong"
    elif length_strength == "Strong" and criteria_met < 3:
        overall_strength = "Moderate"
    else:
        overall_strength = "Strong"

    return {
        "length": length,
        "length_strength": length_strength,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "overall_strength": overall_strength
    }


def assess_and_display_password():
    password = entry_password.get()
    assessment = assess_password_strength(password)

    label_length_result.config(text=f"Length: {assessment['length']} ({assessment['length_strength']})")
    label_upper_result.config(text=f"Uppercase: {'Yes' if assessment['has_upper'] else 'No'}")
    label_lower_result.config(text=f"Lowercase: {'Yes' if assessment['has_lower'] else 'No'}")
    label_digit_result.config(text=f"Numbers: {'Yes' if assessment['has_digit'] else 'No'}")
    label_special_result.config(text=f"Special Characters: {'Yes' if assessment['has_special'] else 'No'}")
    label_overall_result.config(text=f"Overall Strength: {assessment['overall_strength']}")


def clear_results():
    label_length_result.config(text="")
    label_upper_result.config(text="")
    label_lower_result.config(text="")
    label_digit_result.config(text="")
    label_special_result.config(text="")
    label_overall_result.config(text="")


# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Frame for password input and results
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")

# Password entry and assessment button
label_password = ttk.Label(frame, text="Enter Password:")
label_password.grid(row=0, column=0, sticky="w")

entry_password = ttk.Entry(frame, width=30, show="*")
entry_password.grid(row=0, column=1, padx=10)

button_assess = ttk.Button(frame, text="Assess", command=assess_and_display_password)
button_assess.grid(row=0, column=2, padx=10)

# Labels for displaying assessment results
label_length_result = ttk.Label(frame, text="")
label_length_result.grid(row=1, column=0, columnspan=3, sticky="w", pady=5)

label_upper_result = ttk.Label(frame, text="")
label_upper_result.grid(row=2, column=0, columnspan=3, sticky="w", pady=5)

label_lower_result = ttk.Label(frame, text="")
label_lower_result.grid(row=3, column=0, columnspan=3, sticky="w", pady=5)

label_digit_result = ttk.Label(frame, text="")
label_digit_result.grid(row=4, column=0, columnspan=3, sticky="w", pady=5)

label_special_result = ttk.Label(frame, text="")
label_special_result.grid(row=5, column=0, columnspan=3, sticky="w", pady=5)

label_overall_result = ttk.Label(frame, text="")
label_overall_result.grid(row=6, column=0, columnspan=3, sticky="w", pady=5)

# Clear button
button_clear = ttk.Button(frame, text="Clear", command=clear_results)
button_clear.grid(row=7, column=0, columnspan=3, pady=10)

# Run the application
root.mainloop()
