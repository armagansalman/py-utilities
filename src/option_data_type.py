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
    
### End> class Option

if __name__ == "__main__":
    some = Option.some("data")
    print(some.is_some())
    print(some.is_none())
    print(some.get_data())

    none = Option.none()

    print(none.is_some())
    print(none.is_none())
    print(none.get_data())
#
