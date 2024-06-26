# アーキテクチャ

- [アーキテクチャ](#アーキテクチャ)
  - [アーキテクチャとは](#アーキテクチャとは)
  - [3層アーキテクチャ](#3層アーキテクチャ)
  - [レイヤードアーキテクチャ](#レイヤードアーキテクチャ)
    - [メリットデメリット](#メリットデメリット)
  - [ヘキサゴナルアーキテクチャ](#ヘキサゴナルアーキテクチャ)
  - [オニオンアーキテクチャ](#オニオンアーキテクチャ)
    - [メリット](#メリット)
  - [クリーンアーキテクチャ](#クリーンアーキテクチャ)
  - [リソース指向アーキテクチャ(ROA)](#リソース指向アーキテクチャroa)
  - [外部リンク](#外部リンク)

## アーキテクチャとは

## 3層アーキテクチャ

## レイヤードアーキテクチャ

3層アーキテクチャを改善。Domain層を追加して、ビジネスロジック(Domain層)とソフトウェアが行うこと(Application層)を切り分けた。

### メリットデメリット

## ヘキサゴナルアーキテクチャ

ヘキサゴナル、オニオン、クリーンは本質的には一緒。

[DDD](./development.md#ドメイン駆動開発ddd)に基づいたアーキテクチャ。[依存性逆転の法則](./di.md#dip)を導入し、依存を薄くする。関心の分離。アプリケーションの外とはAdaptorを通じてやりとりすることだけを決めている。

## オニオンアーキテクチャ

ヘキサゴナルよりもっと具体的になった。ソフトウェアの内部構造を円環状に分割し各層の役割を定義したもの。中心方向にしか依存せず、依存する際はインターフェースに依存する(ヘキサゴナルのAdaptorも多分インターフェース)。

### メリット

従来のレイヤードアーキテクチャと比較して、

依存関係を減らしたい(柔軟性、保守性が上がる(参考：[DI](./di.md#di)))。対象の分離。層毎にしか依存しないから可読性も上がる。

ドメイン駆動開発を使っている。
そのため、プログラマが業務理解をした実装を行う。つまり、仕様把握できてバグを見つけやすい。
変更に対して強い。単純になりやすい(従来では複雑になりやすい)。
ドメインモデル、ドメインサービスへの単体テストがビジネスの要件を満たすことを確認することになる。

## クリーンアーキテクチャ

オニオンアーキテクチャの各層を細分化したもの。

## リソース指向アーキテクチャ(ROA)

4つの概念と4つの特徴がある。

- リソース：データ。
- URI：リソースの名前。
- 表現：JSON、XMLなど。
- リンク：別のリソースへのリンク

- アドレス可視性：URIを通してリソースを提供できること。
- ステートレス性：HTTPリクエストが全て分離/独立していること。以前のリクエストに依存せず、セッション管理なども行わない。
- 接続性：リソースはリンクを持つうること。
- 統一インターフェース：HTTPメソッドが定義通りに使われること。

## 外部リンク

- [MVC、3 層アーキテクチャから設計を学び始めるための基礎知識 - Qiita](https://qiita.com/os1ma/items/7a229585ebdd8b7d86c2)
- [ドメイン駆動設計(DDD)・オニオンアーキテクチャとは？ - Qiita](https://qiita.com/k_yamaki/items/bf99d3bf64a84258a3a1)：オニオンアーキテクチャ入門。
- [オニオンアーキテクチャとは何か - Qiita](https://qiita.com/cocoa-maemae/items/e3f2eabbe0877c2af8d0)：オニオンアーキテクチャ入門。(TODO:上のリンクとどちらかだけでいいのでは)
- [ドメイン駆動設計で実装を始めるのに一番とっつきやすいアーキテクチャは何か](https://little-hands.hatenablog.com/entry/2017/10/04/231743)：オニオン、クリーン入門。
- [DDDの一般的なアーキテクチャをまとめてみた](https://zenn.dev/ayumukob/articles/ff183004d09ede)：ヘキサゴナル、オニオン、クリーン、特にクリーン重点的。
- [クリーンアーキテクチャ完全に理解した - gist](https://gist.github.com/mpppk/609d592f25cab9312654b39f1b357c60)：クリーンアーキテクチャについて重点的。
- [実践クリーンアーキテクチャ with Java](https://nrslib.com/clean-architecture-with-java/)：Javaでクリーンアーキテクチャの実装イメージを掴める。
