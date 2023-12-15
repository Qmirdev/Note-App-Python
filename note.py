# Import Modules
import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style

# Create main window
root = tk.Tk()
root.title("Note App")
root.geometry("515x515")
# Configure style
style = Style(theme="journal")
style = ttk.Style()


# Configure font for tabs
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

# Create Notebook
notebook = ttk.Notebook(root, style="TNotebook")

# Load previously saved notes
notes = {}
try:
    with open("notes.json", "r") as f:
        notes=json.load(f)
except FileNotFoundError:
    pass

# Create and pack notebook widget
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Function to add new note
def add_note():

    # Create frame for new note
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="New Note")

    # Widgets for note title and content
    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    title_entry = ttk.Entry(note_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    content_label = ttk.Label(note_frame, text="Content:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    content_entry = tk.Text(note_frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)

    # Function to save note
    def save_note():

        # Get title and content
        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)

        # Add note to dictionary
        notes[title] = content.strip()

        # Save notes to file (JSON)
        with open("notes.json", "w") as f:
            json.dump(notes, f)

        # Add note to notebook
        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=title)

    # Save button
    save_button = ttk.Button(note_frame, text="Save",
                             command=save_note, style="secondary.TButton")
    save_button.grid(row=2, column=0, padx=10, pady=10)

# Function to load notes
def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes=json.load(f)

        # Add each note to the notebook
        for title, content in notes.items():
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)

    except FileNotFoundError:
        # Do nothing if file doesn't exists
        pass

# Load notes at start
load_notes()

# Function to delete note
def delete_note():
    # Get current tab index
    current_tab = notebook.index(notebook.select())

    # Get note title
    note_title = notebook.tab(current_tab, "text")

    # Confirm deletion
    confirm = messagebox.askyesno("Delete Note",
                                  f"Are you sure you want to delete {note_title}?")

    if confirm:
        # Remove from notebook
        notebook.forget(current_tab)

        # Remove from notes dict
        notes.pop(note_title)

        # Save notes to file
        with open("notes.json", "w") as f:
            json.dump(notes, f)

# Buttons
new_button = ttk.Button(root, text="New",
                        command=add_note, style="info.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete",
                           command=delete_note, style="primary.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()