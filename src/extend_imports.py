"""
Copyright © 2022 Armağan Salman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import sys
import copy

#from typing import Iterable as Iter
from typing import List


def extend_import_paths(directory_paths: List[str]):
    # Input can be relative. "../tests" etc. Adds given paths to import search variable. Returns original paths.
    
    assert(type(directory_paths) == list) # must be list of str
    
    isdir = os.path.isdir
    abspath = os.path.abspath
    
    abs_paths = map(lambda x: abspath(x), directory_paths)
        
    # Find new paths using sets:
    orig_paths = copy.deepcopy(sys.path)
    
    sys_paths: Set[str] = set(sys.path)
    abs_set: Set[str] = set(abs_paths)
    
    news = abs_set.difference(sys_paths)
    
    for p in news:
        if isdir(p):
            sys.path.append(p)
        #
    #
    #sys.path.extend(list(news))  # Update import search locations.
    
    #print("New paths: ", '\n'.join(list(news)))
    #print("<<<<<<< END New paths")
    return orig_paths
#


#sys.path.append(os.path.dirname(os.path.realpath(__file__)))
#sys.path.append(r"D:\Documents\temp\ExamplePythonProject\source\Project")

"""
paths_to_add = ["..", "../Project", "../Project", "..\Project\SubDir1\SubDir2" \
            , "..\Project\SubDir1", "19"
]

extend_import_paths( paths_to_add )
"""


if __name__ == "__main__":
    dir_paths = ["../sibling-dir"]
    extend_import_paths(dir_paths)
    
    import test_extend_imports
    print("Successfully added", str(dir_paths), "to sys import path list.")
#