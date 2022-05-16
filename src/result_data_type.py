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

from either_data_type import Either

class Result:
    """
    Error type
    Success type
    """
    
    def __init__(self, arg, type_id):
        self.either = None
        
        if type_id == "error":
            self.either = Either.left(arg)
        #
        else:
            self.either = Either.right(arg)
        #
        assert(self.either != None)
    ###
    
    @staticmethod
    def error(arg):
        return Result(arg, "error")
    ###
    
    @staticmethod
    def success(arg):
        return Result(arg, "success")
    ###
    
    def is_error(self):
        return self.either.is_left()
    ###
    
    def is_success(self):
        return self.either.is_right()
    ###
    
    def get_error(self):
        if self.either.is_left():
            return self.either.get_left_or()
        #
        return Result.error("Can't get Error data from Success type.")
    ###
    
    def get_success(self):
        if self.either.is_right():
            return self.either.get_right_or()
        #
        return Result.error("Can't get Success data from Error type.")
    ###

### End: class Result


def test_error():
    orig_err_data = "Cannot compute."
    err_res = Result.error(orig_err_data)
    
    assert(err_res.is_error())
    assert(not err_res.is_success())
    
    err_data = err_res.get_error()
    
    assert(orig_err_data == err_data)
    
    wrong_op_res = err_res.get_success()
    
    assert(wrong_op_res.is_error())
    
    assert(wrong_op_res.get_error() == "Can't get Success data from Error type.")
###

def test_success():
    orig_scss_data = "Computation successful."
    scss_res = Result.success(orig_scss_data)
    
    assert(not scss_res.is_error())
    assert(scss_res.is_success())
    
    scss_data = scss_res.get_success()
    
    assert(orig_scss_data == scss_data)
    
    wrong_op_res = scss_res.get_error()
    
    assert(wrong_op_res.is_error())
    
    assert(wrong_op_res.get_error() == "Can't get Error data from Success type.")
###

if __name__ == "__main__":
    test_funs = [test_error, test_success]
    
    for test in test_funs:
        test()
        print("Test '{}' passed.".format(test.__name__))
    #
    
    print(">> ALL TESTS PASSED.")
    
    err = Result.error( ["error value", 2, (3,4,7)] )
    print(err.get_error())
    print(err.get_success())
#
