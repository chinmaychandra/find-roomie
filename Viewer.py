import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk

def show_user_details(user_id):
    try:
        df = pd.read_csv("data.csv")

        # Convert id column to string for safe matching
        df["id"] = df["id"].astype(str)
        user_id = str(user_id)

        # Check if user exists
        if user_id not in df["id"].values:
            messagebox.showerror("Error", f"User ID {user_id} not found!")
            return

        user_row = df[df["id"] == user_id].iloc[0]

        # Create popup window
        win = tk.Tk()
        win.title(f"Details for User ID: {user_id}")
        win.geometry("400x600")

        text = tk.Text(win, font=("Arial", 12))
        text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for col, val in user_row.items():
            text.insert(tk.END, f"{col} : {val}\n\n")

        text.config(state=tk.DISABLED)
        win.mainloop()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------------------
# Example call
# ---------------------------


def show_multiple_users(id_list):
    try:
        df = pd.read_csv("data.csv")
        df["id"] = df["id"].astype(str)

        # Filter dataset for provided IDs
        filtered = df[df["id"].isin([str(i) for i in id_list])]

        if filtered.empty:
            messagebox.showerror("Error", "No matching user IDs found!")
            return

        # Tkinter main window
        win = tk.Tk()
        win.title("User Recommendations")
        win.geometry("900x600")

        # Scrollable container
        container = ttk.Frame(win)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Display in 3 columns
        col_count = 3
        row_num = 0
        col_num = 0

        for _, row in filtered.iterrows():
            # Create a card widget
            card = ttk.LabelFrame(scroll_frame, text=f"User {row['id']}", padding=10)
            card.grid(row=row_num, column=col_num, padx=15, pady=15, sticky="nw")

            # Add user details inside the card
            for col, val in row.items():
                ttk.Label(card, text=f"{col}: {val}", font=("Arial", 10)).pack(anchor="w", pady=1)

            # Move to next column
            col_num += 1
            if col_num == col_count:
                col_num = 0
                row_num += 1

        win.mainloop()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ----------------------------
# Example call:
# ----------------------------
# show_multiple_users(["101","102","103","104","105","106","107","108","109","110"])

