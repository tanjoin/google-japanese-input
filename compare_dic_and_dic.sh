which python > /dev/null 2>&1
if [ $? = 0 ]; then
  if [ $# = 2 ]; then
    bin/compare_dic_and_dic/compare_dic_and_dic.py $1 $2
  else
	echo "引数が$#個です"
    echo "引数は、1が元ファイル、2が実際にGoogle日本語入力で読み込めた辞書のエクスポートにしてください"
  fi
else
  echo "python : not found"
  echo "pythonが実行できる環境を作ってね"
fi
