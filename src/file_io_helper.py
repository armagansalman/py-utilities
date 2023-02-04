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


def read_binary_chunked(fpath, CHUNK_SIZE=None):
#(
	KB = 1024
	MB = 1024 * KB
	
	if CHUNK_SIZE == None:
		CHUNK_SIZE = 16 * MB
	
	with open(fpath, 'rb') as FL:
	#(
		while True:
		#(
			chunk = FL.read(CHUNK_SIZE)
			if chunk:
				yield chunk
			else:
				# The chunk was empty, which means we're at the end
				# of the file
				return
		#)
	#)
#)

def read_text_line_iter(fpath, ENCODING="utf-8"):
#(
	with open(fpath, 'r', encoding=ENCODING) as FL:
	#(
		while True:
		#(
			chunk = FL.readline()
			if chunk:
				yield chunk
			else:
				# The chunk was empty, which means we're at the end
				# of the file
				return
		#)
	#)
#)

