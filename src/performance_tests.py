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
import time
import random
from enum import Enum, auto as Auto
from typing import Iterable as Iter
from dataclasses import dataclass
#)

#( 3rd party imports:

#)

#( Local imports:

#)


class Shape_Type(Enum):
#(
	SQUARE = Auto()
	RECTANGLE = Auto()
	CIRCLE = Auto()
#)


@dataclass
class Shape:
#(
	kind: Shape_Type
	data: any
#)


@dataclass
class Constval:
#(
	Pi: float = 3.14
#)


class Shape_Coeffs:
#(
	mapping = {
			Shape_Type.SQUARE: 1 \
			, Shape_Type.RECTANGLE:1 \
			, Shape_Type.CIRCLE: Constval.Pi
			}
#)


def make_square(side: float):
#(
	return Shape(Shape_Type.SQUARE, [side, side])
#)


def make_rectangle(first_val: float, second_val: float):
#(
	return Shape(Shape_Type.RECTANGLE, [first_val, second_val])
#)


def make_circle(radius: float):
#(
	return Shape(Shape_Type.CIRCLE, [radius, radius])
#)


def make_many_shapes(max_count):
#(
	for i in range(max_count):
	#(
		if i%3 == 0: # Make Square
		#(
			val = random.uniform(2.0, 100.0)
			yield make_square(val)
		#)
		elif i%3 == 1:
		#(
			val = random.uniform(2.0, 100.0)
			val_2 = random.uniform(2.0, 100.0)
			yield make_rectangle(val, val_2)
		#)
		else:
		#(
			val = random.uniform(2.0, 100.0)
			yield make_circle(val)
		#)
	#)
	return None
#)


def calc_area_shape_if(shape: Shape):
#(
	area = 0.0
	shp = shape
	if shp.kind == Shape_Type.SQUARE:
	#(
		area = shp.data[0] * shp.data[1] # one side squared
	#)
	elif shp.kind == Shape_Type.RECTANGLE:
	#(
		area = shp.data[0] * shp.data[1] # width * height
	#)
	elif shp.kind == Shape_Type.CIRCLE:
	#(
		area = Constval.Pi * shp.data[0] * shp.data[1] # Pi * r^2
	#)
	else:
	#(
		raise Exception(f"Unknown Shape kind (Shape_Type): {shp.kind}")
	#)
	
	return area
#)


def calc_area_sum_if(shape_iter: Iter):
#(
	_sum = 0.0
	area = 0.0
	for shp in shape_iter:
	#(
		area = calc_area_shape_if(shp)
		
		_sum += area
	#)
	return area
#)


def calc_area_shape_table(shape: Shape):
#(
	shp = shape
	area = Shape_Coeffs.mapping[shape.kind] * shp.data[0] * shp.data[1]
	
	return area
#)


def calc_area_sum_shape_table(shape_iter: Iter):
#(
	_sum = 0.0
	area = 0.0
	for shp in shape_iter:
	#(
		area = calc_area_shape_table(shp)
		
		_sum += area
	#)
	return area
#)


def time_area_sum_if(shape_max_count):
#(
	###
	shape_count = shape_max_count
	shapes = make_many_shapes(shape_count)
	
	start_time = time.perf_counter_ns()
	
	area_sum = calc_area_sum_if(shapes)
	print(f"Area sum value: {area_sum}")
	
	end_time = time.perf_counter_ns()
	
	time_interval = (end_time-start_time)/1_000_000
	print(f"time_area_sum_if took {(time_interval)} ms")
	print(f"Time/shape_count {time_interval/shape_count} ms")
#)


def time_area_sum_table(shape_max_count):
#(
	###
	shape_count = shape_max_count
	shapes = make_many_shapes(shape_count)
	
	start_time = time.perf_counter_ns()
	
	area_sum = calc_area_sum_shape_table(shapes)
	print(f"Area sum value: {area_sum}")
	
	end_time = time.perf_counter_ns()
	
	time_interval = (end_time-start_time)/1_000_000
	print(f"time_area_sum_table took {(time_interval)} ms")
	print(f"Time/shape_count {time_interval/shape_count} ms")
#)


def main(args):
#(
	shape_max_count = 1_000_000
	for i in range(3):
	#(
		time_area_sum_if(shape_max_count)
	#)

	for i in range(3):
	#(
		time_area_sum_table(shape_max_count)
	#)
#)


if __name__ == "__main__":
#(
	args = dict()
	
	main(args)
#)





"""
start_time = time.perf_counter_ns()
	
	
	shape_count = 1_000_000
	shapes = make_many_shapes(shape_count)
	
	
	end_time = time.perf_counter_ns()
	
	time_interval = (end_time-start_time)/1_000_000
	print(f"Shape count: {shape_count}")
	print(f"Shape creation took {time_interval} ms")
	print(f"Time/shape_count {time_interval/shape_count} ms")
	
"""

"""
# square = Shape(Shape_Type.SQUARE, 2)
	# rect = Shape(Shape_Type.RECTANGLE, [2,2])
	# circ = Shape(Shape_Type.CIRCLE, 2)
	
	square = make_square(2)
	rect = make_rectangle(2, 2)
	circ = make_circle(2)
	
"""
