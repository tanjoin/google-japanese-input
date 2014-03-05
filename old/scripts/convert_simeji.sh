which python > /dev/null 2>&1
if [ $? = 0 ]; then
  for file in `find google_japanese_input -name "*.txt"`; do
    python scripts/bin/convert_simeji/convert_simeji.py $file
  done
  echo "FINISH!!"
else
  echo "python : not found"
  echo "pythonが実行できる環境を作ってね"
fi
