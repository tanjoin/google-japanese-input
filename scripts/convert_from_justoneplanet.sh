which python > /dev/null 2>&1
if [ $? = 0 ]; then
  for file in `find kaomoji_justoneplanet -name "*.json"`; do
    python scripts/bin/convert_from_justoneplanet/convert_from_justoneplanet.py $file
  done
  echo "FINISH!!"
else
  echo "python : not found"
  echo "pythonが実行できる環境を作ってね"
fi