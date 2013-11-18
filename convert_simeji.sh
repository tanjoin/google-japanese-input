which python > /dev/null 2>&1
if [ $? = 0 ]; then
  echo "python : OK"
  python convert_simeji.py tanjoin_google_japanese_input.txt 
else
  echo "python : not found"
  echo "pythonが実行できる環境を作ってね"
fi
