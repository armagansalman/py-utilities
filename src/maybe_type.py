"""
Copyright © 2022 Armağan Salman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""



from typing import Any
from typing import Tuple

Maybe_t = Tuple

class Maybe():
    # Custom implementation of maybe type.

    class ExtractFromNothing(Exception):
        pass

    @staticmethod
    def nothing_specifier():
        nothing_spec = None
        return nothing_spec
        #
    #

    @staticmethod
    def some_specifier():
        some_spec = True
        
        assert(some_spec != Maybe.nothing_specifier()) # Specifiers must be unique.
        
        return some_spec
        #
    #

    @staticmethod
    def make_some(data: Any) -> Tuple:
        return (Maybe.some_specifier(), data)
    #

    @staticmethod
    def make_nothing() -> Tuple:
        return (Maybe.nothing_specifier(), False) # Second field is unimportant
    #

    @staticmethod
    def is_some(arg: Tuple) -> bool:
        return arg[0] == Maybe.some_specifier()
    #

    @staticmethod
    def is_nothing(arg: Tuple) -> bool:
        return arg[0]  == Maybe.nothing_specifier()
    #

    @staticmethod
    def get_data(arg: Tuple) -> Any:
        if Maybe.is_nothing(arg):
            raise Maybe.ExtractFromNothing("Maybe argument is nothing.")
        #
        return arg[1]
    #
###

if __name__ == "__main__":
    def maybe_divide(nom, denom) -> Maybe_t:
        if denom == 0:
            return Maybe.make_nothing()
        #
        else:
            return Maybe.make_some(nom/denom)
    #
    
    may1 = maybe_divide(12, 5)
    
    if Maybe.is_some(may1):
        print("First maybe data is valid.")
        print("Its value = {}\n".format(Maybe.get_data(may1)))
    #
    
    may2 = maybe_divide(12, 0)
    
    
    if Maybe.is_nothing(may2):
        print("Second maybe data is invalid. Can't access the value.")
        pass # Or handle accordingly.
    #
    
    print("If you try to get data from nothing, this exception is raised: ")
    print(">>> ")
    print(Maybe.get_data(may2)) # Raises an exception when may2 is nothing.
#

