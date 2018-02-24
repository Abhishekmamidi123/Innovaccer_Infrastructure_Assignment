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

def analyze_directories_by_size(list_of_directories):
	size_of_directories = []
	analyze_by_type_of_files = []
	size = 0
	for directory in list_of_directories:
		dir_files = list_files(directory)
		unique_folders = {}
		for f in dir_files:
			file_extension = f.split('.')[-1]
			print f
			print file_extension
			if str(file_extension) != 'desktop':
				file_size = get_size(f)
				size += file_size
				if not file_extension in unique_folders:
					unique_folders[str(file_extension)] = size
        		else:
        			print str(file_extension)
        			unique_folders[str(file_extension)] += size
		size_of_directories.append(size)
		analyze_by_type_of_files.append(unique_folders)
		print size_of_directories
		print analyze_by_type_of_files

list_of_directories = ['/home/abhishek/Desktop']
#, '/home/abhishek/Documents', '/home/abhishek/Downloads', '/home/abhishek/Music']
analyze_directories_by_size(list_of_directories)
