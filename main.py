import os

def arrange_files(files, extension):
    files_with_extention =  [file for file in files if file.endswith(extension)]
    print(files_with_extention)
    os.mkdir("images")
    i = 1
    for file in files_with_extention:
        os.rename(file, f"images/photo-{i}{extension}")
        i += 1
    
if __name__ == "__main__":
    files = os.listdir()
    arrange_files(files, ".jpg")