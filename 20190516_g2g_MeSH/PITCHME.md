@title[Introduction]
# G2GMLを利用したMeSH RDFのプロパティグラフへの変換

### 2019/5/16 PGX ユーザー勉強会 #12

### dogrun Inc. Oishi

---
## Medical Subject Headings (MeSH)とは

PUBmedなどNLMの生物医学系データベースをインデックスするための階層化された用語集。

[Medical Subject Headings - Home](https://www.nlm.nih.gov/mesh/meshhome.html)

---
## MeSH Tree

- MeSHは16のカテゴリに分類される
- それぞれのカテゴリは最大13の専門性の詳細さによる階層構造を持つ
- MeSH descriptorは少なくとも一つのtree形状にひもづくが、だいたい複数のtreeに位置する

[MeSH Tree Structures](https://www.nlm.nih.gov/mesh/intro_trees.html)

---

このMeSH descriptorとtree構造のデータから
[G2G Mapper](https://g2gml.readthedocs.io/en/latest/contents/g2gml.html)を使いグラフを構築してみるというのが今回発表の趣旨。

---
## MeSH RDF

MeSHデータは各種フォーマットのファイル（ftp://nlmpubs.nlm.nih.gov/online/mesh/）や
sparqlエンドポイントで提供されている（https://id.nlm.nih.gov/mesh/sparql ）。

---

G2GMapperは、

- 大きい静的ファイルをパースするのに時間がかかる
- オフセットオプションを設定できない

などの理由で、今回はローカルのvirtuosoにftpサイトからDLしたN-Tripleファイル（mesh.nt）を読み込んで、
プロパティグラフへの変換を行った。

---
## G2G Mapperの設定

G2G Mapperは、
aliasをdockerコンテナに設定して利用。


> $ alias g2g='docker run --rm -v $PWD:/work g2gml/g2g:x.x.x g2g'


---
## RDFからプロパティグラフへの変換（G2GML）

TreeNumberが :parentTreeNumber の関係でカテゴリを示す接頭語==Aのトリプルをグラフとして取得する場合、
G2GMLは‥

```sparql
PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>

(m:TreeNumber)
    ?m a meshv:TreeNumber .

(m1:TreeNumber)-[:parentTreeNumber]->(m2:TreeNumber)
  ?m1 meshv:parentTreeNumber ?m2 .
  FILTER(REGEX(?m1,'A'))
```

---
## RDFからプロパティグラフへの変換（G2G Mapperの実行）

ローカルのvirtuosoのエンドポイントから変換を実行する場合下記のようにg2gを呼ぶ。
G2GMLが記述されたファイル名をmesh.g2gした場合‥


> g2g mesh.g2g http://localhost:8890/sparql?default-graph-uri=http%3A%2F%2Flocalhost%3A8890%2FDAV



---
## MeSH Treeのグラフの出力

g2gによって、例えば下のようなプロパティグラフが出力される。

**例**
> A21.249   A21   :parentTreeNumber


※実際は前出のg2gでは、URIとしてノードは出力される。


---
## MeSH descriptorととTreeとのリンク

MeSH TreeにはMeSH descriptorが紐づくが、このTreeとMeSH descriptorのリンクをグラフとして取得するため
asciiフォーマットのMeSHファイル（d2019.bin）に含まれるMeSH Tree NumberとMeSH UIで
エッジリストを書き出した。

**例**
> D014771 has_code A21.249

※ファイルから抽出したこのエッジは、プロパティ"has_code"とした

※RDFにTreeとUIの関係が含まれていれば利用するのだが見つからなかった

---
## MeSH Treeと MeSH descriptor - Tree





---
## Cytoscapeに読み込みTree構造のグラフととMeSH-Treeをマージ




---
## Neo4jに読み込んでプロパティパス検索
