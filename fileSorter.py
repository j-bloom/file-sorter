import getpass
import os
import platform
import shutil

def getUserOS():
    OS = platform.system()
    return OS

def get_username():
    user_name = getpass.getuser()
    return user_name

def getBasepath():
    user_system = getUserOS()
    user_name = get_username()

    if(user_system == 'Linux'):
        base_path = rf'/home/{user_name}/Downloads/'
        return base_path
    elif(user_system == 'Windows'):
        base_path = rf'C:/Users/{user_name}/Downloads/'
        return base_path
    elif(user_system == 'Darwin'):
        base_path = rf'/Users/{user_name}/Downloads'
        return base_path    
    else:
        print('Unknown System') 

directory_names = ["csv files", "text files", "image files", "pdf files", 
                   "video files", "audio files", "shell scripts", 
                   "drivers and executables", "presentations(powerpoint) files",
                   "zip files"]

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", 
                    ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", 
                    ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", 
                    ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", 
                    ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico",]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", 
                    ".flv", ".swf", ".avchd", ".aiff"]

audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac",]

text_document_extensions = [".doc", ".docx", ".odt",]

csv_document_extensions = [".csv", ".xls", ".xlsx",]

shell_document_extensions = [".sh",]

pdf_document_extensions = [".pdf",]

windows_extensions = [".sys", ".dll", ".drv", ".ocx", ".ax", ".exe", ".com", 
                      ".bat", ".pif", ".msi", ".appinstaller",]

presentation_document_extensions = ["ppt", ".pptx"]

zip_file_extension = [".zip", ".7z"]

dest_dir_image = os.path.abspath(getBasepath() + '/image files')
dest_dir_video = os.path.abspath(getBasepath() + '/video files')
dest_dir_audio = os.path.abspath(getBasepath() + '/audio files')
dest_dir_text = os.path.abspath(getBasepath() + '/text files')
dest_dir_csv = os.path.abspath(getBasepath() + '/csv files')
dest_dir_pdf = os.path.abspath(getBasepath() + '/pdf files')
dest_dir_shell = os.path.abspath(getBasepath() + '/shell scripts')
dest_dir_presentation = os.path.abspath(getBasepath() + '/presentation (powerpoint) files')
dest_dir_windows = os.path.abspath(getBasepath() + '/drivers and executables')
dest_dir_zip = os.path.abspath(getBasepath() + '/zip files')


def move_files():
    base_path = getBasepath()
    user_system = getUserOS()

    for i in range(len(directory_names)):
        if os.path.exists(os.path.join(base_path, directory_names[i])):
            print(directory_names[i] +' already exists')
        else:
            os.makedirs(os.path.join(base_path, directory_names[i]))

    for entry in os.listdir(base_path):
        for extension in image_extensions:
            if entry.endswith(extension):
                shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_image, entry))

        for extension in video_extensions:
            if entry.endswith(extension):
                shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_video, entry))

        for extension in audio_extensions:
            if entry.endswith(extension):
                shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_audio, entry))
            
        for extension in text_document_extensions:
            if entry.endswith(extension):
                shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_text, entry))

        for extension in csv_document_extensions:
            if entry.endswith(extension):
                shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_csv, entry))

        for extension in presentation_document_extensions:
            if entry.endswith(extension):
                shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_presentation, entry))

        for extension in pdf_document_extensions:
            if entry.endswith(extension):
                shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_pdf, entry))

        for extension in zip_file_extension:
            if entry.endswith(extension):
                shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_zip, entry))

        if (user_system == 'Linux' or user_system == 'Darwin'):
            for extension in shell_document_extensions:
                if entry.endswith(extension):
                    shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_shell, entry))

        if(user_system == 'Windows'):
            for extension in windows_extensions:
                if entry.endswith(extension):
                    shutil.move(os.path.join(base_path, entry), os.path.join(dest_dir_windows, entry))


if __name__ == "__main__":
    move_files()
