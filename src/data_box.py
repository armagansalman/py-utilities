"""
Copyright © 2022 Armağan Salman

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
THE SOFTWARE.
"""


"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    > WHY
    To be able to properly represent undefined data.
    
"""


from typing import Any


    
class ExtractFromUndefined(Exception):
    pass
#


class DataBox():
    #

    def __init__(self, data: Any, fill_choice: str):
        if fill_choice == "undefined":
            self.call_func = DataBox.create_accessors(data=None, make_undefined=True)
        #
        elif fill_choice == "fill":
            self.call_func = DataBox.create_accessors(data, make_undefined=False)
        #
        else:
            self.call_func = DataBox.create_accessors(data, make_undefined=False)
        #
    #
    
    @staticmethod
    def create_accessors(data: Any, make_undefined):
        def box_spawner():
            undefined_val = None
            full_val = True
            
            vessel = tuple()
            
            if make_undefined:
                vessel = (undefined_val, undefined_val)
            #
            else:
                vessel = (full_val, data)
            #
            
            def is_undefined():
                assert(undefined_val != full_val)
                return vessel[0] == undefined_val
            #
            
            def is_full():
                return not is_undefined()
            #
            
            def peek():
                if is_full():
                    return vessel[1]
                #
                else:
                    raise DataBox.ExtractFromUndefined("Given DataBox argument is undefined.")
                #
            #
            
            fun_collection = dict()
            fun_collection["is_undefined"] = is_undefined
            fun_collection["is_full"] = is_full
            fun_collection["peek"] = peek
            
            def func_accessor(func_name: str):
                func = fun_collection[func_name]
                return func()
            #
            
            return func_accessor
        # box_spawner
        
        return box_spawner() # Call to create accessor function.
    # __init__
    
    def is_undefined(self):
        res = self.call_func("is_undefined")
        return res
    #
    
    def is_full(self):
        res = self.call_func("is_full")
        return res
    #

    def peek(self):
        res = self.call_func("peek")
        return res
    #
    
    @staticmethod
    def undefined_box():
        return DataBox(0, "undefined")
    #
    
    @staticmethod
    def box(data):
        return DataBox(data, "fill")
    #
    
# DataBox class


if __name__ == "__main__":
    import sys
    
    def DataBox_divide(nom, denom) -> DataBox:
        if denom == 0:
            return DataBox.undefined_box()
        #
        else:
            return DataBox.box(nom/denom) # Make a filled DataBox.
        #
    #
    
    box1 = DataBox_divide(12, 5)
    
    print("++++++++++++++++")
    print(box1)
    print(sys.getsizeof(box1))
    print("box1 is_undefined:", box1.is_undefined())
    print(box1.is_full())
    print(box1.peek())
    
    
    box2 = DataBox_divide(12, 0)
    
    print("++++++++++++++++")
    print(box2)
    print(sys.getsizeof(box2))
    print("box2 is_undefined:", box2.is_undefined())
    print(box2.is_full())
    print(box2.peek())
# if main


"""
def create_const(const):
    a = copy.deepcopy(const)
    def read():
        return copy.deepcopy(a)
    #
    return read
#

const_val = create_const(1234)
const_val() # reads const val
"""
