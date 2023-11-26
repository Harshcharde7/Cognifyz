import tkinter as tk
from tkinter import filedialog

def count_word_occurrences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    words = text.split()
    word_counts = {}

    for word in words:
        word = word.strip('.,!?()[]{}":;')
        if word:
            word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1

    return word_counts

def calculate_word_sum(word_counts):
    return sum(word_counts.values())

def open_file_dialog():
    file_path = filedialog.askopenfilename(initialdir=r"C:\Users\hsaro\OneDrive\Desktop", title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    
    if not file_path:
        file_path = r"C:\Users\hsaro\OneDrive\Desktop\essay.txt"

    word_counts = count_word_occurrences(file_path)
    total_word_count = calculate_word_sum(word_counts)

    # Create a new window for displaying results
    result_window = tk.Toplevel(root)
    result_window.title("Word Occurrences")

    # Create a scrollbar
    scrollbar = tk.Scrollbar(result_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a listbox to display words
    listbox = tk.Listbox(result_window, yscrollcommand=scrollbar.set)
    listbox.pack(expand=True, fill=tk.BOTH)

    # Display word occurrences
    for word, count in sorted(word_counts.items()):
        listbox.insert(tk.END, f'{word}: {count}')

    # Display total word count
    listbox.insert(tk.END, f'Total word count: {total_word_count}')

    # Configure scrollbar to work with the listbox
    scrollbar.config(command=listbox.yview)

# Create the main Tkinter window
root = tk.Tk()
root.title("Word Occurrence Analyzer")

# Create a button to open the file dialog
open_file_button = tk.Button(root, text="Open Text File", command=open_file_dialog)
open_file_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
