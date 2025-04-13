class Note:
    """
    Represents a single note with a title, content, and optional tags.
    """
    def __init__(self, title, content, tags=None):
        """
        Initialize a Note instance.
        Args:
            title (str): The title of the note.
            content (str): The content of the note.
            tags (list, optional): A list of tags. Defaults to empty list.
        """
        super().__init__()
        self.title = title
        self.content = content
        self.tags = tags or []

    def __str__(self):
    
    # Return a colorized string representation of the note.
    
        from utilities import colorize_message
        title_str = colorize_message(f"Title: {self.title}", 'RED')
        tags_str = colorize_message(f"Tags: {' '.join(self.tags)}", 'GREEN')
        content_str = colorize_message(f"Content: {self.content}", 'CYAN')
        return (
            f"{title_str}\n"
            f"{tags_str}\n"
            f"{content_str}\n"
            + "-" * 30
        )