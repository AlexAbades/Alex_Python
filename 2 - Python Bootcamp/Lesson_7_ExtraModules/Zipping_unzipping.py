# Zipping individual files

f = open('file_one.txt', 'w+')
f.write('FILE ONE')
f.close()

f = open('file_two.txt', 'w+')
f.write('FILE TWO')
f.close()


import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('file_one.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file_two.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# ONCE WE CREATED THE ZIPFILE, WE WANT TO EXTRACT FILES

zip_object = zipfile.ZipFile('comp_file.zip', 'r')
# Only one file
zip_object.extract('file_one.txt')
# If we want to extract more than once
zip_object.extractall('extracted_content')  # It creates a directory

import os
import shutil

dir_to_zip = os.getcwd() + "\extracted_content"


output_file_name = 'example'

# MAKEING AN .ZIP ARCHIVE
shutil.make_archive(output_file_name, 'zip', dir_to_zip)

# EXTRACTING AN ARCHIVE
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')
