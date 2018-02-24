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

def top_big_files(list_of_directories):
    global files_and_sizes
    All_files = []
    All_file_sizes = []
    for directory in list_of_directories:
        list_of_files = list_files(directory)
        # print list_of_files
        size_of_files = []
        for f in list_of_files:
            size_in_MB = get_size(f)/(1024.0*1024.0)
            size_of_files.append(size_in_MB)
        # print size_of_files
        All_files += list_of_files
        All_file_sizes += size_of_files
    
    files_and_sizes = zip(All_file_sizes, All_files)
    files_and_sizes.sort()
    length = len(files_and_sizes)
    return files_and_sizes[::-1]

def print_top(N):
    for i in range(N):
        print files_and_sizes[i][1], files_and_sizes[i][0]

list_of_directories = ['/home/abhishek/Desktop', '/home/abhishek/Documents', '/home/abhishek/Downloads', '/home/abhishek/Music']

files_and_sizes = top_big_files(list_of_directories)
# print files_and_sizes

print_top(4)
