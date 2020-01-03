# download-testcase-tool

## 機能

- AtCoderコンテスト用のディレクトリを自動生成する

- AtCoderのテストケースを自動でダウンロードする

## インストール

[online-judge-tools](https://github.com/kmyk/online-judge-tools/blob/master)を導入

各種パッケージを導入

```sh
pip3 install colorama
pip install beautifulsoup4
```

このリポジトリをクローン

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
