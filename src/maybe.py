"""

    ~~~ WHY ~~~
To be able to represent nothing and separate it from something (usable values).

"""


"""
MIT License

Copyright (c) (2022) (Armağan Salman)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
#
#
from typing import (Any)
#
#
t_Any = Any
#
class Maybe:
#(
    class Nothing:
    #(
        _instance = None # Singleton instance.
        
        def __new__(cls, *args, **kwargs):
        #(
            if cls._instance is None: # Create instance only once.
            #(
                cls._instance = object.__new__(cls, *args, **kwargs)
            #)
            return cls._instance
        #)
        def is_nothing(self):
        #(
            return True
        #)
        def is_something(self):
        #(
            return False
        #)
        def get_data(self):
        #(
            raise TypeError(f"{type(self)} type does not hold data.")
        #)
    #)
    class Something:
    #(
        _data: t_Any
        
        def __init__(self, data: t_Any):
        #(
            self._data = data
        #)
        def is_nothing(self):
        #(
            return False
        #)
        def is_something(self):
        #(
            return True
        #)
        def get_data(self):
        #(
            return self._data
        #)
    #)
#)
#
#
def main():
#(
    data = "333"
    nt: Maybe = Maybe.Nothing()
    st: Maybe = Maybe.Something(data)
    
    print(nt)
    print(Maybe.Nothing())
    print(st)
    
    assert(nt.is_nothing() == True)
    assert(nt.is_something() == False)
    
    try:
    #(
        nt.get_data()
    #)
    except TypeError as Err:
    #(
        print(f"~[ INFO ]~ Caught expected error. ( Type: {type(Err)} ) ; ( Msg: {Err} )")
    #)
    
    assert(st.is_nothing() == False)
    assert(st.is_something() == True)
    
    x: int = st.get_data() # Mypy should report an error. st._data is str.
    assert(x == data)
    
    print(f"~[ INFO ]~ SUCCESS: All assertions passed for {__name__}.")
#)


if __name__ == "__main__":
#(
    main()
#)

