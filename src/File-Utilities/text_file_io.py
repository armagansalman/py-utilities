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

from type_aliases import *



def write_textlist_general(fileref: t_Str, data: t_List[t_Str], \
                            filemode: t_Str, encoding_prm: t_Str):
#(
    with open(fileref, filemode, encoding=encoding_prm) as fobj:
    #(
        for text in data:
        #(
            fobj.write(text)
        #)
    #)
#)


def remove_file(fileref: t_Str) -> t_Bool:
#(
    if os.path.isfile(fileref):
    #(
        os.remove(fileref)
        return True
    #)
    
    return False
#)


def append_utf8_list(fileref: t_Str, data: t_List[t_Str]):
#(
    write_textlist_general(fileref, data, filemode="a", encoding_prm="utf8")
#)


def try_1():
#(
    data = ["abc", "def", "şğüçö"]
    
    append_utf8_list("test-out.txt", data)
#)


def try_2():
#(
    data = ["abc", "def", "şğüçö"]
    
    write_utf8_list("test-out.txt", data)
#)


def try_3():
#(
    fref = "test-out.txt"
    remove_file(fref)
#)


if __name__ == "__main__":
#(
    # try_1()
    # try_2()
    try_3()
#)










