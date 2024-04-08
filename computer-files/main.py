from pathlib import Path
from datetime import datetime

import zipfile


def get_files_info():
    p1 = Path('files/ghi.txt')
    print(type(p1))

    if not p1.exists():
        with open(p1, 'w') as file:
            file.write('Content 3')


    print(p1.name) #file name with extension
    print(p1.stem) #file name without extension
    print(p1.suffix) #file with just extension


    p2 = Path('files') # path to files directory
    print(list(p2.iterdir()))

def add_prefix_to_files():
    root_dir = Path('files')
    file_paths = root_dir.iterdir()
    print(Path.cwd())
    for path in file_paths:
        new_filename = "new-" + path.stem + path.suffix
        new_filepath = path.with_name(new_filename)
        print(new_filepath)
        path.rename(new_filepath)

def rename_all_files_based_on_folder():
    root_dir = Path('files')
    file_paths = root_dir.glob("**/*") # get all the items inside path

    for path in file_paths:
        if path.is_file():
            parent_folder = path.parts[-2]
            new_filename = parent_folder + '-' + path.name
            print(new_filename)
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)

def rename_all_files_based_on_sub_sub_folder():

    root_dir = Path('files')

    for path in root_dir.glob("**/*"): # get all the items inside path
        if path.is_file():
            parent_folder = path.parts
            subfolders = path.parts[1:-1]

            new_filename = "-".join(subfolders) + '-' + path.name
            print(new_filename)
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)

def add_created_date_all_files_in_folder():
    root_dir = Path('files')

    for path in root_dir.glob("**/*"): # get all the items inside path
        if path.is_file():
            created_date = datetime.fromtimestamp(path.stat().st_ctime)
            created_date_str = created_date.strftime("%Y-%m-%d_%H:%M:%S")
            new_filename = created_date_str + '_' + path.name
            new_filepath = path.with_name(new_filename)
            path.rename(new_filepath)

def change_files_extensions():
    root_dir = Path('files')

    for path in root_dir.rglob("*.csv"): # rglob - Performs a recursive glob in the current working directory
        if path.is_file():
            new_filepath = path.with_suffix(".txt")
            path.rename(new_filepath)
        
def create_empty_files():
    root_dir = Path('files')

    for i in range(10, 21):
        filename = str(i) + '.txt'
        filepath = root_dir / Path(filename)
        filepath.touch()
        
def create_archive_from_files():
    root_dir = Path('files')
    archive_path = root_dir / Path('archive.zip')

    with zipfile.ZipFile(archive_path, 'w') as zf:
        for path in root_dir.rglob("*.txt"):
            zf.write(path)
            # path.unlink() # delete files after archive - one by one

        
def extract_all_zip_files():

    root_dir = Path('.')
    destination_path = Path('destination')

    for path in root_dir.glob("*.zip"):
        with zipfile.ZipFile(path, 'r') as zf:
            final_path = destination_path / Path(path.stem)
            zf.extractall(path=final_path)
        
def search_file_in_computer():
    root_dir = Path('.')
    search_term = '14'

    for path in root_dir.rglob("*"):
        if path.is_file():
            if search_term in path.stem:
                print(path.absolute())

def destroy_files_permanently():
    root_dir = Path('destination')

    for path in root_dir.glob("*.csv"):
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()