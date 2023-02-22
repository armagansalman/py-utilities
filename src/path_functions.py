"""
BSD 3-Clause License

Copyright (c) 2022-2023, Armağan Salman

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


import os
import logging
import typing as Typ

import common_types as CT
#from user_types import *

# Type aliases:
class T:
#(
	Str = str
#)


def get_absolute_path(path: T.Str):
    """docstr"""
# (
    return os.path.abspath(path)
# )


def is_file(path: T.Str):
    """docstr"""
# (
    return os.path.isfile(path)
# )


def ignore_redundant_subdirs(dirs: CT.t_Iter[T.Str]):
    """ If a dir D_1 is a descendant of a dir D_2, don't include D_1 as
        it will be included with recursive search of D_2. 
        WARNING: If a given path is a file, it will also be ignored.
    """
# (
    dirs_tpl = tuple(dirs)

    abs_paths = list(map(get_absolute_path, filter(os.path.isdir, dirs_tpl)))

    if len(abs_paths) < 1:
        # (
        logging.error(
            f"Can't get directory paths from given dirs: {str(dirs_tpl)}")

        raise Exception(
            "Given paths are not directories. Check LOG_ file for details.")
    # )

    abs_paths.sort()

    prev = abs_paths[0]

    essential_dirs = []

    for ix in range(1, len(abs_paths)):
        # (
        current = abs_paths[ix]

        if current.startswith(prev):  # Current is a descendant, ignore.
            # (
            continue
        # )
        else:
            # (
            essential_dirs.append(prev)
            prev = current
        # )
    # )
    essential_dirs.append(prev)

    return essential_dirs
# )


def get_fpaths_recursively(PATH: T.Str):
    """docstr"""
# (
    rec_files: list = []
    # TODO(armaganslmn): ??? Error handling.
    #ap = os.path.abspath(PATH)

    ap = PATH
    if os.path.isfile(ap):
        # (
        rec_files.append(ap)
        return rec_files
    # )

    elif os.path.isdir(ap):
        # (
        for root, dirs, files in os.walk(ap):
            # (
            for name in files:
                # (
                p = os.path.join(root, name)
                rec_files.append(p)  # os.path.abspath(p)
            # )
        # )
    # )

    else:  # Link or something else. Ignore them.
        # (
        pass
    # )

    return rec_files
# )


def get_fpaths_from_path_iter(paths_iter: CT.t_List[T.Str]):
    """docstr"""
# (
    if type(paths_iter[0]) != T.Str or type(paths_iter[-1]) != T.Str:
        # (
        raise Exception("A list of T.Str must be given.")
    # )

    file_paths: list = []

    # Below line removed. Selection belongs to mdl_Traverser module.
    # unq_paths = set(map(lambda x: x.path_str , paths_iter))

    # TODO(armaganslmn): Handle if input is file.
    # TODO(armaganslmn): ??? Error handling.

    #path_strings = map(lambda x: x.path_str , paths_iter)
    path_strings = paths_iter

    for string in path_strings:
        # (
        file_paths.extend(get_fpaths_recursively(string))
    # )

    return file_paths
# )


def test_ignore_redundant_subdirs_1():
    """docstr"""
# (
    dirs = ["/home/genel/Desktop/TEMP/", "!abc", "/home/genel/Desktop/", "/home/genel/Desktop/TEMP/git-local/",
            "/home/genel/Documents/", "/home/genel/Documents/Programs/", "/home/genel/Documents/Programs/eclipse/"]
    #
    # WARNING: os.path.abspath removes leading / from path. Important for
    # path string comparisons.
    essential_dirs = ["/home/genel/Desktop", "/home/genel/Documents"]

    calc_essential_dirs = ignore_redundant_subdirs(dirs)

    s1 = set(essential_dirs)
    s2 = set(calc_essential_dirs)

    assert (s1.difference(s2) == set())

    print(f"Passed | test_ignore_redundant_subdirs_1 | {__name__}")
# )


if __name__ == "__main__":
    """docstr"""
# (
    # main_1(dict())

    test_ignore_redundant_subdirs_1()
# )
