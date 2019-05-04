@title[Introduction]
# G2GMLを利用したMeSH RDFのプロパティグラフへの変換

### 2019/5/16 PGX ユーザー勉強会 #12

### オーイシ

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
## MeSH RDF：


MeSHデータは各種フォーマットのファイル（ftp://nlmpubs.nlm.nih.gov/online/mesh/）やsparqlエンドポイント（https://id.nlm.nih.gov/mesh/sparql）で提供されている

G2GMapperの変換は
- 静的なファイルから変換する場合、大きいファイルをパースするのに時間がかかる
- sparqlエンドポイントで利用する場合オフセットオプションを設定できない

だったため、ローカルのvirtuosoにftpサイトからDLした
N-Tripleファイル（mesh.nt）を読み込んで、ローカルのvirtuosoを使ってRDFからグラフへの変換を行った。


---
## G2G Mapperの設定

G2G Mapperは、aliasをdockerコンテナに設定して利用する

```
$ alias g2g='docker run --rm -v $PWD:/work g2gml/g2g:x.x.x g2g'
```

---
## RDFからプロパティグラフへの変換



---
## MeSH Treeのグラフ


---
## MeSH descriptorととMeSH Treeとのリンクを抽出

d2019

---
## MeSH Treeと MeSH descriptor - Tree



---
## Cytoscapeに読み込みTree構造のグラフととMeSH-Treeをマージ




---
## Neo4jに読み込んでプロパティパス検索
