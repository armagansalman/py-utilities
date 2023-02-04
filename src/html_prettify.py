"""
BSD 3-Clause License

Copyright (c) 2022-2023, Armağan Salman
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
import sys
import shutil
#
from bs4 import BeautifulSoup as BSp
#
import types_builtin as B
#

def str_repeat(string: B.t_Str, multiplier: B.t_Int) \
		-> B.t_Str:
#(
	return string * multiplier
#)

def prettify_html(text_html: B.t_Str \
		,indent_char = ' ' \
		,expand_indent_multiplier = 1) \
		-> B.t_Str:
	""" doc """
#(
	soup = BSp(text_html, features="html.parser")

	pretty_html = soup.prettify()

	if expand_indent_multiplier == 1 and indent_char == ' ':
	#(
		return pretty_html
	#)
	else:
	#(
		lines = []
		for x in pretty_html.split('\n'):
		#(
			tag_start_idx = x.find('<')
			space_cnt = tag_start_idx
			
			if tag_start_idx != -1: # Tag exists.
			#(
				new_indent = str_repeat(indent_char \
					,space_cnt * expand_indent_multiplier)
				
				new_line = new_indent + x[tag_start_idx : ]
				lines.append(new_line)
			#)
			else:
			#(
				lines.append(x)
			#)
		#)
		return '\n'.join(lines)
	#)
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
		, dest_path_html: B.t_Str \
		, indent_char = ' ' \
		, indent_multiplier: B.t_Int = 1) \
		-> B.t_Bool:
	""" Writes prettified html string to destination file path.

		Takes html file path as string.
	"""
#(
	text_src = read_text_file(source_path_html)

	text_pretty_html = prettify_html(text_src \
		, indent_char \
		, expand_indent_multiplier = indent_multiplier)

	result: B.t_Bool = write_text_file(dest_path_html, text_pretty_html)

	return result
#)
#
#
def main(args: B.t_Dict):
	"""doc"""
#(
	src_path = args["source_path"]
	dest_path = args.get("destination_path", None)

	pthead, pttail = os.path.split(src_path)

	default_out_file_prefix = "pretty-"
	if dest_path == None:
		dest_path = os.path.join(pthead, default_out_file_prefix + pttail)

	if os.path.isfile(dest_path):
	#(
		print(f"<[ ERROR ]> Didn't write pretty html to file. Destination exists. Overwrite is False by default.")
		print(f"<[ ; ]> .          : {os.path.abspath('.')}")
		print(f"<[ ; ]> Source     : {src_path}")
		print(f"<[ ; ]> Destination: {dest_path}")
		print(f"<[ ; ]> ABORTED COMPUTATION!")
		exit(1)
	#)

	success: B.t_Bool = prettify_then_write(src_path \
						, dest_path \
						, indent_char = '\t' \
						, indent_multiplier = 1)

	#( Report part.
	# else:
	#(
	print(f"<[ INFO ]> Pretty html was written to destination.")
	#)
	print(f"<[ ; ]> .          : {os.path.abspath('.')}")
	print(f"<[ ; ]> Source     : {src_path}")
	print(f"<[ ; ]> Destination: {dest_path}")
	#)
#)
#
#
def structure_argv_values(argv_values: B.t_List) \
		-> B.t_Tuple[B.t_Dict, B.t_List]:
	""" Takes sys.argv
	
		Returns a tuple
		First tuple element is a mapping: option->[option.param-1, ... ,option.param-N]
		Second tuple element is positional arguments."""
#(
	script_name = argv_values[0]
	
	if len(argv_values) < 2: #Script name + at least 1 value = at least 2
		return (dict(), [])
	
	options_and_params = argv_values[1:]
	
	opt_val_map = dict()
	positional_vals = []
	
	j = 0
	while j < len(options_and_params):
	#(
		value = options_and_params[j]
		
		if value[0] == '-': # An option
		#(
			opt_val = options_and_params[j+1] # Next element is option's value.
			opt_val_map[value] = opt_val
			j += 1
		#)
		else: # Positional value
		#(
			positional_vals.append(value)
		#)
		
		j += 1
	#)
	return (opt_val_map, positional_vals)
#)

if __name__ == "__main__":
	""" First positional argument is always input html location.
		Second positional argument is always output html location.
		Output location is optional. By default, output file name will be
		input file name prefixed by 'pretty-'
	"""
#(
	""" TODO(armagan): Fix non-tag text indentation levels. """
	opt_map, positionals = structure_argv_values(sys.argv)

	src_path = "./index.html" # Default html source path.

	if len(positionals) > 0:
		src_path = positionals[0]
		
	params = { \
		"source_path": src_path \
		,"opt_map": opt_map \
		}

	main(params)
#)
