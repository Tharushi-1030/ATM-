import tkinter as tk
from tkinter import simpledialog, messagebox

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM")

        self.balance = 1000
        self.pin = "1234"
        self.transaction_history = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to the ATM")
        self.label.pack()

        self.balance_button = tk.Button(self.master, text="Balance Enquiry", command=self.balance_enquiry)
        self.balance_button.pack()

        self.withdraw_button = tk.Button(self.master, text="Cash Withdrawal", command=self.cash_withdrawal)
        self.withdraw_button.pack()

        self.deposit_button = tk.Button(self.master, text="Cash Deposit", command=self.cash_deposit)
        self.deposit_button.pack()

        self.pin_change_button = tk.Button(self.master, text="PIN Change", command=self.pin_change)
        self.pin_change_button.pack()

        self.history_button = tk.Button(self.master, text="Transaction History", command=self.transaction_history_view)
        self.history_button.pack()

    def balance_enquiry(self):
        messagebox.showinfo("Balance Enquiry", f"Your current balance is: ${self.balance}")
        self.transaction_history.append("Balance Enquiry")

    def cash_withdrawal(self):
        amount = simpledialog.askinteger("Cash Withdrawal", "Enter amount to withdraw:")
        if amount is not None:
            if amount > self.balance:
                messagebox.showwarning("Error", "Insufficient balance")
            else:
                self.balance -= amount
                messagebox.showinfo("Success", f"${amount} withdrawn successfully")
                self.transaction_history.append(f"Cash Withdrawal: ${amount}")

    def cash_deposit(self):
        amount = simpledialog.askinteger("Cash Deposit", "Enter amount to deposit:")
        if amount is not None:
            self.balance += amount
            messagebox.showinfo("Success", f"${amount} deposited successfully")
            self.transaction_history.append(f"Cash Deposit: ${amount}")

    def pin_change(self):
        current_pin = simpledialog.askstring("PIN Change", "Enter current PIN:")
        if current_pin == self.pin:
            new_pin = simpledialog.askstring("PIN Change", "Enter new PIN:")
            confirm_pin = simpledialog.askstring("PIN Change", "Confirm new PIN:")
            if new_pin == confirm_pin:
                self.pin = new_pin
                messagebox.showinfo("Success", "PIN changed successfully")
                self.transaction_history.append("PIN Change")
            else:
                messagebox.showwarning("Error", "PINs do not match")
        else:
            messagebox.showwarning("Error", "Incorrect current PIN")

    def transaction_history_view(self):
        history = "\n".join(self.transaction_history)
        messagebox.showinfo("Transaction History", history if history else "No transactions yet")

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
