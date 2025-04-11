from classes.Note import Note

class NotesBook:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content, tags):
        for note in self.notes:
            if note.title == title:
                raise ValueError(f"Note with title '{title}' already exists.")

        unique_tags = list(set(tags))

        note = Note(title, content, unique_tags)
        self.notes.append(note)

    def all_notes(self):
        return self.notes

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return True
        return False

    def edit_note(self, old_title, new_title, new_content, new_tags):
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Title cannot be empty.")
        if not isinstance(new_content, str) or not new_content.strip():
            raise ValueError("Content cannot be empty.")
        if not isinstance(new_tags, list) or not all(isinstance(tag, str) and tag.strip() for tag in new_tags):
            raise ValueError("At least one valid tag is required.")

        note_to_edit = None
        for note in self.notes:
            if note.title == old_title:
                note_to_edit = note
                break

        if not note_to_edit:
            raise ValueError(f"Note with title '{old_title}' not found.")

        if old_title != new_title:
            for note in self.notes:
                if note.title == new_title:
                    raise ValueError(f"Note with title '{new_title}' already exists.")

        note_to_edit.title = new_title
        note_to_edit.content = new_content
        note_to_edit.tags = list(set(tag.strip() for tag in new_tags if tag.strip()))