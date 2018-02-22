import os

def get_size(filename):
    st = os.stat(filename)
    return st.st_size

def list_files(dir):
    r = []
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        files = os.walk(subdir).next()[2]
        if (len(files) > 0):
            for file in files:
                r.append(subdir + "/" + file)
    return r

def clean_the_desktop(source, destination, All_files):
    if not os.path.exists(destination):
        os.makedirs(destination)
    unique_folders = []
    for f in All_files:
        file_extension = f.split('.')[-1]
        # print file_extension
        if not file_extension in unique_folders and file_extension != 'desktop' :
            unique_folders.append(file_extension)
            path = destination + '/' + str(file_extension)
            if not os.path.exists(path):
                os.makedirs(path)
        if file_extension!='desktop':
            des = destination + '/' + file_extension
            os.popen('cp '+ f + ' ' + des)

source = '/home/abhishek/Desktop/vlc'
destination = '/home/abhishek/Documents/sorted_directory'
All_files = list_files(source)
clean_the_desktop(source, destination, All_files)
