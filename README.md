
# project-pycliapp

# 🤖 Assistant Bot ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

A command-line assistant written in Python for managing contacts, phone numbers, addresses, birthdays, and notes.

---

## 📦 Features

1. Save contacts with names, addresses, phone numbers, emails, and birthdays
2. Display a list of contacts who have a birthday within a specified number of days from today
3. Validate phone number and email formats during creation or editing, and notify the user in case of invalid input
4. Search through the contact book
5. Edit and delete contacts
6. Save notes with textual information
7. Search notes
8. Edit and delete notes
9. Search and sort notes by keywords (tags)
10. Analyze the entered text and try to guess what the user wants, offering the closest matching commands

---

## 🚀 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Mohara88s/project-pycliapp
cd assistant-bot
```

### 2. Install in editable mode:
```bash
pip install -e .
```

### 3. Install for user:
```bash
pip install .
```

---

## ▶️ Run in console 

### 1. Run user mode

```bash
abot
```

### 2. Run development mode

```bash
abot-dev
```

---

## ⚠️ If the start command is not recognized (Windows)

After installing with:

```bash
pip install .
```

you **might not have access to the command** (e.g. `project-pycliapp`) in the terminal if the `Scripts` directory is not added to the `PATH` environment variable.

### ✅ How to fix

Run in PowerShell:

```powershell
$env:Path += ";$env:LOCALAPPDATA\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts"
```

> ⚠️ **Replace `Python.3.13` with your actual version**, if it's different!

This temporarily adds the path for the current session. To make it permanent, either:
- Use Control Panel → System → Environment Variables
- Or run in PowerShell:
```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";<your_scripts_path>", "User")
```

---

## 💬 Commands

| Command                 | Description                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------------------|
| `hello`                 | Greet the bot                                                                                                       |
| `all-contacts`          | Show all contacts in details                                                                                        |
| `delete-contact`        | Delete contact in the format `delete-contact [FIRST_NAME] [LAST_NAME]`                                              |
| `edit-name`             | Edit name of a contact in the format `edit-name [OLD_FIRST_NAME] [OLD_LAST_NAME] [NEW_FIRST_NAME] [NEW_LAST_NAME]`  |
| `search-contact`        | Search contacts by: name, phone, birthday, email interactively                                                      |
| `phone`                 | Show available phone numbers by name in the format `phone [FIRST_NAME] [LAST_NAME]`                                 |
| `edit-phone`            | Change contact phone number in the format `edit-phone NAME [OLD_PHONE] [NEW_PHONE]`                                 |
| `add-birthday`          | Add date of birth to a contact in the format `add-birthday [FIRST_NAME] [LAST_NAME] [DD.MM.YYYY]`                   |
| `edit-birthday`         | Edit birthday of a contact in the format `edit-birthday [FIRST_NAME] [LAST_NAME] [DD.MM.YYYY]`                      |
| `birthday`              | Show contact's date of birth in the format `birthday [FIRST_NAME] [LAST_NAME]`                                      |
| `birthdays`             | Show upcoming birthdays in the format `birthdays [LIMIT_OF_DAYS_UNTIL_BIRTHDAY]`                                    |
| `add-email`             | Add email to contact in the format `add-email [FIRST_NAME] [LAST_NAME] [EMAIL]`                                     |
| `edit-email`            | Edit email of a contact in the format `edit-email [FIRST_NAME] [LAST_NAME] [NEW_EMAIL]`                             |
| `add-address`           | Add address to contact in the format `add-address [FIRST_NAME] [LAST_NAME] [ADDRESS]`                               |
| `edit-address`          | Edit address of a contact in the format `edit-address [FIRST_NAME] [LAST_NAME] [NEW_ADDRESS]`                       |
| `delete-address`        | Delete address in the format `delete-address [FIRST_NAME] [LAST_NAME]`                                              |
| `add-note`              | Add note interactively                                                                                              |
| `all-notes`             | Show all notes                                                                                                      |
| `edit-note`             | Edit note interactively                                                                                             |
| `delete-note`           | Delete note interactively                                                                                           |
| `delete-all-notes`      | Delete all notes with confirmation                                                                                  |
| `search-notes`          | Search notes by title, tag, tag grupped or content interactively                                                    |
| `help`                  | Show list of available commands                                                                                     |
| `close` / `exit`        | Exit the assistant                                                                                                  |

---

## 📁 Project Structure

```
project-pycliapp/
├── src/
│   |──classes/            # Classes: AddressBook, Record, Field, etc.
│   |──utilities/          # Functions, input/output handlers, etc.
│   └── main.py            # Entry point
├── .gitignore             # Gitignore
├── addressbook.pkl        # Addressbook storage
├── notes.pkl              # Notes storage
├── LICENSE                # Licence
├── pyproject.toml         # Start configurator
└── README.md              # Documentation
```

---

## 👤 Authors

Created with ❤️ by **ThePythonWay** team:

**Team Lead** Vitalii Vasylets
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mohara88s)
 
**Scrum Master/Developer** Kostiantyn Talamaniuk
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/antifloodbot)

**Developers:** 

Yevhenii Kanivets
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/EZDIVINER)

Tetiana Makara
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Tetiana-co)

---
## 📄 License

This project is licensed under the MIT License.
