"""

MIT License

Copyright (c) 2022 Armağan Salman

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


#(
from type_aliases import *
# Additional type definitions:
t_StrData = t_Dict
t_StrPack = t_Tuple[t_Str, t_StrData]
t_StrPackList = t_List[t_StrPack]

t_PackCreator = t_Callable[[t_StrPack], t_StrPack] # Using a string and its 
    # data, creates a new string.
t_PackCreatorList = t_List[t_PackCreator]
#)


#(
def test(pack: t_StrPack) -> t_StrPack:
    strg, data = pack
    
    print(strg)
    print(data)
    
    return (strg[:-1], data) # remove 1 char from the end.
#)


#(
def omit_first_word(pack: t_StrPack) -> t_StrPack:
    chars, data = pack
    SEPARATOR = ' '
    
    chars = chars.lstrip() # remove whitespaces from left.
    parts = chars.split(SEPARATOR)
    
    first_word_omitted = SEPARATOR.join(parts[1:])
    
    return (first_word_omitted, data)
#)


#(
def transform_string(pack_arg: t_StrPack, CREATORS: t_PackCreatorList) \
                    -> t_StrPack:
    #
    pack = pack_arg
    
    for creator_func in CREATORS:
        pack = creator_func(pack)
    #
    
    return pack
#)


#(
def multiple_string_transform(packs: t_StrPackList, CREATORS: t_PackCreatorList) \
            -> t_StrPackList:
    #
    transformed_packs = map(lambda x: transform_string(x, CREATORS), packs)
    
    return list(transformed_packs)
#)


# TODO(armagan)__2022.05.16_20.28:
# ?Use reduce to reach string result?


#(
def try_1():
    pack: t_StrPack = (" 123 456,789", {})
    strg, data = omit_first_word(pack)
    print(strg)
###
#)


#(
def try_2():
    multi_packs: t_StrPackList = [ \
        (" 123 456,789 10 11 12-13  14", {}) \
        ,(" 123 456,789 10 11 12-13  14", {}) ]
    #
    creators: t_PackCreatorList = [omit_first_word, omit_first_word]
    res = multiple_string_transform(multi_packs, creators)
    print(res)
###
#)


# try_2()