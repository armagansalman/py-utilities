"""
BSD 3-Clause License

Copyright (c) 2023, Armağan Salman

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


#( Python system imports:
from os import path as OPath
import urllib as URL
import shutil
import json
#)

#( 3rd party imports:

#)

#( Local imports:
import path_functions as Pf
import utility as Ut
#)


def move_file(source_path, dest_path):
#(
	shutil.move(source_path, dest_path)
#)


def get_file_size(file_path):
#(
	return OPath.getsize(file_path)
#)


def move_all_dir_files(source_dir_path, dest_dir_path):
#(
	""" dest_dir_path must not have trailing /
	"""
	fpaths = Pf.get_fpaths_recursively(source_dir_path)
	
	file_infos = []
	for idx, x in enumerate(fpaths):
	#(
		src_path, fname = OPath.split(x)
		info = dict()
		
		print(f"idx: {idx}")
		print(f"x: {x}")
		
		new_fname = f"{idx}-{fname}"
		new_destination_path = OPath.join(dest_dir_path.rstrip('/'), new_fname)
		
		move_file(x, new_destination_path)
		
		info["source_path"] = src_path
		info["destination_path"] = dest_dir_path
		info["moved-destination_path"] = new_destination_path
		info["file-name"] = fname
		info["moved-file-name"] = new_fname
		info["file-byte-count"] = get_file_size(x)
		info["move-date-(iso-8601-UTC)"] = Ut.get_now_iso_8601_utc("fractional")
		
		file_infos.append(info)
	#)
	
	return file_infos
#)


def main(args):
#(
	dirpath = "C:/Users/Public/DOC/Test-dir/source"
	fpaths = Pf.get_fpaths_recursively(dirpath)
	
	file_infos = move_all_dir_files("C:/Users/Public/DOC/Test-dir/source" \
			, "C:/Users/Public/DOC/Test-dir/destination")
	#
	
	with open("file_infos.json", "w") as fout:
	#(
		fout.write(json.dumps(file_infos, indent=4))
	#)
	
	
	"""
	for x in fpaths:
	#(
		print(f"abspath: {OPath.abspath(x)}")
		print(f"Byte count: {get_file_size(x)}")
		print("~ ~ ~")
	#)
	"""
#)


if __name__ == "__main__":
#(
	args = dict()
	
	main(args)
#)





