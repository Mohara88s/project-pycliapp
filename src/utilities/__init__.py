from utilities.colorize import colorize_message
from utilities.contact_handlers import add_address, add_birthday, add_contact, add_email, show_phone
from utilities.contact_handlers import change_contact
from utilities.contact_handlers import delete_address, delete_contact
from utilities.contact_handlers import edit_address, edit_birthday, edit_email, edit_name
from utilities.contact_handlers import get_all_contacts, get_upcoming_birthdays, show_birthday
from utilities.error_handler import error_handler
from utilities.handle_search_contact import handle_search_contact
from utilities.notes_handlers import add_note, delete_note, edit_note, search_note, show_all_notes, generate_boxed_notes, delete_all_notes
from utilities.parse_input_handler import parse_input
from utilities.show_all_contacts import show_all_contacts
from utilities.show_banner import show_banner
from utilities.show_birthdays import show_birthdays
from utilities.show_help import show_help
from utilities.show_search import show_search
from utilities.storage_handlers import load_addressbook, load_notes, save_addressbook, save_notes
from utilities.suggest_command import suggest_command
from utilities.user_input_handler import user_input_handler

__all__ = [
    'add_address',
    'add_birthday',
    'add_contact',
    'add_email',
    'add_note',
    'change_contact',
    'colorize_message',
    'delete_address',
    'delete_contact',
    'delete_note',
    'delete_all_notes',
    'edit_address',
    'edit_birthday',
    'edit_email',
    'edit_name',
    'edit_note',
    'error_handler',
    'generate_boxed_notes',
    'get_all_contacts',
    'get_upcoming_birthdays',
    'handle_search_contact',
    'load_addressbook',
    'load_notes',
    'parse_input',
    'save_addressbook',
    'save_notes',
    'search_note',
    'show_all_contacts',
    'show_all_notes',
    'show_banner',
    'show_birthdays',
    'show_birthday',
    'show_help',
    'show_phone',
    'show_search',
    'suggest_command',
    'user_input_handler',
]