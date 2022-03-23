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


class DataBoxV2():
    #
    
    class ExtractFromEmpty(Exception):
        pass
    #
    
    """
    def __init__(self):
        # Create empty DataBox
        self.call_func = DataBoxV2.create_accessors(data=None, make_empty=True)
    #
    """
    
    """
    def __init__(self, data):
        # Create DataBox full with data
        self.call_func = DataBoxV2.create_accessors(data, make_empty=False)
    #
    """
    
    def __init__(self, data: Any, fill_choice: str):
        if fill_choice == "empty":
            self.call_func = DataBoxV2.create_accessors(data=None, make_empty=True)
        #
        elif fill_choice == "fill":
            self.call_func = DataBoxV2.create_accessors(data, make_empty=False)
        #
        else:
            self.call_func = DataBoxV2.create_accessors(data, make_empty=False)
        #
    #
    
    @staticmethod
    def create_accessors(data: Any, make_empty):
        def spawner():
            empty_val = None
            full_val = True
            
            vessel = tuple()
            
            if make_empty:
                vessel = (empty_val, empty_val)
            #
            else:
                vessel = (full_val, data)
            #
            
            def is_empty():
                assert(empty_val != full_val)
                return vessel[0] == empty_val
            #
            
            def is_full():
                return not is_empty()
            #
            
            def get_data():
                if is_full():
                    return vessel[1]
                #
                else:
                    raise DataBoxV2.ExtractFromEmpty("Given DataBox argument is empty.")
                #
            #
            
            """
            def overwrite_data(arg):
                vessel[1] = arg
            #
            """
            
            fun_collection = dict()
            fun_collection["is_empty"] = is_empty
            fun_collection["is_full"] = is_full
            fun_collection["get_data"] = get_data
            
            #fun_collection["overwrite_data"] = overwrite_data
            
            def func_accessor(func_name: str):
                func = fun_collection[func_name]
                return func()
            #
            
            return func_accessor
        # spawner
        
        return spawner() # Call to create accessor function.
    # __init__
    
    def is_empty(self):
        res = self.call_func("is_empty")
        return res
    #
    
    def is_full(self):
        res = self.call_func("is_full")
        return res
    #
    
    """
    def overwrite_data(self, data):
        func = self.call_func("overwrite_data")
        func(data) # overwrite vessel data
    #
    """
    
    """
    def put_data(self, data):
        # Alias.
        self.overwrite_data(data)
    #
    """
    
    def get_data(self):
        res = self.call_func("get_data")
        return res
    #
    
    @staticmethod
    def empty_box():
        return DataBoxV2(0, "empty")
    #
    
    @staticmethod
    def full_box(data):
        return DataBoxV2(data, "fill")
    #
# DataBoxV2


if __name__ == "__main__":
    import sys
    
    def DataBox_divide(nom, denom) -> DataBoxV2:
        if denom == 0:
            #return DataBoxV2(0, "empty") # Make  an empty DataBox.
            return DataBoxV2.empty_box()
        #
        else:
            #return DataBoxV2(nom/denom, "fill") # Make a filled DataBox.
            return DataBoxV2.full_box(nom/denom) # Make a filled DataBox.
        #
    #
    
    box1 = DataBox_divide(12, 5)
    
    print("++++++++++++++++")
    print(box1)
    print(sys.getsizeof(box1))
    print("box1 is_empty:", box1.is_empty())
    print(box1.is_full())
    print(box1.get_data())
    
    
    box2 = DataBox_divide(12, 0)
    
    print("++++++++++++++++")
    print(box2)
    print(sys.getsizeof(box2))
    print("box2 is_empty:", box2.is_empty())
    print(box2.is_full())
    print(box2.get_data())
# if main
    
    