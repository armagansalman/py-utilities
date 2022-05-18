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
        WHAT this module is for
    + This module was meant to provide functions that'll move many files in many
    dirs into one dir while adding id's to files.
    + The paths files have before copying will be stored in a .txt file along with
    the date of copy.
"""


#( TODO(armagan)-2022-05-17T22:25
#( Update(armagan)-2022-05-18T13:01:15
#  Do things below only for relational file manager. Don't expand this module beyond
#  its responsibilities.
#)
#  For each file F under directory D(F), create a new dir named "file store" under
#  D(F) and put all F's inside it. Give them unique ids. Store id and name 
#  relations inside a txt file under D(F)/file store so that original file names
#  can be restored if needed. Also put original paths of the files inside that txt
#  file.
#)


import os
from pathlib import Path, PurePath
import datetime


from type_aliases import *

from string_transformer import t_StrData, t_StrPack, t_StrPackList, t_PackCreator, t_PackCreatorList, transform_string, multiple_string_transform

import text_file_io as TxtIO



def get_utc_datetime_now():
#(
    return datetime.datetime.now()
#)


def time_now_iso8601():
#(
    now = get_utc_datetime_now()
    
    now_str = "{}-{}-{}T{}:{}:{}".format(now.year, now.month, \
        now.day, now.hour, now.minute, now.second)
    
    return now_str
#)


def get_fpaths_recursively(PATH: str):
#(
    rec_files: t_Set = set()
    # TODO(armaganslmn): ??? Error handling.
    ap = os.path.abspath(PATH)
    
    if os.path.isfile(ap):
    #(
        rec_files.add(ap)
        return rec_files
    #)
    
    elif os.path.isdir(ap):
    #(
        for root, dirs, files in os.walk(ap):
        #(  
            for name in files:
            #(
                p = os.path.join(root, name)
                rec_files.add(os.path.abspath(p))
            #)
        #)
    #)
    
    else: # Link or something else. Ignore them.
    #(
        pass
    #)
    
    return rec_files
#)


#(
def abspath_to_strpack(abspath: t_Str) -> t_StrPack:
#(
    # t_StrPack == (t_Str, t_Dict)
    pure = PurePath(abspath)
    
    # pure.parts = Ordered parts of the path returned as a tuple. Last one is filename.
    dirparts = pure.parts[:-1]
    filename = pure.parts[-1]  # Last holds filename.
    
    strdata = {"dirparts": tuple(dirparts)}
    
    return ( filename, strdata )
#)



def try_1():
#(
    src_path = "D:\\ALL BOOKS-PAPERS"
    
    paths_absolute = get_fpaths_recursively(src_path)
    
    for p in paths_absolute:
        print(p)
    #
    print(len(paths_absolute))
#)


def try_2():
#(
    abspath = "D:\ALL BOOKS-PAPERS\Science, Math documents\MATH\math filename-5395-pdf.pdf"
    res = abspath_to_strpack(abspath)
    return res
#)


def try_3():
#(
    dir_1 = "D:\\ALL BOOKS-PAPERS"
    
    all_files = get_fpaths_recursively(dir_1)
    
    lined_paths = '\n'.join(all_files)
    
    out_file = "file_list.txt"
    
    TxtIO.append_utf8_list(out_file, lined_paths)
#)


def try_4():
#(
    dir_1 = "D:\\ALL BOOKS-PAPERS"
    
    files_abs = get_fpaths_recursively(dir_1)
    
    strpacks = []
    for path in files_abs:
    #( Split filenames from their dirs. Collect them as packs.
        path_obj = Path(path)
        
        fname = path_obj.name
        
        pack = ( fname, {"source_full_path": path_obj.as_posix()} )
        
        strpacks.append(pack)
    #)
    
    out_data = map(str, strpacks)
    out_data = "\n\n".join(out_data)
    
    out_file = "try_4-file_list.txt"
    
    TxtIO.remove_file(out_file)
    TxtIO.append_utf8_list(out_file, out_data)
#)


def try_5():
#(
    dir_1 = "D:\\ALL BOOKS-PAPERS"
    
    files_abs = get_fpaths_recursively(dir_1)
    
    strpacks = []
    for path in files_abs:
    #( Split filenames from their dirs. Collect them as packs.
        path_obj = Path(path)
        
        fname = path_obj.name
        
        pack = ( fname, {"source_full_path": path_obj.as_posix()} )
        
        strpacks.append(pack)
    #)
    
    out_data = map(str, strpacks)
    out_data = "\n\n".join(out_data)
    
    out_file = "try_4-file_list.txt"
    
    TxtIO.remove_file(out_file)
    TxtIO.append_utf8_list(out_file, out_data)
#)


if __name__ == "__main__":
#(
    # try_1() # Get all full paths.
    
    #fname, fdirparts = try_2()
    #new_fname = "r10_1--" + fname
    #print(new_fname)
    #print(fdirparts)
    
    # try_3()
    
    # try_4()
    
    assert(1 == 0)
#)



"""
To do overwrite, one must first call remove_file function then call append_utf8_list function. This approach was chosen to minimize accidental data deletion.

text_file_io.py
    remove_file(fileref: t_Str)
    append_utf8_list(fileref: t_Str, data: t_List[t_Str])
"""


"""
#(
import os
def fixpath(path):
    return os.path.abspath(os.path.expanduser(path))
#)
os.path.basename(file_path)  # Returns file name from path string.
os.path.dirname(real_path)  # Returns directory name from path string.
"""


"""
https://stackoverflow.com/questions/26328650/how-to-get-left-part-of-path-in-python/26329375#26329375
https://stackoverflow.com/a/26329375
>>> from pathlib import PurePath
>>> p = PurePath('1/foo/bar/test.jpg')
>>> p.parts
('1', 'foo', 'bar', 'test.jpg')
+++++++++++++++++++++++++++++++++++++++++++++++++

>>> from pathlib import PurePath
>>> p = PurePath('/var/tmp/workdir/1/foo/bar/test.jpg')
>>> p = p.relative_to('/var/tmp/workdir')
>>> p.parts
('1', 'foo', 'bar', 'test.jpg')
"""




"""
def try_4():
#(
    dir_1 = "D:\\ALL BOOKS-PAPERS"
    
    files_abs = get_fpaths_recursively(dir_1)
    
    strpacks = []
    for path in files_abs:
    #( Split filenames from their dirs. Collect them as packs.
        # fname = os.path.basename(path)
        # file_dir = os.path.dirname(path)
        
        p = PurePath(path)
        
        fname = p.parts[-1]  # Last part is filename.
        dirparts = tuple( p.parts[ : -1] )  # Every part till the last is a dir part.
        
        pack = ( fname, {"dirparts": dirparts} )
        
        strpacks.append(pack)
    #)
    
    
    out_data = map(str, strpacks)
    out_data = '\n'.join(out_data)
    
    out_file = "try_4-file_list.txt"
    
    TxtIO.remove_file(out_file)
    TxtIO.append_utf8_list(out_file, out_data)
#)
"""