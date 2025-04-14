from classes import AddressBook, NotesBook
import pickle
"""
Data Persistence Module

Provides functions for saving and loading application data using Python's pickle serialization.
Handles both AddressBook and NotesBook objects with automatic file creation for new instances.
"""


def save_addressbook(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_addressbook(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def save_notes(notes_book, filename="notes.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(notes_book, f)

def load_notes(filename="notes.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return NotesBook()

if __name__ == "__main__":
    pass
