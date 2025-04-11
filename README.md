
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

### 2. Install in development mode:
```bash
pip install -e .
```

### 3. Install for user:
```bash
pip install .
```

---

## ▶️ Run in console

```bash
project-pycliapp
```

---

## ⚠️ If the command is not recognized (Windows)

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

| Command                 | Description                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `hello`                 | Greet the bot                                                                                                                               |
| `add-contact`           | Add a new contact or a new phone to the contact in the format `add-contact NAME PHONE`                                                      |
| `all-contacts`          | Show all contacts in detail in the format `all-contacts`                                                                                    |
| `delete-contact`        | Delete contact in the format `delete-contact NAME`                                                                                          |
| `search-contact`        | Search contacts by: 1) name, 2) phone, 3) birthday, 4) email. Format: `search-contact TYPE VALUE` or `search-contact` for interactive mode  |
| `phone`                 | Show available phone numbers by name in the format `phone NAME`                                                                             |
| `edit-phone`            | Change contact phone number in the format `edit-phone NAME OLD_PHONE NEW_PHONE`                                                             |
| `add-birthday`          | Add date of birth to a contact in the format `add-birthday NAME DD.MM.YYYY`                                                                 |
| `birthday`              | Show contact's date of birth in the format `birthday NAME`                                                                                  |
| `birthdays`             | Show upcoming birthdays in the format `birthdays LIMIT_OF_DAYS_UNTIL_BIRTHDAY`                                                              |
| `add-note`              | Add note `add-note TITLE \"CONTENT\" TAG`                                                                                                   |
| `note`                  | Show note by title `note TITLE`                                                                                                             |
| `all-notes`             | Show all notes `all-notes`                                                                                                                  |
| `edit-note`             | Edit a note `edit-note OLD_TITLE NEW_TITLE \"NEW_CONTENT\" NEW_TAG`                                                                         |
| `delete-note`           | Delete note by title `delete-note TITLE`                                                                                                    |
| `search-note`           | Search notes by title, tags or query in the format [search-note title: TITLE] or [search-note tags: TAGS] or [search-note QUERY]            |
| `search-notes-by-tag`   | Search sorted tags which are similar to query and connectet to them notes in the format [search-notes-by-tag QUERY]                         |
| `help`                  | Show list of available commands in the format                                                                                               |
| `close` / `exit`        | Exit the assistant                                                                                                                          |

---

## 📁 Project Structure

```
project-pycliapp/
├── src/
│   |──components/         # Classes: AddressBook, Record, Field, etc.
│   |──utility/            # Functions, input/output handlers
│   └── main.py            # Entry point
├── .gitignore             # Gitignore
├── addressbook.pkl        # Addressbook storage
├── notes.pkl              # Notes storage
├── LICENSE                # LICENSE
├── pyproject.toml         # Start configurator
└── README.md              # Documentation
```

---

## 👤 Authors

Created with ❤️ by ThePythonWay team:

**Team Lead:** 

Vitalii Vasylets
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mohara88s)
 
**Scrum Master:**м

Kostiantyn Talamaniuk
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/antifloodbot)

**Developers:** 

Yevhenii Kanivets
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/EZDIVINER)

Tetiana Makara
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Tetiana-co)

---
## 📄 License

This project is licensed under the MIT License.
