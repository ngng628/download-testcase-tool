# download-testcase-tool

## 機能

- AtCoderコンテスト用のディレクトリを自動生成する

- AtCoderのテストケースを自動でダウンロードする

## インストール

[online-judge-tools](https://github.com/kmyk/online-judge-tools/blob/master)を導入

各種パッケージを導入

```sh
pip3 install colorama
pip3 install beautifulsoup4
```

このリポジトリをクローン（普段AtCoder用に使っているディレクトリ上推奨）

```sh
git clone https://github.com/ngng628/download-testcase-tool.git
```

パスなどの定数を書き換え

```start.py
# 27行目
# 絶対パスに書き換える
src = '~/download-testcase-tool/download.py'

# 46行目
# 自分のコンテスト用のライブラリがある絶対パスを指定
src = 'template.cpp'
```

## 使い方

## `start.py` と `download.py` を適切な場所に配置

## `python start.py {コンテストの名前}` でコンテスト用のディレクトリを作る

`{コンテストの名前}` ディレクトリが作成され、その中に `download.py` と 各問題用のディレクトリが生成されます。

コンテストの名前は `ABC051` や `AGC003` などが推奨されます

```txt
{contest-name}/
    ├ ─ A
    ├ ─ B
    ├ ─ C
    ├ ─ D
    └ ─ download.py
```

## `cd {コンテストの名前}` でコンテスト用のディレクトリに移動し、 `python downlowad.py`

問題にアクセスできる状態であれば、 `python download.py コンテストのURL` を実行することで問題を一括ダウンロードすることができます。

コンテストのURLとは `https://atcoder.jp/contests/abc000/tasks` など、 `tasks` のページ（「問題」のトップ） のことです。このスクリプトを実行するディレクトリの名前が `ABC000` や `AGC000` など、適切なものであればコンテストのURLは省略することができます。

各問題ディレクトリに `test/` が配置されます。

## `cd A` などで問題ディレクトリに移動。 `main.cpp` を編集して問題を解く

問題を解き終えたら、コンパイルして `oj t` を実行しましょう。自動でテストケースがジャッジされます。

（Pythonで解いた場合は `oj t -c "python3 main.py"` などとしましょう）

## `oj s main.cpp` で提出

`oj s main.cpp` で提出も自動化できます。

ブラウザが開ける環境であれば、 自動で提出の結果確認用にブラウザが起動します。 （無効化したい場合は、 `oj s --no-oepn main.cpp` ）
