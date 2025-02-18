jlaselect [![](https://img.shields.io/badge/python-3.11+-blue.svg)](https://docs.python.org/3.11/) [![Maintainability](https://api.codeclimate.com/v1/badges/65ec5ac5f1152c705347/maintainability)](https://codeclimate.com/github/CALIL/jlaselect/maintainability)
=============================================================
日本図書館協会選定図書総目録CD-ROMのデータ変換ツール

概要
-----
- 日本図書館協会選定図書総目録のデータを使いやすい形に変換
- 抽出したデータはLine-delimited JSON形式で保存
- [図書選定事業](http://www.jla.or.jp/activities/sentei/tabid/207/Default.aspx)は2016年3月に終了しています

依存パッケージのインストール
----
```
poetry install
```

コマンドライン
----

- 各CD-ROM内の"JBISCS"ファイルをコピーする
- 複数ファイルをまとめて処理する場合は、プログラムを直接修正する

```bash
poetry run python jlaselect.py > jlaselect.jsonl
```

サンプルデータ
----
```json
{"year": 1999, "isbn": "426701535X"}
{"year": 1999, "isbn": "4121014995"}
{"year": 1999, "isbn": "4876386749"}
```

| 項目 | 型 | 概要 |
| ---- | ---- | ---- | 
| year | Number | 選定された西暦 |
| isbn | String | 正規化されたISBN（ISBN-10） |


処理済みデータのダウンロード
----

[jlaselect.jsonl](https://github.com/CALIL/jlaselect/raw/master/jlaselect.jsonl) 130,702件 (2019年8月21日公開)

- 処理に用いた元情報は以下の通りです

  | タイトル       | ISBN          | 期間                                          |
  |----------------|---------------|-----------------------------------------------|
  | 選定図書総目録59 | 9784820408109 | 2003年1月～2007年12月                         |
  | 選定図書総目録64 | 9784820413103 | 2008年1月～2012年12月                         |
  | 選定図書総目録67 | 9784820416043 | 2011年1月～2016年3月<br>1996年～2010年の児童図書 |

- 1996年～2016年3月の20年間のデータを統合していますが、全データの範囲は2003年1月～2016年3月となります
- 過去に発行されたCD-ROMに含まれてるデータのうち、選定図書目録58に収録されている2002年1月～2002年12月分が含まれていません（入手困難であったため）
- ISBNの付与されていない選定図書は除外されています
- yearが0となっているデータが一部あります
- このデータは「単なる事実」の集合であり著作権の対象外です
