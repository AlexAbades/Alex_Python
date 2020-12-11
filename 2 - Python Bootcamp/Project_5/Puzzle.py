import shutil
import os
import send2trash
import re

path = r"C:\Users\Alex Abades\Documents\Python\Udemy\Python\Complete-Python-3-Bootcamp-master\12-Advanced Python " \
       r"Modules\08-Advanced-Python-Module-Exercise\unzip_me_for_instructions.zip "

shutil.unpack_archive(path, 'instructions', 'zip')

original_path = os.getcwd() + "\instructions\extracted_content"
final_path = os.getcwd()
print(original_path)
# shutil.move(original_path, final_path)

erase_path = os.getcwd() + "\instructions"

send2trash.send2trash(erase_path)
path_to_look = os.getcwd() + "\extracted_content"

with open(r"extracted_content\Instructions.txt") as f:
    content = f.read()
    print(content)

original_pattern = r"\d{3}-\d{3}-\d{4}"

text = 'my phone number is 864-345-2323'

print(re.findall(original_pattern, text))


def search(file, pattern=original_pattern):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


results = []

for folders, sub_folders, file in os.walk(os.getcwd() + "\\extracted_content"):
    for f in file:
        complete_path = folders + "\\" + f

        results.append(search(complete_path))


print(results)

for element in results:
       if element != '':
              print(element.group())