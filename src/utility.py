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
# from datetime import timezone
import datetime as mDatetime
from dataclasses import dataclass
import enum as mEnum # Enum, unique ; # @mENUM.unique
#)

#( 3rd party imports:

#)

#( Local imports:
import type_definitions as TD
import utility as mUtil
#)


#(
#)


def prepend_indices_to_datas(indata):
#(
	return enumerate(indata)
#)


def convert_to_list(data):
#(
	if type(data) != list:
	#(
		return list(data)
	#)
	else:
	#(
		return data
	#)
#)


def get_now_datetime_utc() -> mDatetime.datetime:
#(
	return mDatetime.datetime.now(mDatetime.timezone.utc)
#)


def get_now_iso_8601_utc(str_format = None) -> str:
	""" iso-8601 datetime string format:
	yyyy-mm-ddThh:mm:ss.fff+|-hhmm
	2008-09-15T15:53:26+04:30
	"""
#(
	now: mDatetime.datetime = get_now_datetime_utc()
	
	iso_8601_datetime_format = str_format
	if str_format == None:
	#(
		# Default format doesn't use milliseconds
		iso_8601_datetime_format = "%Y-%m-%dT%H:%M:%S+00"
	#)
	if str_format == "fractional":
	#(
		# Default format doesn't use milliseconds
		iso_8601_datetime_format = "%Y-%m-%dT%H:%M:%S.%fZ" # Z == +00:00
	#)
	
	# iso-8601 with millisecond:
	# iso_8601_datetime_format = "%Y-%m-%dT%H:%M:%S.%f+00:00"
	
	return now.strftime(iso_8601_datetime_format)
#)

def datetime_examples():
#(	
	# Getting the current date
	# and time
	dt = datetime.datetime.now(datetime.timezone.utc)
		
	utc_time = dt.replace(tzinfo=datetime.timezone.utc)
	utc_timestamp = utc_time.timestamp()

	now = dt
	now_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")

	print(now_str)
	print(get_now_iso_8601_utc())
	print(utc_time)
	print(utc_timestamp)
#)


