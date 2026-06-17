import pytest
from pathlib import Path

def organize_folder(target_folder: str):
    # Convert given folder name into Path
    target_folder_path = Path.home() / target_folder 
    
    file_script = Path(__file__).resolve()

    try:
        for item in list(target_folder_path.iterdir()):
            if item.is_dir():
                continue
            
            if item.name.startswith("."):
                continue
            
            if item.name == file_script.name:
                continue
            
            if item.suffix == "":
                designated_folder_name = "no_extension"
            
            else:
                designated_folder_name = item.suffix[1:].lower()
            
            designated_folder = target_folder_path / designated_folder_name
            designated_folder.mkdir(exist_ok=True)
            
            transfer_file = designated_folder / item.name
            item.rename(transfer_file)
            
                        
    except FileNotFoundError as e:
        print(f"[{type(e).__name__}]: {target_folder_path} -> {e.strerror}")
        raise
    
    except NotADirectoryError as e:
        print(f"[{type(e).__name__}]: '{target_folder_path.name}' is a file, not a folder")
        raise
