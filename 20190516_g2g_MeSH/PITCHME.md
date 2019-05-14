@title[Introduction]
## G2GMLを利用したMeSH RDFのプロパティグラフへの変換

### 2019/5/16 PGX ユーザー勉強会 #12

### dogrun Inc. Oishi

---
## Medical Subject Headings (MeSH)とは

PUBmedなどNLMの生物医学系データベースをインデックスするための階層化された用語集

[Medical Subject Headings - Home](https://www.nlm.nih.gov/mesh/meshhome.html)

---
## MeSH Tree

- MeSHは16のカテゴリに分類される
- それぞれのカテゴリは最大13の専門性の詳細さによる階層構造を持つ
- MeSH descriptorは少なくとも一つの（概ね複数の）階層（Tree）構造のMeSHコードに紐付く

[MeSH Tree Structures](https://www.nlm.nih.gov/mesh/intro_trees.html)

---

RDFから変換したMeSHの階層構造とMeSH descriptorのデータから、
RDFからプロパティグラフへの変換ツールである
[G2G](https://g2gml.readthedocs.io/en/latest/contents/g2gml.html)を使いグラフデータを取得するというのが
今回の資料の趣旨

---
## MeSH RDFからプロパティグラフへの変換

MeSHデータは
- 各種フォーマットのファイル（ftp://nlmpubs.nlm.nih.gov/online/mesh/）や
- sparqlエンドポイントで提供されている（https://id.nlm.nih.gov/mesh/sparql ）

---
G2GMapperを使ってsparqlエンドポイントからMeSHコードの階層構造をグラフに変換しました

---
G2GMapperは、

- 大きい静的ファイルをパースするのに時間がかかる
- オフセットオプションを設定できない

などの理由で、今回は**ローカルのvirtuosoにftpサイトからDLしたN-Tripleファイル（mesh.nt）を読み込んで、
プロパティグラフへの変換**を行った

---
## G2G Mapperの設定

G2G Mapperは
aliasをdockerコンテナに設定して利用

```bash
$ alias g2g='docker run --rm -v $PWD:/work g2gml/g2g:x.x.x g2g'
```

---
## G2GMLの記述

TreeNumberが :parentTreeNumber の関係でカテゴリを示す接頭語==Aのトリプルをグラフとして取得する場合、
G2GMLは‥

```bash
PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>

(m:TreeNumber)
    ?m a meshv:TreeNumber .

(m1:TreeNumber)-[:parentTreeNumber]->(m2:TreeNumber)
  ?m1 meshv:parentTreeNumber ?m2 .
  FILTER(REGEX(?m1,'A'))
```

---
## G2G Mapperの実行

ローカルのvirtuosoのエンドポイントから変換を実行する場合下記のようにg2gを呼ぶ。
G2GMLが記述されたファイル名をmesh.g2gした場合‥

```bash
g2g mesh.g2g http://localhost:8890/sparql?default-graph-uri=http%3A%2F%2Flocalhost%3A8890%2FDAV
```


---
## MeSH Treeのグラフの出力

g2gによって、例えば下のようなプロパティグラフが出力される

```bash
// 例
A21.249   A21   :parentTreeNumber
```

※実際は前出のg2gでは、URIとしてノードは出力される。


---
## DescriptorとTreeとのリンク

MeSHコードにはMeSH descriptorが紐づくが、このTree構造のコードとコードとMeSH descriptorのリンクをマージしてグラフとして取得するため
asciiフォーマットのMeSHファイル（d2019.bin）に含まれるMeSH Tree NumberとMeSH UIで
エッジリストを書き出した（詳細は省く）

---

```bash
// 例
D014771 has_code A21.249

```

- ファイルから抽出したこのエッジは、プロパティ"has_code"とした
- RDFにTreeとUIの関係が含まれていれば利用するのだが見つからなかった

---
### Cytoscapeに読み込みTree構造のグラフと"MeSH-Tree"のエッジをマージ

<center><img src="https://github.com/dogrunjp/presentation/blob/master/images/mesh_descriptor_and_tree_network.png?raw=true" width=400></center>


---
### Neo4jへインポート

- マージしたグラフをNeo4Jに読み込むと、パスクエリを利用して面白い検索ができるかも

- 例えば、あるMeSH Tree Numberに直接だけではなく、その子階層で関係するMeSH UIをパスクエリで検索することができる

```sql
MATCH p=(u1)-[:has_code]->(c1)-[:parentTreeNumber*0..]->(:Code {Id:"A08.186.211.180"})
RETURN p
```

---
### パスクエリを使った検索のサンプル

A08.186.211.180の子階層以下のTree含めて関連するMeSHを検索したサンプル

<center><img src="https://github.com/dogrunjp/presentation/blob/master/images/mesh_neo4j_path_query_sample.png?raw=true" width=500></center>


