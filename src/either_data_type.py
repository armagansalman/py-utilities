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
    
    @staticmethod
    def create_either(value_arg: Any, left_or_right: str):
        # if left_or_right == "left" -->> returns an Either.Left with a value 
        # of given value.
        # else, returns an Right tagged type with a value of given value.
        
        LEFT_TYPE_INDICATOR = 0
        RIGHT_TYPE_INDICATOR = 1
        
        assert(LEFT_TYPE_INDICATOR != RIGHT_TYPE_INDICATOR)
        
        container = None
        
        if left_or_right == "left":
            container = (LEFT_TYPE_INDICATOR, value_arg)
        #
        elif left_or_right == "right":
            container = (RIGHT_TYPE_INDICATOR, value_arg)
        #
        else:
            raise Error("Invalid selector value used in creation.")
        #
        
        assert(container != None)
        
        class InnerEither:
            
            @staticmethod
            def is_left():
                return container[0] == LEFT_TYPE_INDICATOR
            ###
            
            @staticmethod
            def is_right():
                return container[0] == RIGHT_TYPE_INDICATOR
            ###
            
            @staticmethod
            def get_left_or(alternative: Any = None):
                if InnerEither.is_left():
                    return container[1]
                #
                else:
                    return alternative
                #
            ###
            
            @staticmethod
            def get_right_or(alternative: Any = None):
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
        return Either.create_either(value, "left")
    ###
    
    @staticmethod
    def right(value):
        return Either.create_either(value, "right")
    ###
    
### End: class Either

def test_left():
    orig_val = "left val"
    orig_alt_val = "alt"
    
    lf = Either.left(orig_val)
    
    assert(lf.is_left())
    assert(not lf.is_right())
    
    real_val = lf.get_left_or()
    alt_val = lf.get_right_or(orig_alt_val)
    
    assert(real_val == orig_val)
    assert(orig_alt_val == alt_val)
    
    # Get left's value when it's left type.
    assert(orig_val == lf.get_left_or("dummy"))
###

def test_right():
    orig_val = "right val"
    orig_alt_val = "alt"
    
    rht = Either.right(orig_val)
    
    assert(rht.is_right())
    assert(not rht.is_left())
    
    real_val = rht.get_right_or()
    alt_val = rht.get_left_or(orig_alt_val)
    
    assert(real_val == orig_val)
    assert(orig_alt_val == alt_val)
    
    # Get right's value when it's right type.
    assert(orig_val == rht.get_right_or("dummy"))
###


if __name__ == "__main__":
    
    test_funs = [test_left, test_right]
    
    for test in test_funs:
        test()
        print("Test '{}' passed.".format(test.__name__))
    #
    
    print("All tests passed.")
#
