import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string
import os

# Function to generate a random license plate
def generate_license_plate():
    """Generates a random license plate with 3 uppercase letters and 4 digits."""
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=4))
    return letters + numbers

# Function to check if a license plate contains prohibited words (exact match)
def check_prohibited_words(plate, prohibited_words):
    """Checks if the generated plate matches any prohibited words."""
    return plate in prohibited_words

# Function to check for duplicate license plates
def check_duplicate(plate, existing_plates):
    """Checks if the generated plate already exists."""
    return plate in existing_plates

# Function to add prohibited words to the list
def add_prohibited_word():
    """Prompts user to add a prohibited word and updates the file."""
    word = simpledialog.askstring("Input", "Enter the word to prohibit:").upper()
    if word:
        if word in prohibited_words:
            messagebox.showinfo("Info", f"The word '{word}' is already in the list of prohibited words.")
        else:
            prohibited_words.add(word)
            with open('prohibited_words.txt', 'a') as file:
                file.write(word + '\n')
            messagebox.showinfo("Success", f"Added prohibited word: {word}")

# Function to generate and save a valid license plate
def generate_plate():
    """Generates a valid license plate and saves it to the file."""
    while True:
        plate = generate_license_plate()
        if not check_prohibited_words(plate, prohibited_words) and not check_duplicate(plate, existing_plates):
            with open('plates.txt', 'a') as file:
                file.write(plate + '\n')
            existing_plates.add(plate)
            messagebox.showinfo("Generated License Plate", f"{plate}")
            break
        else:
            print(f"Rejected License Plate: {plate}")

# Function to view all generated license plates
def view_license_plates():
    """Displays all generated license plates."""
    with open('plates.txt', 'r') as file:
        plates = file.read()
    messagebox.showinfo("Generated License Plates", plates if plates else "No license plates generated yet.")

# Function to view all prohibited words
def view_prohibited_words():
    """Displays all prohibited words."""
    with open('prohibited_words.txt', 'r') as file:
        words = file.read()
    messagebox.showinfo("Prohibited Words", words if words else "No prohibited words added yet.")

# Load existing plates and prohibited words from file
prohibited_words = set()
existing_plates = set()

# Ensure the files exist
open('plates.txt', 'a').close()
open('prohibited_words.txt', 'a').close()

with open('plates.txt', 'r') as file:
    for line in file:
        existing_plates.add(line.strip())

with open('prohibited_words.txt', 'r') as file:
    for line in file:
        prohibited_words.add(line.strip())

# Setup the main window
root = tk.Tk()
root.title("License Plate Generator")
root.geometry("400x300")  # Set the initial window size

# Create and place buttons on the main window with padding
generate_button = tk.Button(root, text="Generate License Plate", command=generate_plate)
generate_button.pack(pady=10)

add_word_button = tk.Button(root, text="Add Prohibited Word", command=add_prohibited_word)
add_word_button.pack(pady=10)

view_plates_button = tk.Button(root, text="View Generated Plates", command=view_license_plates)
view_plates_button.pack(pady=10)

view_words_button = tk.Button(root, text="View Prohibited Words", command=view_prohibited_words)
view_words_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(pady=10)

# Start the main event loop
root.mainloop()
