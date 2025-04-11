class Note:
    def __init__(self, title, content, tags=None):
        self.title = title
        self.content = content
        self.tags = tags or []

    def __str__(self):
        from utility import colorize_message
        return (
                f"{colorize_message(f'Title: {self.title}', 'RED')}\n"
                f"{colorize_message(f'Tags: {" ".join(self.tags)}', 'GREEN')}\n"
                f"{colorize_message(f'Content: {self.content}', 'CYAN')}\n"
                + "-" * 30
        )
