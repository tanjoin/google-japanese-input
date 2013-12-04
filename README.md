google-japanese-input
=====================

Google日本語入力のカスタム辞書です


Google日本語入力にインポートするだけで使えます

👏(・_・)ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ

## google_japanese_input
Google日本語入力用辞書群

- android_google_japanese_input_suggest_dictionary.txt - Android版Google日本語入力サジェスト辞書
- encyclopedia.txt - 300字の簡易辞書
- inmu_dictionary.txt - これもうわかんねぇな。
- kaomoji_dictionary.txt - 顔文字辞書
- mac_google_japanese_input_suggest_dictionary.txt
- seiyu_dictionary.txt - 声優語録
- sub_calture_dictionary.txt - サブカル専門用語等をまとめた辞書
- suretai_dictionary.txt - 2chのスレタイを集めた辞書

#### other
開発中の辞書

- tanjoin_google_japanese_input.txt - 個人的な趣味の詰まった辞書


## simeji
Simeji用辞書群

## scripts
実行可能なシェルスクリプト群 (pythonが実行可能な環境が必要)

- convert_simeji.sh

      ./scripts/convert_simeji.sh

- compare_dic_and_dic.sh

      ./scripts/compare_dic_and_dic.sh <比較元 file> <比較対象 file>

- check_google_japanese_input.sh

      ./scripts/check_google_japanese_input.sh

#### bin
pythonファイル郡

基本的にシェルスクリプトから呼び出します

- check_gji_dictionary - Google日本語入力の辞書として使えるかチェックスクリプト
- compare_dic_and_dic - 辞書同士を比較するスクリプト
- convert_simeji - Google日本語入力の辞書をSimejiの辞書に変換する

## README.md
このファイル