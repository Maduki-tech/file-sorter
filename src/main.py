import os
import shutil



def list_files(folder):
    files = []
    """List all files in folder"""
    for file in os.listdir(os.path.expanduser(folder)):
        # skip folders
        if os.path.isdir(os.path.expanduser(folder + "/" + file)):
            continue
        files.append(file)
    return files

def move_files(file, folder):
    # if folder does not exist, create it
    if not os.path.exists(os.path.expanduser(folder)):
        os.makedirs(os.path.expanduser(folder))
    # move file to folder
    os.rename(os.path.expanduser("~/Downloads/" + file), os.path.expanduser(folder + "/" + file))

def get_file_type(file):
    """Get file type"""
    file_type = file.split(".")[-1]
    return file_type
    pass

def get_file_destination(file, file_type):
    """Get file destination"""
    image_types = ["jpg", "jpeg", "png", "gif", "svg", "bmp", "jpeg"]
    document_types = ["doc", "docx", "pdf", "txt", "xls", "xlsx", "ppt", "pptx"]
    video_types = ["mp4", "avi", "mov", "wmv", "flv", "mkv"]
    audio_types = ["mp3", "wav", "ogg", "flac", "aac"]
    compressed_types = ["zip", "rar", "tar", "gz", "7z"]
    executable_types = ["exe", "msi"]
    code_types = ["py", "js", "html", "css", "cpp", "c", "java", "go", "php", "rb", "sh"]
    if file_type in image_types:
        return "~/Downloads/Images"
    elif file_type in document_types:
        return "~/Downloads/Documents"
    elif file_type in video_types:
        return "~/Downloads/Videos"
    elif file_type in audio_types:
        return "~/Downloads/Audios"
    elif file_type in compressed_types:
        return "~/Downloads/Compressed"
    elif file_type in executable_types:
        return "~/Downloads/Executables"
    elif file_type in code_types:
        return "~/Downloads/Code"
    else:
        return "~/Downloads/Others"


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
