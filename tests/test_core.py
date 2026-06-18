from pathlib import Path

import pytest

from src.folder_organizer.core import organize_folder


@pytest.fixture
def mock_home(tmp_path, monkeypatch):
    """Fixture to safely redirect Path.home() to a temporary test folder."""
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    return tmp_path


def test_organize_folder_success(mock_home):
    """
    Verifies that common files, extension-less files,
    and case variations are correctly moved.
    """
    # 1. Setup a dummy target directory inside our fake home folder
    target_dir = mock_home / "Downloads"
    target_dir.mkdir()

    # 2. Create mock files reflecting different conditions
    text_file = target_dir / "notes.txt"
    img_file = target_dir / "photo.PNG"  # Tests uppercase preservation / conversion
    no_ext_file = target_dir / "README"  # Tests extensionless files
    hidden_file = target_dir / ".env"  # Tests hidden files

    text_file.touch()
    img_file.touch()
    no_ext_file.touch()
    hidden_file.touch()

    # 3. Run your function
    organize_folder("Downloads")

    # 4. Assertions: Check if files ended up in the right folders
    assert (target_dir / "txt" / "notes.txt").exists()
    assert (target_dir / "png" / "photo.PNG").exists()
    assert (target_dir / "no_extension" / "README").exists()

    # Assertions: Check if hidden files were skipped and stayed put
    assert hidden_file.exists()
    assert not (target_dir / "env").exists()


def test_file_not_found(mock_home):
    """
    Verifies that FileNotFoundError is raised and
    passes outward when directory doesn't exist.
    """
    # We do not create the folder "MissingFolder" inside mock_home
    with pytest.raises(FileNotFoundError):
        organize_folder("MissingFolder")


def test_not_a_directory(mock_home):
    """
    Verifies that NotADirectoryError is raised when trying to
    organize a literal file instead of a folder.
    """
    # Create a file matching the target string name instead of a folder
    fake_folder_file = mock_home / "is_actually_a_file.txt"
    fake_folder_file.touch()

    with pytest.raises(NotADirectoryError):
        organize_folder("is_actually_a_file.txt")
