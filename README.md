# BadAppleConverter
#### ※本プログラムは、Pythonとpipが導入されたWindows上での実行を想定しています。

## 概要
ターミナル上で任意の動画を任意の解像度で再生します。

## 使い方
1. まずpre.batを実行します。これで、BadAppleの動画(具体的には内部のURLの動画)がダウンロードされます。
2. 次に、make_BadApple.pyを実行します。内部のfix_height, fix_widthが、縦横のドット数に対応します。
3. 最後に、**フルスクリーンにしたコマンドプロンプトで**play_BadApple.pyを実行します。これでいけると思います。

## 参考記事
- BadApple!! を terminalで動かしてみた https://blog.shinonome.io/sh-badapple/
- Pythonで作ったコンソール上で動くライフゲーム https://qiita.com/y-tetsu/items/264d263717f933ad3cb2