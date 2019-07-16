@title[Introduction]
## DBpediaからg2gを使いプロパティグラフを取得しWord2Vecアーティストの類似度を算出してみた

### 2019/7/16 [PGX ユーザー勉強会 #13](https://pgx.connpass.com/event/134129/)

### dogrun Inc. オーイシ


---
- Graphデータを対象とした機械学習すこしづつ盛り上がってます？
- RDFがMachine learning-readyであれば、整備されたRDFデータを活用しやすくなるかも

+++

ということで身近なデータであるDBpediaからg2gを使ってプロパティグラフを取得し
Graph Embedding(Word2Vec)で類似するノードを取得してみました。

WikipediaをMachine learning-readyな辞書として活用できたら面白いですよね。

---
## 実際の操作


---
### DockerのvirtuosoにDBpediaのttlを読み込む

+++

---
### G2Gでプロパティグラフに変換

+++

---
### Random walkとWord2Vec
 
 
[参考：DeepWalkを実装してみた](https://netres-bigdata.hatenablog.com/entry/2018/07/06/042240)  
 
+++


+++

### 類似度測定

model = Word2Vec(walks, min_count=, size=, window=, workers=)
vector = model.wv[wiki_page_id]
model.most_similar( [vector], [], 出力数)

+++
### 実際の利用例

```
$ python get_ranking.py <アーティスト名> <出力するランキング数> <pgのパス>
```
今回はこのスクリプトを

[https://github.com/dogrunjp/presentation/blob/master/20190716_pgx_event/get_ranking.py](https://github.com/dogrunjp/presentation/blob/master/20190716_pgx_event/get_ranking.py)

+++
#### 例１ Berryz工房の場合

```
$ python get_ranking.py Berryz工房 30 ../output/artist2artist/artist2artist.pg
```
+++

```
[{'id': '231703', 'label': 'Lia'}]
[{'id': '2750512', 'label': 'PUSHIM'}]
[{'id': '2654773', 'label': 'あのHUMPTY'}]
[{'id': '2682720', 'label': 'Chu-Z'}]
[{'id': '153854', 'label': '藤林聖子'}]
[{'id': '1841273', 'label': '新選組リアン'}]
[{'id': '3134418', 'label': '"THE HOOPERS"'}]
[{'id': '2064876', 'label': 'Annabel'}]
[{'id': '2263543', 'label': '"CANDY GO!GO!"'}]
[{'id': '1640646', 'label': 'アイスクリー娘。'}]
[{'id': '2280164', 'label': 'SISTAR'}]
[{'id': '875372', 'label': 'マシコタツロウ'}]
[{'id': '3320581', 'label': '仲澤莉南'}]
[{'id': '1804529', 'label': 'アイドルカレッジ'}]
[{'id': '757758', 'label': '"MICROPHONE PAGER"'}]
[{'id': '2281628', 'label': '"OKI (ヒップホップ・ミュージシャン)"'}]
[{'id': '292077', 'label': 'ジョー・リノイエ'}]
[{'id': '262972', 'label': '"まこと (ミュージシャン)"'}]
[{'id': '2834036', 'label': 'A応P'}]
[{'id': '1653207', 'label': 'さいとう大三'}]
[{'id': '2547659', 'label': "Μ's"}]
[{'id': '2437920', 'label': '"Flower (グループ)"'}]
[{'id': '2247399', 'label': 'ノースリーブス'}]
[{'id': '357359', 'label': '松橋未樹'}]
[{'id': '1028047', 'label': 'C-ZONE'}]
[{'id': '43606', 'label': 'ZYX'}]
[{'id': '1045454', 'label': 'Noria'}]
[{'id': '3319618', 'label': '"Luce Twinkle Wink☆"'}]
[{'id': '44373', 'label': 'Berryz工房'}]
[{'id': '1963403', 'label': 'イ・スンギ'}]

```

+++
#### 例２　サカナクションの場合

```
python get_ranking.py サカナクション 30 "../output/artist2artist/artist2artist.pg"
```

+++

```

[{'id': '114464', 'label': 'あがた森魚'}]
[{'id': '423432', 'label': '板東道生'}]
[{'id': '2544114', 'label': '"The SALOVERS"'}]
[{'id': '2235958', 'label': 'TOTALFAT'}]
[{'id': '2785207', 'label': 'サカナクション'}]
[{'id': '43564', 'label': 'P-MODEL'}]
[{'id': '82734', 'label': 'サディスティック・ミカ・バンド'}]
[{'id': '289581', 'label': 'うしろ髪ひかれ隊'}]
[{'id': '3219025', 'label': '黄雅莉'}]
[{'id': '3216598', 'label': '"GLIM SPANKY"'}]
[{'id': '2641960', 'label': '川上つよし'}]
[{'id': '695180', 'label': '寺井尚子'}]
[{'id': '338294', 'label': '加橋かつみ'}]
[{'id': '1777611', 'label': 'あらかじめ決められた恋人たちへ'}]
[{'id': '2136342', 'label': '山口一郎'}]
[{'id': '3020328', 'label': '"TAMTAM (ダブバンド)"'}]
[{'id': '2260672', 'label': '"BUMP OF CHICKEN"'}]
[{'id': '3203912', 'label': 'プリンセスケッツ'}]
[{'id': '2922519', 'label': 'ジャンニ・フェッリオ'}]
[{'id': '2935931', 'label': '中幸一郎'}]
[{'id': '3032350', 'label': '"DOPPEL (バンド)"'}]
[{'id': '2044174', 'label': 'SINCREA'}]
[{'id': '967381', 'label': '"BODY (バンド)"'}]
[{'id': '2103632', 'label': '渡辺美貴'}]
[{'id': '1734669', 'label': '"佐藤正治 (音楽家)"'}]
[{'id': '679442', 'label': 'ビセンテ・マルティーン・イ・ソレル'}]
[{'id': '2395453', 'label': '"螢 (歌手)"'}]
[{'id': '1660489', 'label': '西寺実'}]
[{'id': '1988974', 'label': 'Peronica'}]
[{'id': '2700168', 'label': 'HIKAKIN'}]
```

---
### とりあえずやってみた感想

- random walkからWord2Vecまでパラメータが非常に多い
- [Word2Vecで特定ノードの類似度を出力するスクリプトを公開しました](https://github.com/dogrunjp/presentation/blob/master/20190716_pgx_event/get_ranking.py)のでパラメータを色々変えて試してほしい
- 今回の環境構築、g2gの設定など公開しました
- 誰かやってみて！良い設定を見つけてください
- グラフ向けの機械学習を他にも試してみたい