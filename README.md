# Innovaccer_Infrastructure_Assignment

## Getting Started

These instructions will let you know about the project.

### Prerequisites

- os

- humanize

The module must be in the Home folder.

#### Basic functions:
````
>> from large_size_files import get_size, list_files
>> file_path = 'path_of_the_file'
>> get_size(file_path)
>> 18.2 MB
>> directoy_path = 'path_of_the_directory'
>> list_files(directory_path)
>> ['file_1', 'file_2']
````

#### Part 1: Identify the top N large files in the given paths.
````
>> from large_size_files import top_big_files, print_top
>> N = 10
>> list_of_directories = ['Desktop', 'Documents', 'Downloads', 'Music']
>> top_big_files(list_of_directories)
>> print_top(N)
````

#### Part 2: Sort the files on Desktop on the basis of file extension and move them in separate folders in Documents folder.
````
>> from clean_the_desktop import list_files, clean_the_desktop
>> source = 'path_of_the_source_folder'
>> destination = 'path_of_the_destination_folder'
>> All_files = list_files(source)
>> clean_the_desktop(source, destination, All_files)
````

#### Bonus: Analyze directories by size and type.
````
>> from analyze import analyze_directories_by_size, analyze_directories_by_type
>> list_of_directories = ['Desktop', 'Documents', 'Downloads', 'Music']
>> analyze_directories_by_size(list_of_directories)
>> ['6.4 GB', '183.1 MB', '2.3 GB', '0 Bytes']
>> analyze.size_of_directories_in_bytes
>> [6418039037, 183061688, 2270358979, 0]
>> list_of_directories = ['Desktop']
>> analyze_directories_by_type(list_of_directories)
>> Directory: Desktop
   bin  208.5 MB
   mp4  3.5 GB
   ppt  13.2 MB
   JPG  5.5 MB
````
