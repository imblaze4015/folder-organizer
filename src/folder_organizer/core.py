from pathlib import Path

def organize_folder(target_folder: str):
    # Convert given folder name into Path
    target_folder_path = Path.home() / target_folder 

    try:
        """
        Grab the next item from iterator. It will route to except,
        if folder doesn't exists, not a directory, or empty
        """
        next(target_folder_path.iterdir())
        
        for content in target_folder_path.iterdir():
            print(content.name)
        
    except FileNotFoundError as e:
        print(f"[{type(e).__name__}]: {target_folder_path} -> {e.strerror}")
        
    except StopIteration:
        print(f"'{target_folder_path.name}' contains zero items")
    
    except NotADirectoryError as e:
        print(f"[{type(e).__name__}]: '{target_folder_path.name}' is a file, not a folder")

