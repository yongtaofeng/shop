#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

import re
# print(re.findall("^[012]","1982asasa"))
#
# print(re.findall("er\B",'verb'))
# print(re.search("hello", "world hello python hello"))
# print(re.match("hello", "hello python").group())
src="c|linux|shell|python"
# print(re.search("([a-zA-Z]+\|){3}",src).group())

#print(re.search("([a-zA-Z]+\|)([a-zA-Z]+\|)([a-zA-Z]+\|)",src))
print(re.sub('([a-zA-Z]+\|)([a-zA-Z]+\|)([a-zA-Z]+\|)',r"\3\2\1",src))
