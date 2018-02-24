import os
import humanize

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
	global size_of_directories_in_bytes, size_of_directories
	size_of_directories_in_bytes = []
	size_of_directories = []
	for directory in list_of_directories:
		size = 0
		dir_files = list_files(directory)
		for f in dir_files:
			size += get_size(f)
		size_of_directories_in_bytes.append(size)
		size_in_MB = humanize.naturalsize(size)
		size_of_directories.append(size_in_MB)
	print size_of_directories

def analyze_directories_by_type(list_of_directories):
	global info
	info = []
	for directory in list_of_directories:
		files_type_sizes = {}
		dir_files = list_files(directory)
		for f in dir_files:
			if len(f.split('/')[-1].split('.')) != 1:
				file_extension = f.split('.')[-1]
				if not file_extension in files_type_sizes and file_extension != 'desktop' :
					files_type_sizes[str(file_extension)] = 0
				if file_extension != 'desktop':
					files_type_sizes[str(file_extension)]+=get_size(f)
		info.append(files_type_sizes)
	# Change bytes to MB
	for directory in info:
		for typ in directory:
			directory[typ] = humanize.naturalsize(directory[typ])
	# Print sizes
	count = 0
	for directory in info:
		print 'Directory:  ' + str(list_of_directories[count])
		for typ in directory:
			print typ + ' ' + str(directory[typ])
	# print info
	
list_of_directories = ['/home/abhishek/Desktop']
# list_of_directories = ['/home/abhishek/Documents/sorted_directories']	
# list_of_directories = ['/home/abhishek/Desktop', '/home/abhishek/Documents', '/home/abhishek/Downloads', '/home/abhishek/Music']
# analyze_directories_by_size(list_of_directories)
analyze_directories_by_size(list_of_directories)
analyze_directories_by_type(list_of_directories)
# print size_of_directories_in_bytes
# print size_of_directories
