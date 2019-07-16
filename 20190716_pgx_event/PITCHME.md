@title[Introduction]
## DBpediaからG2Gでプロパティグラフを取得しWord2Vecでアーティストの類似度を算出してみた

### 2019/7/16 [PGX ユーザー勉強会 #13](https://pgx.connpass.com/event/134129/)

### dogrun Inc. オーイシ


---
- Graphデータを対象とした機械学習すこしづつ盛り上がっている？？
- RDFなデータベースがMachine learning-readyであれば整備されたRDFデータがより活用しやすくなるかも

+++

ということで身近なデータであるDBpediaからG2Gを使ってプロパティグラフを取得し
Graph Embedding(Word2Vec)で類似するノードを取得してみました。

Wikipediaにある知識をMachine learning-readyな辞書としていろいろ活用できたら面白いですよね？

---
## 環境構築
---
### Dockerでvirtuosoを起動

```
docker run \
   -d \
    --name my_virtdb \
    --interactive \
    --tty \
    --env DBA_PASSWORD=hoge \
    --publish 1111:1111 \
    --publish  8890:8890 \
    -v `pwd`/database:/opt/virtuoso-opensource/database  \
    -v `pwd`/import:/import \
    -e "NumberOfBuffers=100000000" \
    -e "MaxDirtyBuffers=50000000" \
    openlink/virtuoso-opensource-7:latest
```
- -eは効いていないかも
- ResultSetMaxRowsの設定はDockerに入ってvirtuoso.iniを変更する必要があった
--- 
### Dockerのvirtuosoにttlをインポート

- [http://ja.dbpedia.org/dumps/20160407/](http://ja.dbpedia.org/dumps/20160407/)からttl取得
- database/virtuoso.iniに/importを追加しrestart
```
DirsAllowed = ., /opt/virtuoso-opensource/vad, /import
```
- virtuosoにttlをインポート
```
$ docker exec -it インスタンス名 /bin/bash
#  # isql -U dba -P $DBA_PASSWORD
SQL> ld_dir('/import', '*.ttl', 'http://dbpedia.org');
SQL> rdf_loader_run();
```

---
## RDFからプロパティグラフへの変換

---
### 今回試したG2GML (artist2artist.g2g)

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>

# Node mappings
(id:page_id {label:nam})
    ?mus rdf:type dbpedia-owl:MusicalArtist .
    ?mus rdfs:label ?nam . 
    ?mus dbpedia-owl:wikiPageID ?id .

# Edge mappings
(id1:page_id)-[:wikiPageWikiLink]->(id2:page_id)
    ?mus1 rdf:type dbpedia-owl:MusicalArtist .
    ?mus2 rdf:type dbpedia-owl:MusicalArtist .
    ?mus1 dbpedia-owl:wikiPageWikiLink ?mus2 .
    ?mus1 dbpedia-owl:wikiPageID ?id1 .
    ?mus2 dbpedia-owl:wikiPageID ?id2 .
```

<div class="sm">グラフのノードはWikiPageIDとした。あとSPARQL力が低い。。</div>

+++
### G2G実行

```
$ alias g2g='docker run --rm -v $PWD:/work g2gml/g2g:0.3.4 g2g'
$ g2g artist2artist.g2g http://xx.xx.xx.xx:8890/sparql  

```

ワーキングディレクトリの下に`output/artist2artist/artist2artist.pg` のようにpgファイルが出力されます

---
### Random walkとWord2Vec
 
 
<div class="c_sm"> [参考：DeepWalkを実装してみた](https://netres-bigdata.hatenablog.com/entry/2018/07/06/042240)  </div>

+++

### 類似度測定はおおよそこんな感じ

model = Word2Vec(walks, min_count=, size=, window=, workers=)

vector = model.wv[wiki_page_id]

model.most_similar( [vector], [], 出力数)

+++
### 実際の利用例

```
$ python get_ranking.py <アーティスト名> <出力するランキング数> <pgのパス>
```
<div class="c_sm">今回はこの↓スクリプトを使いました</div>

<div class="c_sm">
[https://github.com/dogrunjp/presentation/blob/master/20190716_pgx_event/get_ranking.py](https://github.com/dogrunjp/presentation/blob/master/20190716_pgx_event/get_ranking.py)
</div>

+++
#### Berryz工房の場合



```

$ python get_ranking.py Berryz工房 30 \
   "../output/artist2artist/artist2artist.pg"

```

+++
<div class="sxm">
[{'id': '231703', 'label': 'Lia'}]<br/>
[{'id': '2750512', 'label': 'PUSHIM'}]<br/>
[{'id': '2654773', 'label': 'あのHUMPTY'}]<br/>
[{'id': '2682720', 'label': 'Chu-Z'}]<br/>
[{'id': '153854', 'label': '藤林聖子'}]<br/>
[{'id': '1841273', 'label': '新選組リアン'}]<br/>
[{'id': '3134418', 'label': '"THE HOOPERS"'}]<br/>
[{'id': '2064876', 'label': 'Annabel'}]<br/>
[{'id': '2263543', 'label': '"CANDY GO!GO!"'}]<br/>
[{'id': '1640646', 'label': 'アイスクリー娘。'}]<br/>
[{'id': '2280164', 'label': 'SISTAR'}]<br/>
[{'id': '875372', 'label': 'マシコタツロウ'}]<br/>
[{'id': '3320581', 'label': '仲澤莉南'}]<br/>
[{'id': '1804529', 'label': 'アイドルカレッジ'}]<br/>
[{'id': '757758', 'label': '"MICROPHONE PAGER"'}]<br/>
[{'id': '2281628', 'label': '"OKI (ヒップホップ・ミュージシャン)"'}]<br/>
[{'id': '292077', 'label': 'ジョー・リノイエ'}]<br/>
[{'id': '262972', 'label': '"まこと (ミュージシャン)"'}]<br/>
[{'id': '2834036', 'label': 'A応P'}]<br/>
[{'id': '1653207', 'label': 'さいとう大三'}]<br/>
[{'id': '2547659', 'label': "Μ's"}]<br/>
[{'id': '2437920', 'label': '"Flower (グループ)"'}]<br/>
[{'id': '2247399', 'label': 'ノースリーブス'}]<br/>
[{'id': '357359', 'label': '松橋未樹'}]<br/>
[{'id': '1028047', 'label': 'C-ZONE'}]<br/>
[{'id': '43606', 'label': 'ZYX'}]<br/>
[{'id': '1045454', 'label': 'Noria'}]<br/>
[{'id': '3319618', 'label': '"Luce Twinkle Wink☆"'}]<br/>
[{'id': '44373', 'label': 'Berryz工房'}]<br/>
[{'id': '1963403', 'label': 'イ・スンギ'}]<br/>

</div>


+++

#### ℃-uteの場合

<div class="sxm">
[{'id': '688414', 'label': 'MICADELIC'}]<br/>
[{'id': '299913', 'label': 'イ・ヒョリ'}]<br/>
[{'id': '2173749', 'label': '"ミルキィホームズ (声優ユニット)"'}]<br/>
[{'id': '1205017', 'label': 'ジェジュン'}]<br/>
[{'id': '2438597', 'label': '"Sexy Zone"'}]<br/>
[{'id': '653506', 'label': '"DJ MASTERKEY"'}]<br/>
[{'id': '1206134', 'label': 'NORIKIYO'}]<br/>
[{'id': '3046510', 'label': 'MEG.ME'}]<br/>
[{'id': '2832706', 'label': 'シブヤDOMINION'}]<br/>
[{'id': '2389133', 'label': '里神楽・神代神楽研究会'}]<br/>
[{'id': '2894141', 'label': 'KAGAJO☆4S'}]<br/>
[{'id': '1974308', 'label': '鶴田加茂'}]<br/>
[{'id': '43046', 'label': 'ココナッツ娘。'}]<br/>
[{'id': '262972', 'label': '"まこと (ミュージシャン)"'}]<br/>
[{'id': '539477', 'label': '2BACKKA'}]<br/>
[{'id': '116871', 'label': 'M.c.A・T'}]<br/>
[{'id': '1946689', 'label': 'ユナク'}]<br/>
[{'id': '270325', 'label': '℃-ute'}]<br/>
[{'id': '2536161', 'label': '"Goose house"'}]<br/>
[{'id': '656522', 'label': '市川昭介'}]<br/>
[{'id': '3046080', 'label': '木之下慶行'}]<br/>
[{'id': '1018288', 'label': '中吉涼子'}]<br/>
[{'id': '2996580', 'label': '並木橋ハイスクール'}]<br/>
[{'id': '2787690', 'label': '"Hiroki Sagawa"'}]<br/>
[{'id': '441504', 'label': 'DROPS'}]<br/>
[{'id': '1386339', 'label': 'いちごはちみつ'}]<br/>
[{'id': '821110', 'label': '室屋光一郎'}]<br/>
[{'id': '616442', 'label': '坂上庸介'}]<br/>
[{'id': '1563888', 'label': 'しゅごキャラエッグ!'}]<br/>
[{'id': '2671030', 'label': 'Unico'}]<br/>
</div>

+++
#### サカナクションでは

```

python get_ranking.py サカナクション 30 \
    "../output/artist2artist/artist2artist.pg"
    
```

+++

<div class="sxm">
[{'id': '114464', 'label': 'あがた森魚'}]<br/>

[{'id': '423432', 'label': '板東道生'}]<br/>

[{'id': '2544114', 'label': '"The SALOVERS"'}]<br/>

[{'id': '2235958', 'label': 'TOTALFAT'}]<br/>

[{'id': '2785207', 'label': 'サカナクション'}]<br/>

[{'id': '43564', 'label': 'P-MODEL'}]<br/>

[{'id': '82734', 'label': 'サディスティック・ミカ・バンド'}]<br/>

[{'id': '289581', 'label': 'うしろ髪ひかれ隊'}]<br/>

[{'id': '3219025', 'label': '黄雅莉'}]<br/>

[{'id': '3216598', 'label': '"GLIM SPANKY"'}]<br/>

[{'id': '2641960', 'label': '川上つよし'}]<br/>

[{'id': '695180', 'label': '寺井尚子'}]<br/>

[{'id': '338294', 'label': '加橋かつみ'}]<br/>

[{'id': '1777611', 'label': 'あらかじめ決められた恋人たちへ'}]<br/>

[{'id': '2136342', 'label': '山口一郎'}]<br/>

[{'id': '3020328', 'label': '"TAMTAM (ダブバンド)"'}]<br/>

[{'id': '2260672', 'label': '"BUMP OF CHICKEN"'}]<br/>

[{'id': '3203912', 'label': 'プリンセスケッツ'}]<br/>

[{'id': '2922519', 'label': 'ジャンニ・フェッリオ'}]<br/>

[{'id': '2935931', 'label': '中幸一郎'}]<br/>

[{'id': '3032350', 'label': '"DOPPEL (バンド)"'}]<br/>

[{'id': '2044174', 'label': 'SINCREA'}]<br/>

[{'id': '967381', 'label': '"BODY (バンド)"'}]<br/>

[{'id': '2103632', 'label': '渡辺美貴'}]<br/>

[{'id': '1734669', 'label': '"佐藤正治 (音楽家)"'}]<br/>

[{'id': '679442', 'label': 'ビセンテ・マルティーン・イ・ソレル'}]<br/>

[{'id': '2395453', 'label': '"螢 (歌手)"'}]<br/>

[{'id': '1660489', 'label': '西寺実'}]<br/>

[{'id': '1988974', 'label': 'Peronica'}]<br/>

[{'id': '2700168', 'label': 'HIKAKIN'}]<br/>
</div>

---
### とりあえずやってみた感想

- random walk,Word2Vecのパラメータ多すぎ‥
- DBpediaからどの関係を取得すると良いのか？
- [Word2Vecでノードの類似度を出力するスクリプトを公開した](https://github.com/dogrunjp/presentation/blob/master/20190716_pgx_event/get_ranking.py)
- 誰かもっとやってみて！良い設定を見つけてください
- G2Gを使ってグラフ向けの機械学習を他にも試してみたい