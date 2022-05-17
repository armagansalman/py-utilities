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



import os
from pathlib import PurePath


from type_aliases import *

from string_transformer import t_StrData, t_StrPack, t_StrPackList, t_PackCreator, t_PackCreatorList, transform_string, multiple_string_transform


#(
def get_fpaths_recursively(PATH: str):
    rec_files: t_Set = set()
    # TODO(armaganslmn): ??? Error handling.
    ap = os.path.abspath(PATH)
    
    if os.path.isfile(ap):
        rec_files.add(ap)
        return rec_files
    #
    
    elif os.path.isdir(ap):
        for root, dirs, files in os.walk(ap):
            for name in files:
                p = os.path.join(root, name)
                rec_files.add(os.path.abspath(p))
            #
        #
    #
    
    else: # Link or something else. Ignore them.
        pass
    #
    return rec_files
###
#)


#(
def abspath_to_strpack(abspath: t_Str) -> t_StrPack:
    # t_StrPack == (t_Str, t_Dict)
    pure = PurePath(abspath)
    
    # pure.parts = Ordered parts of the path returned as a tuple. Last one is filename.
    dirparts = pure.parts[:-1]
    filename = pure.parts[-1]  # Last holds filename.
    
    strdata = {"dirparts": tuple(dirparts)}
    
    return ( filename, strdata )
###
#)


#(
def try_1():
    src_path = "D:\\ALL BOOKS-PAPERS"
    
    paths_absolute = get_fpaths_recursively(src_path)
    
    for p in paths_absolute:
        print(p)
    #
    print(len(paths_absolute))
###
#)


#(
def try_2():
    abspath = "D:\ALL BOOKS-PAPERS\Science, Math documents\MATH\math filename-5395-pdf.pdf"
    res = abspath_to_strpack(abspath)
    print(res)
###
#)

# try_1() # Get all full paths.

try_2()



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