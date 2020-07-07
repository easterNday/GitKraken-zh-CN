#!/usr/bin/python 
# -*- coding: utf-8 -*-

import json
import pprint
import zhconv
import codecs
import sys

class Translation():
    def read_json(self):
        return json.load(codecs.open(sys.argv[1],'r',encoding="utf-8"))

t = Translation()
dict = t.read_json()
#pprint.pprint(dict)

dict["languageOption"]["label"] ="简体中文"
dict["languageOption"]["value"] = 'zh-CN'

menuStrings = dict["menuStrings"]

for key,value in menuStrings.items():
    menuStrings[key] = zhconv.convert(value, 'zh-cn')
    
strings = dict["strings"]

for key,value in strings.items():
    strings[key] = zhconv.convert(value, 'zh-cn')
    
output = json.dumps(dict, indent=2, ensure_ascii=False)

f = codecs.open("./strings.json", "w", encoding="utf8")
f.write(output)

