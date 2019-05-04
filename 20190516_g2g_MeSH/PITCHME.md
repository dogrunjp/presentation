@title[Introduction]
# G2GMLを利用したMeSH RDFのプロパティグラフへの変換

### 2019/5/16 PGX ユーザー勉強会 #12

### dogrun Inc. 

---
## Medical Subject Headings (MeSH)とは

PUBmedなどNLMの生物医学系データベースをインデックスするための階層化された用語集。

[Medical Subject Headings - Home](https://www.nlm.nih.gov/mesh/meshhome.html)

---
## MeSH Tree

- MeSHは16のカテゴリに分類される
- それぞれのカテゴリは最大13の専門性の深さによる階層構造を持つ
- MeSH descriptorは少なくとも一つのtree形状にひもづくが、だいたい複数のtreeに位置する

[MeSH Tree Structures](https://www.nlm.nih.gov/mesh/intro_trees.html)

このMeSH descriptorとtree構造のデータから[G2G Mapper](https://g2gml.readthedocs.io/en/latest/contents/g2gml.html)を使いグラフを構築してみるというのが今回発表の趣旨。

---
## MeSH RDF

MeSHデータは各種フォーマットのファイル（ftp://nlmpubs.nlm.nih.gov/online/mesh/）や
sparqlエンドポイント（https://id.nlm.nih.gov/mesh/sparql ） で提供されている

G2GMapperは、大きい静的ファイルをパースするのに時間がかかる、オフセットオプションを設定できないなどの理由で、
ローカルのvirtuosoにftpサイトからDLしたN-Tripleファイル（mesh.nt）を読み込んで、プロパティグラフへの変換を行った。


---
## G2G Mapperの設定

G2G Mapperは、
aliasをdockerコンテナに設定して利用。

```
$ alias g2g='docker run --rm -v $PWD:/work g2gml/g2g:x.x.x g2g'
```

---
## RDFからプロパティグラフへの変換（G2GML）

TreeNumberが :parentTreeNumber の関係かつカテゴリを示す接頭語==Aのトリプルをグラフとして取得する場合、
このG2GMLをファイルに保存しておく。

```
PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>

(m:TreeNumber)
    ?m a meshv:TreeNumber .

(m1:TreeNumber)-[:parentTreeNumber]->(m2:TreeNumber)
  ?m1 meshv:parentTreeNumber ?m2 .
  FILTER(REGEX(?m1,'A'))
```


---
## RDFからプロパティグラフへの変換（G2G Mapperの実行）

ローカルのvirtuosoから（mesh.g2gとする）で変換を実行する場合下記のようにg2gを呼ぶ。

```
g2g mesh.g2g http://localhost:8890/sparql?default-graph-uri=http%3A%2F%2Flocalhost%3A8890%2FDAV
```


---
## MeSH Treeのグラフ

先ほどのファイルを（例えばmesh.g2gとして）を呼び出すと、例えば下のようなプロパティグラフが出力される。



```
A21.249   A21   :parentTreeNumber
```

※実際は前出のg2gでは、URIとして出力される。


---
## MeSH descriptorととMeSH Treeとのリンクを抽出

d2019

---
## MeSH Treeと MeSH descriptor - Tree



---
## Cytoscapeに読み込みTree構造のグラフととMeSH-Treeをマージ




---
## Neo4jに読み込んでプロパティパス検索
