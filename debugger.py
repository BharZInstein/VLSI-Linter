import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import sqlite3
import subprocess
import os

DB_FILE = "errors.db"
selected_log_file = ""

def choose_log_file():
    global selected_log_file
    file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.txt *.log"), ("All files", "*.*")])
    if file_path:
        selected_log_file = file_path
        log_label.config(text=f"Selected: {os.path.basename(file_path)}")

def run_parser():
    if not selected_log_file:
        messagebox.showerror("Error", "Please select a log file first.")
        return
    try:
        subprocess.run(["perl", "parse_logs.pl", selected_log_file], check=True)
        messagebox.showinfo("Success", "Parsed errors saved to errors.log")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Error parsing the log.")

def populate_db():
    try:
        subprocess.run(["python3", "errors_db.py"], check=True)
        messagebox.showinfo("Success", "Database populated.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Error running errors_db.py")

def search_error():
    query = search_entry.get().strip()
    if not query:
        messagebox.showwarning("Warning", "Please enter an error to search.")
        return

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT solution FROM errors WHERE error_message LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()

    output_box.delete(1.0, tk.END)
    if results:
        for row in results:
            output_box.insert(tk.END, f"Solution: {row[0]}\n\n")
    else:
        output_box.insert(tk.END, "No solution found for that error.")

#main code for the checking thing:
root = tk.Tk()
root.title("Error Linter GUI")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="Error Linter - Debug Assistant", font=("Helvetica", 16), fg="white", bg="#1e1e1e")
title.pack(pady=10)

log_button = tk.Button(root, text="Select Log File", command=choose_log_file, width=20, bg="#007acc", fg="white")
log_button.pack()

log_label = tk.Label(root, text="No log file selected", fg="white", bg="#1e1e1e")
log_label.pack(pady=5)

actions_frame = tk.Frame(root, bg="#1e1e1e")
actions_frame.pack(pady=10)

parse_btn = tk.Button(actions_frame, text="Parse Log", command=run_parser, width=15, bg="#007acc", fg="white")
parse_btn.grid(row=0, column=0, padx=5)

populate_btn = tk.Button(actions_frame, text="Build DB", command=populate_db, width=15, bg="#007acc", fg="white")
populate_btn.grid(row=0, column=1, padx=5)

search_entry = tk.Entry(root, width=40, font=("Courier", 12))
search_entry.pack(pady=10)
search_entry.insert(0, "Type error to search...")

search_btn = tk.Button(root, text="Search Error", command=search_error, width=20, bg="#28a745", fg="white")
search_btn.pack()

output_box = scrolledtext.ScrolledText(root, width=70, height=10, bg="#252526", fg="white", font=("Courier", 10))
output_box.pack(pady=10)

root.mainloop()

