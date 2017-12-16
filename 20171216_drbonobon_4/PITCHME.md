# 4. 基本データ解析

## Dr.Bonoの生命科学データ解析 読書会

2017-12-16

大石直哉 @oec014


+++

## 発表者紹介

- 大石直哉
- Twitter: [@oec014](http://twitter.com/oec014)
- 株式会社ドッグラン 代表
- 開発＆デザイン
    - 生命科学研究分野のデータ可視化サービスを開発しています。
    - 同じく生命科学研究分野の日本語コンテンツサービスの開発しています。

+++

## 4.1 配列データ解析

次世代シークエンサー（NGS）は大量の塩基配列データを生み出します。
大量の配列データの持つ意味を明らかにするためにはコンピュータによるデータ解析が必要です。
本章では配列データの解析手法・配列データの解析に使われるアプリケーションを紹介します。

+++

### 配列アラインメントとツール 

+++

### ペアワイズアラインメント


配列解析の基本は二本の配列を並べる（アライメントする）こと。
以下、二本の配列のアライメント・解析の手法・バリエーションを紹介します。

+++

二本の配列を並べ、同じ文字が縦に揃うように並べることを __ペアワイズドアライメント__ という。
ペアワイズドアライメントは生命科学の配列データ解析の基本となる。
例えば
- 個体のゲノムの比較
- 異なる生物種間の比較し進化の系統樹

+++

４章で紹介されるアライメントツールの多くは
__EMBOSSパッケージ__ として利用できます。

Macの場合はパッケージ管理システムの[Homebrew](https://brew.sh/index_ja.html)
```
$ brew install -v EMBOSS

```
でインストールできます。
Homebrewはあらかじめ自分でインストールしておく必要がありますが、Macでデータ解析をする際には入れておいた方が良いでしょう。

+++
##### ドットプロット

二本の配列間の類似性を可視化する手段。
図4.1では[EMBOSS dottup](http://www.bioinformatics.nl/cgi-bin/emboss/dottup)で作成されたドットプロットが示されています。
図のようにゲノムとmRNAの類似する部分や自分自身の繰り返し配列を可視化することができます。

+++ 


### 大域的アラインメント（Global alignment）

+++

__大域的アラインメント__ とは配列中の全塩基やアミノ酸を並べるようにする方法。
現在Needleman-Wunch法と呼ばれる方法が広く使われている。

Needleman-Wunch法の実装としてEMBOSSでは
[needle](https://www.ebi.ac.uk/Tools/psa/emboss_needle/)というプログラムが利用できます。

+++

Needleman-Wunch法は、homebrewでEMBOSSをインストールできたら簡単に試せます。
（以下、簡単なアミノ酸を二つのファイルに入力してアライメント）

```
$ needle sample_eaa1.txt sample_eaa2.txt
Needleman-Wunsch global alignment of two sequences
Gap opening penalty [10.0]: # Gap open : ギャップを作るコスト
Gap extension penalty [0.5]: # Gap extension : ギャップ伸長のコスト
Output alignment [sample_eaa1.needle]:
```

+++

```
# Program: needle
# Rundate: Thu  7 Dec 2017 22:43:06
# Commandline: needle
#    [-asequence] sample_eaa1.txt
#    [-bsequence] sample_eaa2.txt
# Align_format: srspair
# Report_file: test_short_aa1.needle
########################################

#=======================================
#
# Aligned_sequences: 2
# 1: 
# 2: 
# Matrix: EBLOSUM62
# Gap_penalty: 10.0
# Extend_penalty: 0.5
#
# Length: 9
# Identity:       9/9 (100.0%)
# Similarity:     9/9 (100.0%)
# Gaps:           0/9 ( 0.0%)
# Score: 52.0
# 
#
#=======================================

                   1 WKMFTVLIH      9
                     |||||||||
                   1 WKMFTVLIH      9
```
+++

### 局所的アラインメント

+++

大域的アライメントの方法を改良して、部分的な類似性が見つけられるようにした手法は
__局所的アライメント（Local Alignment）__ と呼ばれます。

局所的アライメントの方法として最もよく用いられているのが __Smith-Waterman法__ 。

EMBOSSでは __water__ というプログラムでSmith-Waterman法によるアライメントが実行可能です。

+++

```
$ water sample_eaa1.txt sample_eaa3.txt
Smith-Waterman local alignment of sequences
Gap opening penalty [10.0]: 
Gap extension penalty [0.5]: 
Output alignment [sample_eaa1.water]: 
```
+++
```
# Aligned_sequences: 2
# 1: 
# 2: 
# Matrix: EBLOSUM62
# Gap_penalty: 10.0
# Extend_penalty: 0.5
#
# Length: 11
# Identity:       9/11 (81.8%)
# Similarity:     9/11 (81.8%)
# Gaps:           2/11 (18.2%)
# Score: 41.5
# 
#
#=======================================

                   1 WKM--FTVLIH      9
                     |||  ||||||
                   5 WKMPSFTVLIH     15
```
+++

局所的アライメントは手持ちの配列を用いて、データベースの全ての配列を仮想的な一つの配列とみなし、
配列類似性のデーターベース検索に応用されてきた。

FASTAパッケージに含まれているssearchというプログラムではSmith-Waterman法によるDB配列検索が用いられている。

+++

ssearchはmacではhomebrewでインストールできます。

```
$ brew install -v fasta
```

ssearchは-Tオプションでスレッド数を指定でき、結果をえるまでの実行時間を短縮することができる。
コンピュータの並列処理によるデータベース配列検索がssearchに寄って可能になった。

+++

### FASTA 法

+++

局所的アライメントは高速なBLASTがギャップを許容しない配列検索だったことから、当初FASTAがよく用いられていた。

FASTAによるアラインメントのプロセスは...
1. 文字のかたまりとして行うギャップを考慮しない初期検索
1. 初期検索で見つかった領域をつなぎ合わせ得られる領域で最もスコアの高い周辺でSmith-Waterman法によるアラインメントを実行
1. 各配列の長さや、DB全体のサイズを考慮した統計値のz-scoreと期待値が計算され最終的な配列類似性の評価に用いられる。


+++

FANTOMプロジェクトのcDNA解析の際には、フレームシフトを考慮して __クエリの塩基配列をアミノ酸に翻訳して__
配列比較を行うプログラムの __fastx__ と __fasty__ が有用だったとのこと。

+++

fastyと同様にフレームシフトを許して、アミノ酸配列をゲノムやESTの塩基配列にペアワイズするアライメントツールとして
__GeneWise__ もある。

+++

__genewise__ はイントロンを考慮してアミノ酸配列をゲノム配列に対して、

__estwise__ はアミノ酸配列をcDNA/EST配列に大してそれぞれペアワイズアライメントするプログラム

このプログラムは、[EBIのWebインターフェース](https://www.ebi.ac.uk/Tools/psa/genewise/)から利用でき、
またmacOSではHomebrewでローカルマシンにインストールすることができる。

```
$ brew instawll -v genewise
```

+++

### BLAST

+++

__BLAST(Basic Local Alignment Search Tool)__ はNCBIで開発された配列類似性検索のためのツール
macOSではHomebrewでローカルマシンにインストールすることができる。

```
$ brew install -v blast
```

+++

ローカルマシンでの利用だけでなく、[NCBIのWebサイト](https://blast.ncbi.nlm.nih.gov/Blast.cgi)でもBLASTを利用することはできる。
Weサイトからの利用では、検索対象DBはサーバにありqueryだけ自前で準備すれば良い。


NCBIのBLASTでは目的別の多用な目的用の検索が用意されている。詳細は[統合TV](http://doi.org/10.7875/togotv.2017.023)を見てください。

+++
次の図はある塩基配列を[NCBI BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi)にかけた結果返ってきたアラインメントです。

+++

![アラインメント](images/NCBI_BLAST_result_alignment.png)

+++

#### BLASTのコマンド

BLASTのquery配列はFASTA形式、コマンドラインツールを利用する際のDBとして
はmulti-FASTA形式の塩基 OR アミノ酸配列である必要がある。

DBはBLAST検索用にindexを形成して置く必要があるが、
下記コマンドの __makeblastdb__ でindexは作成できる。このツールはblastインストール時に同時にインストールされる。

+++

BLASTの実行はqueryとDBの組み合わせ（塩基配列とアミノ酸配列）
によって、使うプログラムが異なってきます。

+++

例えばqueryとDB共に塩基配列のケースでは、コマンドは下記のようになる。

```
$ blastn -query sample_query.fa -db sample_genome.fa
```

+++

BLASTのプログラムには __blastn__, __tblastx__, __blastx__, __tblastn__, __blastp__　がある。
塩基配列レベルの比較を行うのはblastnのみ。tblastnとtblastxは塩基配列をアミノ酸に翻訳しながら配列比較するため、
他のプログラムに比べると実行時間ははるかに長くなる。

+++

デフォルトのBLASTの出力は目でアラインメントを見て評価するという目的には合致するが、
コンピュータに大量に処理させる目的には向いていない。そのため、出力オプションの __-ouftmt__ で別の出力形式を選択し、
大量処理用に出力することがよく行われる。

+++

BLASTの __-outfmt__ などのオプションについては[NCBIのコマンドラインユーザマニュアル](https://www.ncbi.nlm.nih.gov/books/NBK279684/)のTable C1に記述があります。
また、[統合TVにもLocal BLASTの使い方について2017年にアップデートされた動画](http://doi.org/10.7875/togotv.2017.045)があり、
この動画でもLocal BLASTのオプションなどについて学習することができます。

+++
#### BLAT

__BLAT（The BLAST-Like Alignment Tool）__ は検索対象を __リファレンスゲノム配列__ に特化させた配列類似性検索のためのツール。
リファレンスゲノムのみを対象のDBとし、ほぼ一致する領域を探すことに特化しているため非常に高速。

+++
BLATは、
[UCSC Genome Browser](https://genome.ucsc.edu/cgi-bin/hgBlat)のサイトにあるウェブインターフェースから利用されることが多い。
[統合TVの2017の動画で](http://doi.org/10.7875/togotv.2017.093)UCSCのウェブサイトからり利用できるBLATの使い方が紹介されています。

+++

また、macOSであれば下記のようにHomebrewでBLATをローカルマシンにインストールすることもできます。

```
$ brew install -v blat
```

コマンドラインで実行する場合、queryはFASTあるいはmulti-FASTA形式、検索対象のDBはmulti-FASTA、
出力がPSL形式となリマス。

+++
    
### 多重配列アライメントと系統樹

+++

__多重配列アラインメント__ はできるだけギャップを入れないようにして、三本以上のアミノ酸もしくわ塩基配列を並べる手法。

アラインメントした結果から __分子系統樹__ が推定され、その結果を見てまたアラインメントを改良するという、
多重配列アラインメントと分子系統樹は非常に密接な関係にある。

+++

多重配列アラインメントのツールとして __Clustalシリーズ__ が使われてきた。FORTRANで書かれたClustalシリーズが使われていたが、
その後C言語で書き直された __ClustalV__ やその改良版の __ClustalW__ が広く使われてきました。

ClustalWでは入力された配列の全てのペアでアラインメントを作成しスコアが計算され、
配列ペア間の全スコアをもとにガイドツリーが作成される。現在ではガイドツリー作成が高速化された __Clustal Omega__ が利用可能になっている。

+++

__Clustal Omega__ は[EBIのウェブインターフェース](https://www.ebi.ac.uk/Tools/msa/clustalo/)で手軽に利用できる。
macOSの場合はHomebrewで以下のようにインストールすることができる<sup>[*](#note1)</sup>

```
$ brew install -v clustal-omega
```

+++
*自分の環境（macOS 10.12.6）ではbrew installでMake errorが発生しました。

Clustal omegaはanacondaのパッケージの一つである[biocondaからもインストールできる](https://anaconda.org/bioconda/clustalo)ので、
こちらを利用しても良いかもしれません。
```
$ conda install -c bioconda clustalo 
```

+++

clustaloコマンドを以下のように入力するとアライメントの結果のギャップが入ったmulti-FASTA形式のファイルが出力される。
```
$ clustalo -i unaligned.mfa -o aligned.mfa
```
+++

よく利用される多重配列アラインメントプログラムとして一万個以上の配列に対してアライメント可能な __MAFFT__ がある。

MAFFTはClustal Omega同様、ウェブインターフェースでも、次のようにインストールしてコマンドラインからでも利用することができる。


+++
```markdown
$ brew install -v mafft
```
```markdown
$ mafft unaligned.mfa > aligned.mfa
```
+++

Clustal OmegaやMAFFTで作成した多重配列アラインメントの結果は __Jalview__ などのソフトウェアで可視化できます。
様々なバージョンのアプリケーションが[サイト](http://www.jalview.org)からダウンロードでき、
使い方は統合TV[「Jalviewを使って配列解析・系統樹作成をする 2013」](http://doi.org/10.7875/togotv.2013.049)で学習できます。

+++

![Jalviewで生成した系統樹](./images/Jalview_tree.png)

+++

### マッピング（Suffix Array）


+++
次世代シークエンサーの登場で個人ゲノム配列や様々なサンプルの転写産物の配列が大量に解読できるようになりました。

限定されたクエリ配列を用いた巨大なDBの検索から、
読まれた膨大の配列データは、まずヒトゲノムやマウスゲノムにマッピングするのが現在の __配列類似性検索__ 。

巨大なクエリとなるデータを用いて、配列類似性を超高速に行うのを可能にした __特別なインデックス化__ を用いた技術が
 __Suffix Array__ です。

+++

#### Suffix Arrayを利用したソフトウェア

__BWA__ と __Bowtie__ は次世代シークエンサーから出たデータをリファレンスゲノムにマッピングすることに特化した
ソフトウェアです。

検索対象のDB（リファレンスゲノム配列）があらかじめ[Burrows Wheeler Transform(BWT)](https://research.preferred.jp/2012/11/burrows-wheeler-transform-lf-mapping/)で前処理されていて
検索対象文字列の出現位置を高速に検索でき、また非常に短い配列でも検索可能です。

+++

BWAの場合インデックス作成は、multi-Fasta形式のリファレンスゲノム配列hogenome.faである場合下記のように指定する。

```
$ bwa index hogenome.fa
```
+++

Bowtieの場合はbowtie-buildコマンドを用います

```
$ bowtie-build hogenome.fa honenome
```

ヒトやマウスの場合、BWAやBowtie用のインデックス作成済みのリファレンスゲノム配列ファイルが提供されているので、
それを使うことができます。

+++

実際の検索は

```markdown
bwa t4mem hogenome.fa hoge.fastq.gz > hoge.sam
```

```markdown
bowtie -q -x hogenome -S hoge.sam -p 4 hoge.fastq.gz
```

のように行います。

これらの計算は、コンピュータに非常に大きな負荷がかかるため、並列化が必須で、
自らの環境に合わせたスレッド数の設定を指定する必要があります。

+++

#### GGRNAとGGGenome

BWAやBowtieと同様Suffix Arrayを利用したツールとして、
[GGRNA](https://ggrna.dbcls.jp/ja/)と[GGGenome](http://gggenome.dbcls.jp)が
[DBCLS](http://dbcls.rois.ac.jp/)のサービスとして公開されていてる。

これらサービスを使うとGoogleで検索するように塩基配列の検索を行うことができます。


+++

### アッセンブル

+++

長い塩基配列の読める次世代シークエンサーが登場しても、染色体一本をまるごとひと続きの
塩基配列として解読することはできません。

そこで解読した配列をコンピュータ上で
__アッセンブル（組み立てる）__ することが必要となります。

+++

#### ゲノム配列のアッセンブル

ヒトのサンプルだけを扱う場合は直接アッセンブルすることは無く
ゲノムへのマッピング-リファレンス配列との差分の解析が行われます。

これまでよく使われてきたヒト疾患モデル生物に関しても
リファレンスゲノム配列がすでに得られていて、それを利用可能なことが多い。

+++

#### 新しい生物種のゲノム配列では...

今後モデルとして新規な生物種を利用する際には、
その生物種のゲノム配列とゲノムアノテーションが必要となり
自らそれを行う必要があるかもしれません。

+++

ゲノム配列のassemblerは和製の[platanas](http://platanus.bio.titech.ac.jp/?page_id=2)など
様々なツールがあり、それらは[nucloetid.es](http://nucleotid.es)にassemblerカタログとして
公開されています。

assembleは実行に非常に多くのメモリを必要とし、ローカルのコンピュータで実行するのが困難であるため
国立遺伝学研究所のスーパーコンピュータシステムを申請して利用することが推奨される、とのこと。

有償ではあるが、[CLC Assembly Cell](CLC Assembly Cell)のように使用するメモリが少なくてもすむ
ソフトウェアもあります。

+++

### 転写配列のアッセンブル

+++

ヒトのサンプルだけを扱う研究では、ゲノムアッセンブル同様不要なものかもしれません。

しかし、解読された __転写配列__ __（transcriptome）__ を全てクラスタリングする
__Trinity__ のようなソフトウェアをうまく利用すると、既知の遺伝子セットには無い遺伝子が
発見されることも十分考えられます。


+++
 
TrinityはmacOSでHomebrewでインストールできます。
```markdown
$ brew install -v Trinity
```
ただし実行には多くのメモリが必要とされるため、遺伝研のスパコンを利用した方が良いかもしれません。

+++


### 数値データ解析

+++

#### 階層的クラスタリング

生命科学の分野では、それぞれの類似性に基づいた __デンドログラム（樹形図）__ や、
特に遺伝子間の進化的距離による分子系統樹という形で __階層的クラスタリング__ が利用されてきました。

+++

大量の遺伝子発現を一度に測定できるマイクロアレイの登場によって
とランスクリプトームデータの解析が可能となり、
階層的クラスタリングを用いた遺伝子発現の挙動が似ている遺伝子群のクラスタリングが
頻繁に行われるようになりました。

+++

#### 階層クラスタリングの計算方法

全てのノード（例えば遺伝子）間の距離を、
配列類似性や遺伝子発現の類似度などで計算します。

ノード間の距離の計算方法には

- 最短距離法
- 際長距離法
- 群平均法
- ウォード法

など幾つかの流儀があり、これらの計算によってクラスターの結合を繰り返し
最後にクラスター結合の結果を樹形図で可視化します。

+++

#### 階層的クラスタリングの実装と可視化

- 系統樹作成にはGUIをもつソフトウェアの[MEGA](http://togotv.dbcls.jp/20171106.html)（Molecular Evolutionary Genetics Analysis）がよく用いられる。

- 遺伝子発現解析では __XCluster__ や __TreeView__　がアカデミックフリーのソフトとして、
有償のマイクロアレイデータ解析ソフトウェアとしてGeneSpringが使われてきた

- 汎用の解析環境として、R言語の __Bioconductor__ で利用可能なパッケージを利用することが多い。
- [TIBCO Spotfire](http://togotv.dbcls.jp/20170406.html)のような __Buisiness Inteligenct__ __(BI)__ ソフトウェアに階層クラスタリング機能をもつものもある。

+++
### 主成分分析

+++

__主成分分析（PCA:Principal Component Analysis）__ は、
多次元のデータを低次元に圧縮する古くから使われる統計解析手法だが、
解析データが一度にたくさん得られるようになった現在、
様々な種類の生命科学データ解析で使用され、出力結果の図を見る機会も多い。

多次元のデータの次元を圧縮し、より少ない次元で元のデータを表現することが狙いの解析で
__R言語の標準関数 procomp__ や、__Pythonのscikit-learn__ などのパッケージで計算することができる。


+++

Macを持っている、大学に自由に使えるMacがあるようでしたら、
４章のツールの多くは無償でインストールして簡単＆すぐに使うことができます。








