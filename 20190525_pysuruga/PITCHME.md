@title[Introduction]
## Pythonで作る生命科学データ関連Webサービス

### 2019/5/25 [Python駿河 勉強会 #1](https://py-suruga.connpass.com/event/127869/)

### dogrun Inc. オーイシ

---
## 発表者の紹介

- 名前：オーイシ
- 肩書：静岡市のある会社（従業員一人）代表
- 仕事：データ可視化業（生命科学研究に関わるデータベース関連サービスの構築も）

---
## Pythonを使った事例の紹介

---
## AOE
### [https://aoe.dbcls.jp](https://aoe.dbcls.jp)

公共データベースに登録された遺伝子発現データについて、検索・閲覧・比較するこのとできる目次サービス。

<center><a href="https://aoe.dbcls.jp"><img src="https://github.com/dogrunjp/presentation/blob/master/images/20190525_pysuruga_aoe.png?raw=true" width=750></a></center>

---
## AOEのPythonなところ

- 遺伝子発現データの可視化（データベースの探索的な可視化）が特徴のサービス
- APIはPythonで構築
- 可視化しているデータの統計値をデータ更新時にPythonで計算

---
## 統合TV

### [https://togotv.dbcls.jp/](https://togotv.dbcls.jp/)

データベースやウェブツールの使い方を動画で解説するサービス

<center><a href="https://togotv.dbcls.jp/"><img src="https://github.com/dogrunjp/presentation/blob/master/images/20190525_pysuruga_togotv.png?raw=true" width=750></a></center>


---
統合TVに興味のある方、サイトとリンクしたこちらの書籍もご参考にしていただけると思います

[「生命科学データベース・ウェブツール 図解と動画で使い方がわかる! 研究がはかどる定番18選」](https://www.amazon.co.jp/生命科学データベース・ウェブツール-図解と動画で使い方がわかる-研究がはかどる定番18選-坊農秀雅/dp/4815701431)
---
## 統合TVのPythonなところ

- コンテンツのソースはGoogleドライブやYoutubeで管理している
- Pythonの静的サイトジェネレータを使ってサイトを構築している

---
## 新着論文レビュー　[https://first.lifesciencedb.jp/](https://first.lifesciencedb.jp/)

日本人の著者による生命科学分野の論文の著者本人による日本語レビュー

<center><a href="https://first.lifesciencedb.jp/"><img src="https://github.com/dogrunjp/presentation/blob/master/images/20190525_pysuruga_fa.png?raw=true" width=750></a></center>


---
## 新着論文レビューのPythonなところ

- Pythonの静的サイトジェネレータで構築
- コンテンツ内の生命科学用語の自動アノテーション機能のバックエンド

---
## DBCLS SRA [https://first.lifesciencedb.jp/](https://first.lifesciencedb.jp/)

公共データベースに登録された次世代シーケンサー（NGS）の塩基配列データを、
様々な属性情報から検索しデータ取得できるサイト

<center><a href="http://sra.dbcls.jp/"><img src="https://github.com/dogrunjp/presentation/blob/master/images/20190525_pysuruga_ddbjsearch.png?raw=true" width=750></a></center>

---
## DBCLS SRAのPythonなところ

- 日々更新されるデータを収集しElasticsearchに保存する自動処理
- 検索API構築

---
## Pythonの利用用途

<center><img src="https://github.com/dogrunjp/presentation/blob/master/images/20190525_pysuruga_service_aim.png?raw=true" width=800></center>


---
## PythonをWebサービス開発者とデザイナーに推す理由

- より深くデータと連携したシステムとデザインがサービスに要求されるようになる（かもしれない）。
- そんなニーズが予想される中、Pythonは幅広くデータに関わる要求に対応できる言語である（かもしれない）。

---
## PythonをWebサービス開発者＆デザイナーに推す理由（追加）

- 実際はPythonだけでは完結しないことが多い（JavaScript, Julia、RやDBのクエリなど）。
- 何かの言語の仕様を一通り目を通しておくとオレオレ実装をしなくて済むことがある。
- Pythonは学習コストが低い（と言われている）ので一人で開発言語を学習するには良いと思う。

---
データ関連のWebサービスの開発には、
データの分析、エンジニアリング、可視化、対象となる分野の専門知識（ドメイン知識などと言われる）など
統合的な知見が必要。色々な経験をもったIT関係者がデータに歩み寄って、
データ関連のサービス開発に踏み入れてくれたら良いと思っています。

---

### 来月、静岡市でエンジニア向け生命科学データ解析のイベント開催します

<center><a href="https://shizuoka-ngs.connpass.com/event/128816/"><img src="https://github.com/dogrunjp/presentation/blob/master/images/shizuokangs_2_ad.png?raw=true" width=750></a></center>
