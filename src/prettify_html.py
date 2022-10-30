"""
BSD 3-Clause License

Copyright (c) 2022, Armağan Salman
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
#
import os
import shutil
#
from bs4 import BeautifulSoup as BSp
#
import types_builtin as B
#
#
def prettify_html(text_html: B.t_Str) -> B.t_Str:
    """doc"""
#(
    soup = BSp(text_html, features="html.parser")
    
    pretty_html = soup.prettify()
    
    return pretty_html
#)
#
#
def prettify_many_htmls(iter_html_text: B.t_Iter[B.t_Str]) -> B.t_Iter[B.t_Str]:
    """ Returns prettified html strings.
    
        Takes html files as strings.
    """
#(
    return map(prettify_html, iter_html_text)
#)
#
#
def read_chunks(infile, chunk_size, offset=0):
    """doc"""
#(
    if( chunk_size + offset < 1 ):
        return
    while True:
    #(
        chunk = infile.read(chunk_size)
        if chunk:
        #(
            yield chunk
            
            if offset != 0:
              if not infile.read(1): # eof reached
                return
              infile.seek(infile.tell()+offset-1)
              # -1 to revert read(1)
        #)
        else:
            return
    #)
#)
#
#
def read_text_file_by_chunks(text_file_path: B.t_Str) -> B.t_Str:
    """ Doc
    """
#(
    KB_4 = 4 * 1024
    text: B.t_Optional[B.t_Str] = None
    
    with open(text_file_path, mode="rb") as fl:
        #
    #(
        file_chunks = []
        for x in read_chunks(fl, KB_4):
        #(
            file_chunks.append(x)
        #)
        text = ''.join(map(str, file_chunks))
    #)
    
    return str(text)
#)
#
#
def read_text_file(text_file_path: B.t_Str) -> B.t_Str:
    """ Doc
    """
#(
    with open(text_file_path, mode="r") as fl:
        #
    #(
        lines = fl.readlines()
        return ''.join(lines)
    #)
#)
#
#
def write_text_file(text_file_path: B.t_Str \
        , text_data: B.t_Str \
        , overwrite: B.t_Bool = False) \
        -> B.t_Bool:
    """ Writes text_file_path contents with text_data.
    Overwrites the target file_path if 'overwrite' is True
    
    Returns True if data was written successfully.
    Returns False if overwrite was False and file already existed.
    """
#(
    if os.path.isfile(text_file_path) and (not overwrite): # File exists but user choose not to overwrite.
    #(
        return False
    #)
    else:
    #(
        with open(text_file_path, mode="w") as fl:
        #(
            fl.write(text_data)
            return True
        #)
    #)
#)
#
#
def prettify_then_write(source_path_html: B.t_Str \
        , dest_path_html: B.t_Str) \
        -> B.t_Bool:
    """ Writes prettified html string to destination file path.
    
        Takes html file path as string.
    """
#(
    text_src = read_text_file(source_path_html)
    
    text_pretty_html = prettify_html(text_src)
    
    result: B.t_Bool = write_text_file(dest_path_html, text_pretty_html)
    
    return result
#)
#
#
def main(args):
    """doc"""
#(
    src_path = args["source_path"]
    
    pthead, pttail = os.path.split(src_path)
    dest_path = os.path.join(pthead, "pretty_" + pttail)

    success: B.t_Bool = prettify_then_write(src_path, dest_path)
    
    #( Report part.
    if not success:
    #(
        destination_exists = os.path.isfile(dest_path)
        de = destination_exists
        
        print(f"[ WARNING ] Didn't write pretty html to file. Destination exists: {de}. Overwrite is False by default.")
    #)
    else:
    #(
        print(f"[ INFO ] Pretty html was written to destination.")
    #)
    print(f"[ ; ] Source     : {src_path}")
    print(f"[ ; ] Destination: {dest_path}")
    #)
#)
#
#
if __name__ == "__main__":
#(
    src_path = "./test_youtube.html"
    params = {"source_path": src_path}
    
    main(params)
#)
