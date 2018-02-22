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

# source = '/home/abhishek/Desktop'
source = '/home/abhishek/Desktop/dummy'
destination = '/home/abhishek/Documents/sorted_directories'

All_files = list_files(source)
# print All_files
# print '\n'

if not os.path.exists(destination):
    os.makedirs(destination)

unique_folders = []

for f in All_files:
    file_extension = f.split('.')[-1]
    if not file_extension in unique_folders:
        unique_folders.append(file_extension)
        path = destination + '/' + str(file_extension)
        if not os.path.exists(path):
            os.makedirs(path)
    des = destination + '/' + file_extension
    os.popen('cp '+ f + ' ' + des)
    # print f.split('.')[-1]
