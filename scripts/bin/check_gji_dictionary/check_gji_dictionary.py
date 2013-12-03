#!/usr/bin/env python
# coding:utf-8

import sys
import re

argv = sys.argv
argc = len(argv)

if (argc != 2):
  print u'引数はファイル名１つにして下さい'
  quit()

# よみ (ひらがなとその他記号のチェックをする予定だが記号はよくわからないので未定よってWarningのみ)
regexpYomi = re.compile(r'^(?:\xE3\x81[\x81-\xBF]|\xE3\x82[\x80-\x93]|ー)+$')
# 単語 (半角英数字だけだとサジェストしてくれないのでWarning表示)
regexpTango = re.compile(r'^[0-9A-Za-z]$')
# 品詞 (特定の選択肢でなければならない)
arrayHinshi = [u"名詞", u"短縮よみ", u"サジェストのみ", u"固有名詞",u"人名", u"姓", u"名", u"組織", u"地名", u"名詞サ変",
               u"名詞形動", u"数", u"アルファベット", u"記号", u"顔文字", u"副詞", u"連体詞", u"接続詞", u"感動詞", u"接頭語", 
               u"助数詞", u"接尾一般", u"接尾人名", u"接尾地名", u"動詞ワ行五段", u"動詞カ行五段", u"動詞サ行五段", u"動詞タ行五段",
               u"動詞ナ行五段", u"動詞マ行五段", u"動詞ラ行五段", u"動詞ガ行五段", u"動詞バ行五段", u"動詞ハ行四段", u"動詞一般",
               u"動詞カ変", u"動詞サ変", u"動詞ザ変", u"動詞ラ変", u"形容詞", u"終助詞", u"句読点", u"独立語", u"抑制単語"];

f = open(argv[1], 'r')

line = f.readline() # 1行読み込む
counter = 1
while line:
  divideLine = line.split("	") # タブで分割
  # サイズ ------------------------------
  if len(divideLine) != 4 :
    print(u"Error : " + str(counter) + u"line : " + u"必要な要素が不足しています")
    line = f.readline()
    counter = counter + 1
    continue
  # よみ --------------------------------
  if len(divideLine[0]) > 300 :
    print(u"Error : " + str(counter) + u"line : " + u"よみが長いです(" + str(len(divideLine[0]))  + u")")
  result = regexpYomi.search(divideLine[0])
  if result == None : # すべてがひらがなではなかったとき
    print(u"Warning : " + str(counter) + u"line : " + divideLine[0].decode("utf-8") + u" ひらがな以外が含まれています")
  # 単語 --------------------------------
  if len(divideLine[1]) > 300:
      print(u"Error : " + str(counter) + u"line : " + u"単語が長いです(" + str(len(divideLine[1])) + u")")
  # 品詞 --------------------------------
  if (divideLine[2].decode("utf-8") in arrayHinshi) == False  :
      print(u"Error : " + str(counter) + u"line :  " + divideLine[2].decode("utf-8")  + " : " + u"品詞が不正です")
      line = f.readline()
      counter = counter + 1
      continue
  # コメント ----------------------------
  if len(divideLine[3]) > 300:
      print(u"Error : " + str(counter) + u"line : " + u"コメントが長いです(" + str(len(divideLine[3])) + u")")
  line = f.readline()
  counter = counter + 1
f.close
