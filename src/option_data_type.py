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
        # of given value_arg.
        # else, returns an Right tagged type with a value of given value_arg.
        
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


class Option:
    """
    None type
    Some type
    """
    NONE_TYPE_ID = 0
    SOME_TYPE_ID = 1
    
    
    def __init__(self, tag_type, data):
        assert(Option.NONE_TYPE_ID != Option.SOME_TYPE_ID)
        
        if tag_type == Option.NONE_TYPE_ID:
            self.tagged_data = (Option.NONE_TYPE_ID,)
        #
        else:
            self.tagged_data = (Option.SOME_TYPE_ID, data)
    ###
    
    @staticmethod
    def none():
        # create None instance and return.
        return Option(Option.NONE_TYPE_ID, None)
    ###
    
    @staticmethod
    def some(data):
        # create Some instance and return.
        return Option(Option.SOME_TYPE_ID, data)
    ###
    
    def is_none(self):
        return self.tagged_data[0] == Option.NONE_TYPE_ID
    ###
    
    def is_some(self):
        return self.tagged_data[0] == Option.SOME_TYPE_ID
    ###
    
    def get_data(self):
        if self.tagged_data[0] == Option.SOME_TYPE_ID:
            return self.tagged_data[1]
        #
        else:
            # TODO(armagan): Use Result type and return Error.
            # Don't raise exception.
            raise Exception("Can't get data from a Option.None")
        #
    ###
    
### End >> class Option
