#!/usr/bin/env python
# coding:utf-8

import os
import sys
import re
import json

argv = sys.argv
argc = len(argv)

if (argc != 2):
  print u'引数はファイル名１つにして下さい'
  quit()

# 読み込み
f = open(argv[1], 'r')
data = json.load(f)
f.close()

result = ""
for word_model in data["favorite"]:
  result += "＠" + str(word_model["_id"]).encode('utf-8') + "\t"
  result += re.sub('\r\n|\r|\n','<br>',word_model["face"].encode('utf-8')) + "\t"
  result += "名詞" + "\t"
  result += word_model["tag"].encode('utf-8') + " みんなの顔文字辞典"
  result += "\n"
  result += "かおもじ" + "\t"
  result += re.sub('\r\n|\r|\n','<br>',word_model["face"].encode('utf-8')) + "\t"
  result += "顔文字" + "\t"
  result += word_model["tag"].encode('utf-8') + " みんなの顔文字辞典"
  result += "\n"
# 書き込み
splitfilename = argv[1].split('/')
f = open('google_japanese_input/converted_kaomoji_justoneplanet/' + splitfilename[-2].replace('.','_') + '_' + splitfilename[-1].replace('json','txt'), 'w')
f.write(result)
f.close()
