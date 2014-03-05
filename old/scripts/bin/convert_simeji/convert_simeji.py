#!/usr/bin/env python
# coding:utf-8

import sys

argv = sys.argv
argc = len(argv)

if (argc != 2):
  print u'引数はファイル名１つにして下さい'
  quit()

jajp_value = []
jajp_key = []
f = open(argv[1], 'r')
line = f.readline() # 1行読み込む
while line:
  divideLine = line.split("	")
  jajp_key.append(divideLine[0])
  jajp_value.append(divideLine[1])
  line = f.readline()
f.close
result = "{\"EN_KEY\":[],\"EN_VALUE\":[],\"JAJP_VALUE\":["
# jajp_value 一覧
jajp_value_first = 0
for x in jajp_value:
  if jajp_value_first == 0:
    jajp_value_first = 1
    result += "\"" + x + "\"";
  else:
    result += ",\"" + x + "\"";
    
result += "],\"JAJP_KEY\":["
# jajp_key 一覧
jajp_key_first = 0
for x in jajp_key:
  if jajp_key_first == 0:
    jajp_key_first = 1
    result += "\"" + x + "\"";
  else:
    result += ",\"" + x + "\"";

result += "]}"

splitfilename = argv[1].split('/');
f = open('simeji/' + splitfilename[-1], 'w')
f.write(result)
f.close()