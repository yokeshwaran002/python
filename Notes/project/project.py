import tkinter as tk
from tkinter import messagebox, ttk

# Create application form window
def open_application_form():
    app_window = tk.Toplevel()
    app_window.title("Application Form")
    app_window.geometry("400x400")

    labels = ["Name", "Email", "Phone", "Age", "Address"]
    entries = {}

    # Normal entry fields
    for idx, lbl in enumerate(labels):
        tk.Label(app_window, text=lbl).grid(row=idx, column=0, padx=10, pady=5)
        entry = tk.Entry(app_window)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[lbl] = entry

      # Combobox fields for Address
    address_labels = ["Country", "State", "District"]
    address_values = {
        "Country": ["India", "USA", "UK", "Canada", "Australia"],
        "State": ["Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh", "Telangana"],
        "District": ["Chennai", "Cochin", "Bangalore", "Hyderabad", "Vijayawada"]
    }

    comboboxes = {}
    start_row = len(labels)
    for idx, lbl in enumerate(address_labels):
        tk.Label(app_window, text=lbl).grid(row=start_row + idx, column=0, padx=10, pady=5, sticky="e")
        cb = ttk.Combobox(app_window, values=address_values[lbl], state="readonly")
        cb.current(0)  # set default value
        cb.grid(row=start_row + idx, column=1, padx=10, pady=5)
        comboboxes[lbl] = cb

    # Gender radio buttons
    gender_var = tk.StringVar(value="Male")  # Default selection
    tk.Label(app_window, text="Gender").grid(row=len(labels)+4, column=0, padx=10, pady=5)
    gender_frame = tk.Frame(app_window)
    gender_frame.grid(row=len(labels)+4, column=1, padx=10, pady=5)
    tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
    tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")
    tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").pack(side="left")

# Save to file with file handling
    def submit_form():
        details = [entries[key].get() for key in labels + ["Address"]]

        with open("applicants.txt", "a") as f:
            f.write(", ".join(details) + f", Gender: {gender_var.get()}\n")

        messagebox.showinfo("Form Submitted", "Details saved to file!")

        # Clear the entries after submission (optional)
        for key in entries:
            entries[key].delete(0, tk.END)
        gender_var.set("Male")  # reset gender

    submit_btn = tk.Button(app_window, text="Submit", command=submit_form)
    submit_btn.grid(row=len(labels)+5, column=1, pady=15)


# Basic login validation
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "Admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        login_window.destroy()
        open_application_form()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Login Form
login_window = tk.Tk()
login_window.title("Login Form")
login_window.geometry("300x180")

tk.Label(login_window, text="Username:").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_btn = tk.Button(login_window, text="Login", command=validate_login)
login_btn.pack(pady=20)

login_window.mainloop()