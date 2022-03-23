"""
Copyright © 2022 Armağan Salman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    > WHY
    To be able to safely return null data.
    
"""

from typing import Any
from typing import Tuple

DataBox_t = Tuple

class DataBox():
    # Custom implementation of Option type.

    class ExtractFromEmpty(Exception):
        pass
    #
    
    @staticmethod
    def empty_specifier():
        nothing_spec = None
        return nothing_spec
        #
    #

    @staticmethod
    def full_specifier():
        some_spec = True
        
        assert(some_spec != DataBox.empty_specifier()) # Specifiers must be unique.
        
        return some_spec
        #
    #

    @staticmethod
    def make_full(data: Any) -> Tuple:
        return (DataBox.full_specifier(), data)
    #

    @staticmethod
    def make_empty() -> Tuple:
        return (DataBox.empty_specifier(), False) # Second field is unimportant
    #

    @staticmethod
    def is_some(arg: Tuple) -> bool:
        return arg[0] == DataBox.full_specifier()
    #

    @staticmethod
    def is_empty(arg: Tuple) -> bool:
        return arg[0]  == DataBox.empty_specifier()
    #

    @staticmethod
    def get_data(arg: Tuple) -> Any:
        if DataBox.is_empty(arg):
            raise DataBox.ExtractFromEmpty("Given DataBox argument is empty.")
        #
        return arg[1]
    #
###

if __name__ == "__main__":
    def DataBox_divide(nom, denom) -> DataBox_t:
        if denom == 0:
            return DataBox.make_empty()
        #
        else:
            return DataBox.make_full(nom/denom)
    #
    
    may1 = DataBox_divide(12, 5)
    
    if DataBox.is_some(may1):
        print("First DataBox data is valid.")
        print("Its value = {}\n".format(DataBox.get_data(may1)))
    #
    
    may2 = DataBox_divide(12, 0)
    
    
    if DataBox.is_empty(may2):
        print("Second DataBox data is invalid. Can't access the value.")
        pass # Or handle accordingly.
    #
    
    print("If you try to get data from an empty DataBox, this exception is raised: ")
    print(">>> ")
    print(DataBox.get_data(may2)) # Raises an exception when may2 is empty.
#

