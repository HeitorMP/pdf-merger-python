#!/usr/bin/env python3

import sys
import PyPDF2
from os import path


def get_files(args):
    """Get from argv a list of files to merge.

    Args:
        args: args = sys.argv

    Returns:
        list: A list with all pdf files to merge, or None if there are not at least 2 pdf files.
    """
    file_list = []
    for file in args[3:]:
        if path.isfile(file) and file.endswith('.pdf'):
            file_list.append(file)
        else:
            print(f'{file} not found or not pdf file!')

    return file_list if len(file_list) > 1 else None


args = sys.argv
file_list = get_files(sys.argv)

if (len(args) < 4) or (args[1] != '-o') or (not file_list):
    print(
        'Usage:\n\tpython3 pdf-merger.py -o [output-file-name] [files to merge]\n')
    exit(1)

# add .pdf if the output name given not ends with .pdf
output_name = args[2]
if not output_name.endswith('.pdf'):
    output_name = args[2] + '.pdf'


merger = PyPDF2.PdfMerger()
for file in file_list:
    try:
        merger.append(file)
    except:
        print(f'{file} is not a valid pdf file!')

try:
    merger.write(output_name)
    merger.close()
except PermissionError:
    print(f'\ncannot create {output_name}: Permission denied')
    exit(1)

print(f'{output_name} was create with success')
print('Merged files:')
for file in file_list:
    print('\t- ' + file)
print('Done')
exit(0)
