
# project-pycliapp

# 🤖 Assistant Bot

A command-line assistant written in Python for managing contacts, phone numbers, addresses, birthdays, and notes.

---

## 📦 Features:

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

## ▶️ Run in console:

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

| Command          | Description                                |
|------------------|--------------------------------------------|
| `hello`          | Greet the bot                              |
| `add`            | Add a contact: `add Name Phone`            |
| `change`         | Change a phone: `change Name NewPhone`     |
| `delete`         | Delete a contact by name                   |
| `phone`          | Show phone number by name                  |
| `all`            | Show all contacts                          |
| `add-birthday`   | Add a birthday to a contact                |
| `show-birthday`  | Show birthday by name                      |
| `birthdays`      | Show upcoming birthdays                    |
| `help`           | Show all available commands                |
| `close` / `exit` | Exit the assistant                         |

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
├── LICENSE                # LICENSE
├── pyproject.toml         # Start configurator
└── README.md              # Documentation
```

---

## 👤 Author

Created with ❤️ by Note Buddy team

---

## 📄 License

This project is licensed under the MIT License.
