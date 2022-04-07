"""
Copyright © 2022 Armağan Salman

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


from typing import Any


class Either:    
    LEFT_TYPE_INDICATOR = 0
    RIGHT_TYPE_INDICATOR = 1
    
    @staticmethod
    def create_either(value_arg: Any, left_or_right: int):
        # if left_or_right == 0 -->> returns an Either.Left with a value 
        # of given value.
        # else, returns an Either.Right with a value of given value.
        
        assert(Either.LEFT_TYPE_INDICATOR != Either.RIGHT_TYPE_INDICATOR)
        
        container = None
        
        if left_or_right == Either.LEFT_TYPE_INDICATOR:
            container = (Either.LEFT_TYPE_INDICATOR, value_arg)
        #
        elif left_or_right == Either.RIGHT_TYPE_INDICATOR:
            container = (Either.RIGHT_TYPE_INDICATOR, value_arg)
        #
        else:
            raise Error("Invalid selector value used in creation.")
        #
        
        
        class InnerEither:
            
            @staticmethod
            def is_left():
                return container[0] == Either.LEFT_TYPE_INDICATOR
            ###
            
            @staticmethod
            def is_right():
                return container[0] == Either.RIGHT_TYPE_INDICATOR
            ###
            
            @staticmethod
            def get_left_or(alternative: Any):
                if InnerEither.is_left():
                    return container[1]
                #
                else:
                    return alternative
                #
            ###
            
            @staticmethod
            def get_right_or(alternative: Any):
                if InnerEither.is_right():
                    return container[1]
                #
                else:
                    return alternative
                #
            ###
            
        ### End: class InnerEither
        
        
        return InnerEither()  
    ### End: create_either
    
    @staticmethod
    def left(value):
        return Either.create_either(value, Either.LEFT_TYPE_INDICATOR)
    ###
    
    @staticmethod
    def right(value):
        return Either.create_either(value, Either.RIGHT_TYPE_INDICATOR)
    ###
    
### End: class Either


if __name__ == "__main__":
    eit_l = Either.left("left value")
    eit_r = Either.right("right value")

    print(eit_l.is_left())
    print(eit_l.get_left_or(555))
    print(eit_r.get_left_or(555))

    print(eit_r.is_left())
    print(eit_r.is_right())
    print(eit_r.get_left_or(777))
    print(eit_l.get_left_or(777))

    print(eit_l)
#
