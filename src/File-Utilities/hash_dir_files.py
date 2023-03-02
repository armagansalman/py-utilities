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


import hashlib
from functools import partial

import common_types as CT
import file_io_helper as Mfio
import path_functions as Mpfn


def read_file_binary_chunked(fpath):
#(
	KB = 1024
	MB = 1024 * KB
	
	CHUNK_SIZE = 16 * MB
	
	return Mfio.read_file_binary_chunked(fpath, CHUNK_SIZE)
#)

def sha512_hexdigest(fpath):
#(
	hobj = hashlib.sha512()
	for chunk in read_file_binary_chunked(fpath):
	#(
		hobj.update(chunk)
	#)
	return hobj.hexdigest()
#)

def hash_file(fpath, digest_func):
#(
	return digest_func(fpath)
#)

def hash_all_dir_files(dirpath):
#(
	all_fpaths = Mpfn.get_fpaths_recursively(dirpath)
	
	return map(lambda X: (hash_file(X,sha512_hexdigest),X) , all_fpaths)
#)

if __name__ == "__main__":
#(
	"""
	fpath = "./test_youtube.html"
	
	hexdigest = hash_file(fpath, sha512_hexdigest)
	
	print(f"sha512: {hexdigest} ~;~ {fpath}")
	"""
	
	"""
	# _dirpath = "/home/genel/Documents/E-BOOK/"
	dirpath = "/home/genel/Documents/ALL BOOKS-PAPERS/"
	
	hash_iter = hash_all_dir_files(dirpath)
	
	print(f"Directory: {dirpath}")
	for hsh, fpath in hash_iter:
	#(
		print(f"sha512: {hsh} ~;~ {fpath}")
	#)
	"""
	
	fpath = "/home/genel/Documents/GIT-LOCAL/py-utilities/src/out~ALL-BOOKS~16MB.txt"
	
	line_iter = Mfio.read_text_line_iter(fpath)
	
	for x in line_iter:
		print(x, end="")
	
#)












