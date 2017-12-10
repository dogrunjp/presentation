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
    - 生命科学研究分野のデータ可視化ツール開発
    - 同じく生命科学研究分野の日本語コンテンツサービスの開発
    
+++

## 4.1 配列データ解析

次世代シークエンサー（NGS）は大量の塩基配列データを生み出します。
大量の配列データの持つ意味を明らかにするためにはコンピュータによるデータ解析が必要です。
この章ではまず配列データの解析手法と配列データの解析に使われるアプリケーションを紹介します。

+++

### 配列アラインメントとツール 

#### ペアワイズアラインメント


配列解析の基本は二本の配列を並べる（アライメントする）こと。
以下、二本の配列のアライメント・解析の手法・バリエーションを紹介します。



二本の配列を並べ、同じ文字が縦に揃うように並べることを __ペアワイズドアライメント__ という。
ペアワイズドアライメントは生命科学の配列データ解析の基本となる。
例えば
- 個体のゲノムの比較
- 異なる生物種間の比較し進化の系統樹

４章で紹介されるアライメントツールの多くは
__EMBOSSパッケージ__ として利用できます。

Macの場合はパッケージ管理システムの[Homebrew](https://brew.sh/index_ja.html)
```
brew install -v EMBOSS

```
でインストールできます。
Homebrewは自分でインストールされている必要がありますが、Macでデータ解析をする際にはほぼ必須です。

+++
##### ドットプロット

二本の配列間の類似性を可視化する手段。
図4.1は[EMBOSS dottup](http://www.bioinformatics.nl/cgi-bin/emboss/dottup)で作成されたドットプロットで、
横方向のアフリカツメガエルのRhodopsin遺伝のゲノム領域5000塩基以降に、
縦方向のmRNAとの断続的な類似部分がプロットされています。
また斜め線として現れる５つの断続的な類似部分からエクソンが５つあることが表れています。

図4.2のようにドットプロットを自分自身の配列と比較して（縦、横に自分の配列をとる）、
配列内部の繰り返し配列を可視化することもできます。

+++ 


##### 大域的アラインメント（Global alignment）

大域的アライメントとは配列中の全塩基やアミノ酸を並べるようにする方法。
現在Needleman-Wunch法と呼ばれる方法が広く使われている。

Needleman-Wunch法の実装としてEMBOSSでは
[needle](https://www.ebi.ac.uk/Tools/psa/emboss_needle/)というプログラムが利用できる

+++

homebrewでEMBOSSをインストールできたら、簡単に試せます。
（以下、必須アミノ酸同士を二つのファイルに入力してアライメントしている）

```
$ needle sample_eaa1.txt sample_eaa2.txt
Needleman-Wunsch global alignment of two sequences
Gap opening penalty [10.0]: # Gap open : ギャップを作るコスト
Gap extension penalty [0.5]: # Gap extension : ギャップを伸長するコスト
Output alignment [sample_eaa1.needle]:
```

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

##### 局所的アラインメント

大域的アライメントの方法を改良して、部分的な類似性が見つけられるようにした手法は
局所的アライメント（Local Alignment）と呼ばれます。
局所的アライメントの方法として最もよく用いられているのが __Smith-Waterman法__ 。

EMBOSSでは __water__ というプログラムでSmith-Waterman法によるアライメントが実行可能。
局所的アライメントでは、局所的によく似ている部分だけをアライメントしている。
次の例では9アミノ酸配列と15アミノ酸配列をアライメントしているが似ている部分だけがアライメントされている。

```
$ water sample_eaa1.txt sample_eaa3.txt
Smith-Waterman local alignment of sequences
Gap opening penalty [10.0]: 
Gap extension penalty [0.5]: 
Output alignment [sample_eaa1.water]: 
```

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

局所的アライメントは手持ちの配列を用いて、データベースの全ての配列を仮想的な一つの配列とみなした、
配列類似性のデーターベース検索に応用されてきた。

FASTAパッケージに含まれているssearchというプログラムではSmith-Waterman法によるDB配列検索が用いられている。

ssearchは
```
brew install -v fasta
```
でインストールできる。
ssearchは-Tオプションでスレッド数を指定でき、結果をえるまでの実行時間を短縮することができる。

+++

##### FASTA 法







    - BLAST
    - BLAT
    
    
#### 多重配列アライメントと系統樹


### マッピング（Suffix Array）
- BWAとBowtie
- GGRNAとGGGenome

### アッセンブル
- ゲノム配列のアッセンブル
- 転写配列のアッセンブル

+++

## 数値データ解析

大量の遺伝子発現を一度に測定できるマイクロアレイの登場移行、
遺伝子発現量の解析 （トランスクリプトーム解析）が可能になりました。

次に遺伝子発現量の類似性や遺伝子間の距離算出など、
実験結果より得られたデータに統計的な意味を見出し・可視化する解析手法を紹介します。

+++

### 階層的クラスタリング
- 階層的クラスタリングとは？
- 階層的クラスタリングの計算法
- 階層的クラスタリングの実装と可視化

### 主成分分析





