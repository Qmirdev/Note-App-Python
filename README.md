# Note App Python

This is a simple note taking app written in Python. It allows users to create, edit, and delete text notes.

## Features

- Create new notes with a title and text content
- Edit existing notes by modifying the title and text
- Delete notes
- List all existing notes with their titles
- Save notes to a JSON file for persistence
- Load notes from the JSON file at startup

> [!NOTE]
> I'll release another version of this Python Note app soon or later with more features such as searching, tagging, and more.

## Implementation

The app is implemented in Python. It uses the json module to serialize notes to JSON for persistence.

The Note class represents a single note with a title and text content. The NoteManager class handles operations on the list of notes and loading/saving to the JSON file.

## Installation

Requires Python 3.x.

Run `pip install -r requirements.txt` to install the dependencies.

- or Install them manually:

```
pip install tkinter
pip install json
pip install ttkbootstrap
```

## License

This project is licensed under the MIT license. See LICENSE for details.

## Contributing

Contributions are welcome! Please open an issue or pull request on GitHub.
