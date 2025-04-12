from classes.Note import Note

class NotesBook:
    """
    A container for managing a collection of Note instances.
    Supports adding, editing, deleting, and retrieving notes,
    with validation for title, content, and tags.
    """
    def __init__(self):
        """Initialize an empty NotesBook."""
        super().__init__()
        self.notes = []

    def add_note(self, title, content, tags):
        """
        Add a new note to the NotesBook after validation.
        Args:
            title (str): The note's title.
            content (str): The note's content.
            tags (list): A list of tag strings.
        Raises:
            ValueError: If validation fails or title already exists.
        """
        self.validate_title(title)
        self.validate_content(content)
        self.validate_tags(tags)

        for note in self.notes:
            if note.title == title:
                raise ValueError(f"Note with title '{title}' already exists.")

        unique_tags = list(set(tags))
        note = Note(title, content, unique_tags)
        self.notes.append(note)

    def all_notes(self):
        """
        Retrieve all stored notes.
        Returns:
            list: A list of Note objects.
        """
        return self.notes

    def delete_note(self, title):
        """
        Delete a note by its title.
        Args:
            title (str): Title of the note to delete.
        Returns:
            bool: True if note was found and deleted, False otherwise.
        """
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return True
        return False

    def edit_note(self, old_title, new_title, new_content, new_tags):
        """
        Edit an existing note.
        Args:
            old_title (str): Current title of the note.
            new_title (str): New title.
            new_content (str): New content.
            new_tags (list): New list of tags.
        Raises:
            ValueError: If note doesn't exist or validation fails.
        """
        self.validate_title(new_title)
        self.validate_content(new_content)
        self.validate_tags(new_tags)

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

    @staticmethod
    def validate_title(title):
        """
        Raise ValueError if title is empty or invalid.
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title cannot be empty.")

    @staticmethod
    def validate_content(content):
        """
        Raise ValueError if content is empty or invalid.
        """
        if not isinstance(content, str) or not content.strip():
            raise ValueError("Content cannot be empty.")

    @staticmethod
    def validate_tags(tags):
        """
        Raise ValueError if tags list is invalid or empty.
        """
        if not isinstance(tags, list) or not all(isinstance(tag, str) and tag.strip() for tag in tags):
            raise ValueError("At least one valid tag is required.")