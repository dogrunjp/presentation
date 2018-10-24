@title[Introduction]
# Jupyter notebookとNetworkX, PyGraphvizでSRAオブジェクトの構成図を自動的に描画する

### 2018/10/25 PGX ユーザー勉強会 #10

### @oec14



---
## SRAとは

- DRAは次世代シーケンサーからの出力データのためのデータベースです！
- DRAに登録されたデータは（基本的に）NCBI SRAとEBI ERAと国際協力の元に3極でミラーリングされている。
- SRAのメタデータには、シークエンスデータがどのように得られたか記載されている。
- メタデータは、Submission、BioProject、BioSample、Experiment、Run、Analysisの各オブジェクトで構成されている。
- 各オブジェクトはXMLスキーマで定義され、相互に関連づけられる。

[DDBJ Sequence Read Archive Handbook: https://www.ddbj.nig.ac.jp/dra/submission.html](https://www.ddbj.nig.ac.jp/dra/submission.html)

---
## SRAオブジェクトのデータモデル

#### ![データモデル](https://github.com/dogrunjp/presentation/blob/master/images/sra_object.png?raw=true)
[DDBJ Sequence Read Archive Handbook: https://www.ddbj.nig.ac.jp/dra/submission.html](https://www.ddbj.nig.ac.jp/dra/submission.html)

---
### 一つのプロジェクトを構成するオブジェクトの全体のイメージが掴みにくい？？かも

自動的に先ほどの構成図のような何かが自動的に出力されると便利かも。

---
## SRAオブジェクトの構成図をグラフとして可視化してみた

1. NewworkXのDiGraph()でグラフを生成する
1. SRA_Accessionsからあるプロジェクトに関わるオブジェクトを検索し、node, edgeに変換して読み込む
1. （本当はここで正しいグラフデータ検索することが一番重要かも）
1. NetworkXでdraw_networkx()する
1. matplotlibで描いてみる

---

![networkxとmatplotlibでプロット](https://github.com/dogrunjp/presentation/blob/master/images/sra_kankei_networkx_sample.png?raw=true =250x250)


できればtreeなレイアウトにしたい
---
## NetworkXのグラフをPyGraphvizに変換してグラフを描いてみた

- Gv = nx.nx_agraph.to_agraph(Gx) でPyGraphvizのグラフに変換できる。
- dotレイアウトで階層的にグラフをレイアウトするらしい。
---
![PyGraphvizでプロット](https://github.com/dogrunjp/presentation/blob/master/images/sra_kankei_sample_gv_dot.png?raw=true)

