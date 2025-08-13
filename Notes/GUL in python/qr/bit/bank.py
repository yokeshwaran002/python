import tkinter as tk
from tkinter import messagebox

class BankApp:
    def __init__(self, root):
        self.balance = 0
        self.root = root
        self.root.title("Simple Bank Application")

        # Display balance
        self.balance_label = tk.Label(root, text=f"Balance: ₹{self.balance}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        # Entry for amount
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(pady=5)

        # Deposit button
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=5)

        # Withdraw button
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=5)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            self.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0 or amount > self.balance:
                raise ValueError
            self.balance -= amount
            self.update_balance()
        except ValueError:
            messagebox.showerror("Invalid Input", "Invalid withdrawal amount.")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ₹{self.balance}")
        self.amount_entry.delete(0, tk.END)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
