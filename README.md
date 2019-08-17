jlacd-conv [![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://docs.python.org/3.7/)
=============================================================
日本図書館協会選定図書総目録CD-ROMのデータ変換ツール

概要
-----
- 日本図書館協会選定図書総目録のデータを使いやすい形に変換
- 抽出したデータはLine-delimited JSON形式で保存

依存パッケージのインストール
----
```json
pipenv install
```

コマンドライン
----
```bash
pipenv run python jlacd-conv.py > jlacd.jsonl
```

処理済みデータのダウンロード
----
- 処理済みデータにはISBNおよび選定年が含まれます（書誌情報は含みません）
- ISBNの付与されていない選定図書は除外されています
- データは「単なる事実」であり、著作保護の対象外です
- 処理に用いた元情報は以下の通りです
