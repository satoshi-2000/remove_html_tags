# Remove HTML tags
本プログラムは、あるディレクトリに含まれるファイルについて、globによってパスを取得し、各ファイルに含まれるHTMLタグを除去するものである。

# Remove Nan rows
pandasのisnull()メソッドを用いることで、Nanが含まれている行を抽出する。
本プログラムでは、Nanが含まれていない行を取り出すため、isnull()メソッドで抽出した行に対して、論理値を反転し、ブールインデックス参照で抽出を行っている。

# Memo
HTMLタグの検出については、python標準ライブラリに含まれるreのcomplileメソッド及びsubメソッドを用いている。

# Reference
[1] re
https://docs.python.org/ja/3/library/re.html
[2] [Python]文字列内のhtmlタグを除去する
https://yyuuiikk.org/entry/703
[3] pandasで欠損値NaNを含む行・列を抽出
https://note.nkmk.me/python-pandas-nan-extract/
[4] pandas.isnull
https://pandas.pydata.org/docs/reference/api/pandas.isnull.html
