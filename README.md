# Folder Organizer

A Python tool that sorts files in a folder by their extension into subfolders.

## Features

- Moves files into subfolders named after the file extension (e.g., `.txt` → `txt/`)
- Extension-less files are placed in a `no_extension/` folder
- Hidden files (starting with a dot) are automatically skipped
- Preserves original filenames – no renaming
- Straightforward command-line usage, no flags needed

## Installation

1. **Clone the repository:**  
    ```bash
   git clone https://github.com/your-username/folder-organizer.git
    ```

2. **Create and activate a virtual environment:**
    ```bash
    # Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```
3. **Install the project and test dependencies:**
    ```bash
    pip install -e ".[test]"
    ```
4. **Run the tests to confirm everything works:**
    ```bash
    pytest
    ```

## Usage

### Command line (recommended)

After installation, the command organize-folder becomes available globally (inside the virtual environment).
You can also run the package as a Python module.

```bash
# Using the entry point (shortcut)
organize-folder Downloads

# Using python -m
python -m folder_organizer Downloads
```

The folder name is always relative to your home directory (~/).
For example, organize-folder Pictures will process ~/Pictures.

    ⚠️ No dry-run mode – files are moved immediately.
    Test first on a temporary folder if you’re unsure.

### From Python code
```python
from folder_organizer.core import organize_folder

organize_folder("Desktop")   # sorts files in ~/Desktop
```

