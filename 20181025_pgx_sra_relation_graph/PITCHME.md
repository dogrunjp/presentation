@title[Introduction]
# Jupyter notebookとNetworkX, PyGraphvizでSRAオブジェクトの構成図を自動的に描画する

### 2018/10/25 PGX ユーザー勉強会 #10

### @oec14



---
## SRAとは

- DRAは次世代シーケンサーからの出力データのためのデータベース。
- SRAのメタデータには、シークエンスデータがどのように得られたか記載されている。
- メタデータは、Submission、BioProject、BioSample、Experiment、Run、Analysisの各オブジェクトで構成され、各オブジェクトは相互に関連づけられる。

[DDBJ Sequence Read Archive Handbook: https://www.ddbj.nig.ac.jp/dra/submission.html](https://www.ddbj.nig.ac.jp/dra/submission.html)

---
## SRAオブジェクトのデータモデル

<center><img src="https://github.com/dogrunjp/presentation/blob/master/images/sra_object.png?raw=true" width=400></center>
[DDBJ Sequence Read Archive Handbook: https://www.ddbj.nig.ac.jp/dra/submission.html](https://www.ddbj.nig.ac.jp/dra/submission.html)

---
### 一つのプロジェクトを構成するオブジェクトの全体のイメージが掴みにくい？？


#### 自動的に先ほどの構成図のような何かが自動的に出力されると便利かも。

---
## SRAオブジェクトの構成図をグラフとして可視化してみた

1. SRA_Accessionsからあるプロジェクトに関わるオブジェクトを検索し、node, edgeに変換して読み込む
1. （ここで正しいグラフデータを生成することが一番重要かも）
1. NetworkXでdraw_networkx()する
1. matplotlibで描いてみる

---

<center><img src="https://github.com/dogrunjp/presentation/blob/master/images/sra_kankei_networkx_sample.png?raw=true" width=400></center>

### できればtreeなレイアウトにしたい

---
## NetworkXのグラフをPyGraphvizに変換してグラフを描いてみた

1. Gv = nx.nx_agraph.to_agraph(Gx) でPyGraphvizのグラフに変換できる。
1. dotレイアウトを指定すると階層的にグラフをレイアウトするらしい。

---
![PyGraphvizでプロット](https://github.com/dogrunjp/presentation/blob/master/images/sra_kankei_sample_gv_dot.png?raw=true)

