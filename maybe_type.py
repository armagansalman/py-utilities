"""

BSD 3-Clause License

Copyright (c) 2022, Armağan Salman
All rights reserved.

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

