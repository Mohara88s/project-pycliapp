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

    def edit_note(self, old_title, new_title, new_content, new_tag):
        if not new_title.strip() or not new_content.strip() or not new_tag.strip():
            raise ValueError("Title, content, and tag cannot be empty.")

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
        note_to_edit.tags = [new_tag]