import os
import shutil



def list_files(folder):
    files = []
    """List all files in folder"""
    for file in os.listdir(os.path.expanduser(folder)):
        files.append(file)
    return files

def move_files(file, folder):
    """
    Move file to destination
    """
    pass

def get_file_type(file, file_type):
    """
    Get file type
    Should use a switch statement
    """
    pass

def get_file_destination(file):
    """Get file destination"""
    pass


def main():
    folders = ["~/Downloads"]
    for folder in folders:
        files = list_files(folder)
        for file in files:
            file_type = get_file_type(file)
            file_destination = get_file_destination(file, file_type)
            move_files(file, file_destination)




if __name__ == "__main__":
    main()
