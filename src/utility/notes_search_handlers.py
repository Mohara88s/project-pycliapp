def search_notes(args, notes_book):
    if len(args) < 1:
        raise ValueError("Please provide a search query (title or tag)")
    
    if args[0].lower()=='tags:':
        return search_note_by_tags(args[1:],notes_book)
    elif args[0].lower()=='title:':
        return search_note_by_title(' '.join(args[1:]),notes_book)
    else:
        return search_note_by_text(' '.join(args),notes_book)


def search_note_by_tags(tags,notes_book):
    if not len(tags):
        raise ValueError("Please provide at least one tag.")

    tags = [t.lower() for t in tags]
    results = []
    for note in notes_book.all_notes():
        note_tags = [tag.lower() for tag in note.tags]
        if all(tag in note_tags for tag in tags):
            results.append(note)
    return results

def search_note_by_title(title_query, notes_book):
    title_query = title_query.strip().lower()
    results = []

    for note in notes_book.all_notes():
        if title_query in note.title.lower():
            results.append(note)
    return results

def search_note_by_text(text_query, notes_book):
    text_query = text_query.strip().lower()
    results = []

    for note in notes_book.all_notes():
        if text_query in note.content.lower():
            results.append(note)
    return results




if __name__ == "__main__":
    pass