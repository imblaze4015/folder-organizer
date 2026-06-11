from pathlib import Path

def organize_folder(target_folder: str):
    
    target_folder_path = Path.home() / target_folder

    try:
        next(target_folder_path.iterdir())
        
    except FileNotFoundError as e:
        print(f"[{type(e).__name__}]: {target_folder_path} -> {e.strerror}")
        
    except StopIteration:
        print(f"'{target_folder_path.name}' contains zero items")
    
    
