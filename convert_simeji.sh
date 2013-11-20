which python > /dev/null 2>&1
if [ $? = 0 ]; then
  python bin/convert_simeji.py tanjoin_google_japanese_input.txt 
  echo "FINISH!!"
else
  echo "python : not found"
  echo "pythonが実行できる環境を作ってね"
fi
