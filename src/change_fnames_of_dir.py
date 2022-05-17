"""
MIT License

Copyright (c) 2022 Armağan Salman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    > WHY
    To change with flexibility the file names under one directory/folder.
    
"""


import os

from typing import Tuple # Can't use tuple[list[str], str] for Python ver. below 3.8 ; must use typing.Tuple
from typing import List
from typing import Callable


FName_t = str
DirName_t = str
NameDir_t = Tuple[FName_t, DirName_t]
MultiNameDir_t = Tuple[List[FName_t], DirName_t]
ChangedName_t = FName_t
NameGenFun_t = Callable[[NameDir_t], ChangedName_t]


def names_under_dir(dir_path: str):
    assert(os.path.isdir(dir_path))
    
    names = os.listdir(dir_path)
    
    return (names, dir_path)
###


def combine_folder_filename(folder: str, filename: str) -> str:
    combined = os.path.join( folder, filename )
    
    if os.path.isfile(combined) or os.path.isdir(combined):
        return os.path.abspath(combined)
    #
    else:
        err = "{} not a file or directory.".format(combined)
        raise Exception(err)
    #
###


def bulk_generate_names(names_dir: MultiNameDir_t, name_generator: NameGenFun_t) \
            -> MultiNameDir_t:
    #
    many_names: List[str] = names_dir[0]
    folder: str = names_dir[1]
    
    generated_names = []
    for name in many_names:
        name_dir = (name, folder)
        new_name: ChangedName_t = name_generator(name_dir)
        
        generated_names.append(new_name)
    #
    return (generated_names, folder)
###


def crop_from_start(str_from_start: str) -> NameGenFun_t:
    def cropper(arg: NameDir_t) -> str:
        if arg[0].startswith(str_from_start):
            crop_len = len(str_from_start)
            return arg[0][crop_len:]
        #
        else:
            return arg[0]
        #
    ###
    return cropper
###


def add_str_to_first_word(to_append: str) -> NameGenFun_t:
    def concatter(arg: NameDir_t):
        name = arg[0]
        splitter = ' '
        parts = name.split(splitter)
        first_word = parts[0]
        added = first_word + str(to_append)
        parts[0] = added
        
        return splitter.join(parts)
    ###
    return concatter
###


def prepend_str_to_first_word(to_prepend: str) -> NameGenFun_t:
    def concatter(arg: NameDir_t):
        name = arg[0]
        splitter = ' '
        parts = name.split(splitter)
        first_word = parts[0]
        added = str(to_prepend) + first_word
        parts[0] = added
        
        return splitter.join(parts)
    ###
    return concatter
###


# dirp = "."
# dirp = "C:\\Users\\armagan\\Desktop\\Temp items\\music change name"
dirp = "D:/Documents/Aile/tmp music/to change names_2"

mult_name_dir = names_under_dir(dirp)
old_names, orig_dir = mult_name_dir

generated_namesdir = bulk_generate_names(mult_name_dir, crop_from_start("9convert.com - "))

"""
generated = generated_namesdir[0]
folder = generated_namesdir[1]

new_names = generated
"""

"""
for i in range(len(generated)):
    orig, genr = old_names[i], new_names[i]
    print("+++++++++++++++++++++++++++++")
    print("Folder: {}".format(folder))
    print("old -> new preview = <<{}>> # <<{}>>".format(orig, genr))
#
"""

str_to_add = ",5"
generated_namesdir2 = bulk_generate_names( generated_namesdir, add_str_to_first_word(str_to_add) )

# str_to_add = "7,"
# generated_namesdir2 = bulk_generate_names( generated_namesdir, prepend_str_to_first_word(str_to_add) )

generated = generated_namesdir2[0]
folder = generated_namesdir2[1]

new_names = generated

assert(len(old_names) == len(new_names))

"""
for i in range(len(generated)):
    orig, genr = old_names[i], new_names[i]
    print("+++++++++++++++++++++++++++++")
    print("Folder: {}".format(folder))
    print("old -> new preview = <<{}>> ### <<{}>>".format(orig, genr))
#
"""

#(
import shutil

source_dir = orig_dir
source_names = old_names

dest_dir = os.path.join(source_dir, "renamed copies")
dest_names = new_names


for i in range(len(generated)):
    src, dest = source_names[i], dest_names[i]
    
    source_full = os.path.join(source_dir, src)
    dest_full = os.path.join(dest_dir, dest)
    
    print("+++++++++++++++++++++++++++++")
    print(source_full)
    print("will be copied to:")
    print(dest_full)
    
    
    # Use copy after you're sure you have the right data.
    if os.path.isfile(source_full):
        # shutil.copy(source_full, dest_full)
    #
#
#)










