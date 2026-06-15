import shutil
from pathlib import Path

def organize_folder(target_folder: str):
    # Convert given folder name into Path
    target_folder_path = Path.home() / target_folder 
    
    file_script = Path(__file__).resolve()

    try:

        for content in target_folder_path.iterdir():
            
            if content.is_file():
                
                if content == file_script:
                    continue
                
                elif content.name.startswith("."):
                    continue
                
                else:
                    
                    if content.suffix == "":
                        assign_folder = "no_extension"
                    
                    else:
                        assign_folder = content.suffix[1:].lower()
                    
                    assign_folder_path = target_folder_path / assign_folder
                    assign_folder_path.mkdir(exist_ok=True)                       
                    
                    old_content_path = target_folder_path / content.name
                    new_content_path = target_folder_path / assign_folder / content.name
                    
                    shutil.move(str(old_content_path), str(new_content_path))
                        
    except FileNotFoundError as e:
        print(f"[{type(e).__name__}]: {target_folder_path} -> {e.strerror}")
    
    except NotADirectoryError as e:
        print(f"[{type(e).__name__}]: '{target_folder_path.name}' is a file, not a folder")

