#!/usr/bin/env python
# coding:utf-8

import sys

argv = sys.argv
argc = len(argv)

if (argc != 3):
  print u'引数は、1が元ファイル、2が実際にGoogle日本語入力で読み込めた辞書のエクスポートにしてください'
  quit()

f1 = open(argv[1], 'r')
f2 = open(argv[2], 'r')

yomitango = []

# 実際にGoogle日本語入力で読み込めた辞書のエクスポートのよみと単語を配列にぶち込む
line2 = f2.readline()
counter = 1
while line2:
  divideLine = line2.split("	") # タブで分割
  # サイズ ------------------------------
  if len(divideLine) != 4 :
    print(u"line : " + str(counter) + u" 実際にGoogle日本語入力で読み込めた辞書のエクスポートが異常です " + str(len(divideLine)) + u"個")
  # よみ --------------------------------
  # 単語 --------------------------------
  yomitango.append(divideLine[0] + divideLine[1])
  line2 = f2.readline()
  counter = counter + 1
f2.close

# 元ファイルと比較する
line1 = f1.readline()
counter = 1
while line1:
  divideLine = line1.split("	") # タブで分割
  # サイズ ------------------------------
  if len(divideLine) != 4 :
    print(u"元ファイルが異常な形式と判明したため処理を中止します")
    quit()
  # よみ --------------------------------
  # 単語 --------------------------------
  if (divideLine[0] + divideLine[1] in yomitango) == False :
    print(u"line " + str(counter) + u" : 見つかりませんでした( ◞‸◟)☞" + divideLine[0].decode("utf-8") + " " + divideLine[1].decode("utf-8"))
  line1 = f1.readline()
  counter = counter + 1
f1.close
