# Java

- [Java](#java)
  - [POJO以外](#pojo以外)
    - [ビルドツール](#ビルドツール)
      - [Maven](#maven)
      - [Gradle](#gradle)
    - [フレームワーク](#フレームワーク)
      - [Spring](#spring)
      - [Seasar2](#seasar2)
      - [JUnit](#junit)
  - [POJO](#pojo)
    - [総括的なページ](#総括的なページ)
    - [書籍のメモ](#書籍のメモ)
      - [付属のコード](#付属のコード)
    - [WEB+DBの記事](#webdbの記事)
    - [特定の機能についてのページ](#特定の機能についてのページ)
    - [個人的メモ](#個人的メモ)
    - [疑問](#疑問)

## POJO以外

### ビルドツール

- [ビルドツール make / ant / maven / gradle ざっくり理解メモ - Qiita](https://qiita.com/MahoTakara/items/ff73338e218b656bedfa)

#### Maven

- [Mavenの基本勉強メモ - Qiita](https://qiita.com/opengl-8080/items/bb32732f9aa5cb3495d2)
- [Maven関連](http://www.sangyo-rock.com/tech/index.php?Maven%B4%D8%CF%A2)

#### Gradle

- [ただ build.gradle を読めるようになりたい - Qiita](https://qiita.com/_mi/items/4aea84f14e5b35ee6cda)

### フレームワーク

- [Javaで超簡易Webフレームワークを作ってみよう - Qiita](https://qiita.com/hatimiti/items/79b6bd1003fe6bfec2f3)
- [作って理解するDIコンテナ](https://nowokay.hatenablog.com/entry/20160406/1459918560)

#### [Spring](./spring.md)

#### [Seasar2](./seasar2.md)

#### JUnit

- [JUnit 5 ユーザーガイド](https://oohira.github.io/junit5-doc-jp/user-guide/#overview)
- [JUnitのassertThatを使う理由 - Qiita](https://qiita.com/YNYS/items/8090048d3f540455b699)：そこまでassertThatじゃなくてもassertEqualsでいい、という話

## POJO

POJO(Plain Old Java Object:普通のJava)について。

- [dokojava](https://dokojava.jp/sources)：Web上でJavaが実行できるサービス

### 総括的なページ

ドキュメントなど

- [Oracleのバージョン別](https://www.oracle.com/jp/java/technologies/documentation.html)
- [Java EEの概要 - Oracle](https://www.oracle.com/jp/java/technologies/java-ee-glance.html)
- [Jakarta EE 8 仕様 API](https://spring.pleiades.io/specifications/platform/8/apidocs/overview-summary.html)：Springが公開しているページかな...?
- [Java言語規定](http://www.y-adagio.com/public/standards/tr_javalang/index.htm)
- [Java コーディングスタンダード CERT/Oracle 版](https://www.jpcert.or.jp/java-rules/)

ひしだまさんのページ
- [Java](http://www.ne.jp/asahi/hishidama/home/tech/java/index.html)
- [新機能メモ](http://www.ne.jp/asahi/hishidama/home/tech/java/uptodate.html)

きしだなおきさんの記事
- https://qiita.com/nowokay
- [Javaで最低限おさえておいてほしいクラス・インタフェース35 - 2024年版](https://nowokay.hatenablog.com/entry/2024/05/16/215353)

### 書籍のメモ

#### 付属のコード

- [Effective Java](https://github.com/jbloch/effective-java-3e-source-code)

### WEB+DBの記事

- 

### 特定の機能についてのページ

- モジュール：[モジュールシステムを学ぶ - Qiita](https://qiita.com/opengl-8080/items/93c8e0cf58654d5f73cb)、[【Java】モジュール](https://qiita.com/suema0331/items/121e23300527832cc117)
- [【Java】Serializableの実装、役割、使い方、危険性とその対策【serialVersionUIDとは】](https://debimate.jp/2021/02/20/【java】serializableの実装、役割、使い方、危険性とその対/)
- [Optionalクラスを意図されたとおりに使うための12のレシピ](https://blogs.oracle.com/otnjp/post/recipes-for-using-the-optional-class-as-its-meant-to-be-used-ja)

### 個人的メモ

- ほとんどのJavaコンパイラではpublicクラスのクラス名とファイル名を同じにしなくてはならない。大文字小文字が異なっていてもダメ。
- Stringの比較で==でも成功することがある([参考](https://qiita.com/awesam86/items/5d3461ecd4af30d88d71))
- TODO:要移動
  - [【入門】結局getter/setterは悪なのか](https://zenn.dev/kumackey/articles/c3acbd928d1d510268ab)
  - [結局のところgetter／setterは要るのか？要らないのか？](https://qiita.com/katolisa/items/6cfd1a2a87058678d646)
  - [継承は禁止するべき](https://anond.hatelabo.jp/20201022005749)
  - [オブジェクト指向は必要なのか](https://speakerdeck.com/kishida/is-object-oriented-needed)

### 疑問

- Spring BootのものをDockerで動かすには、tomcatが内蔵されてるからJDKを動かせばよい？
てことはhirameみたいにわざわざmaven wrapperを入れなくてもJDK動けば動かせるのでは? デバックモードのためにmaven使ってんのかな
- 古いJUnitの@Testと、新しい(jupiter)JUnitの@Testで、@Autowiredがうまくいかないのは、newしちゃうとDIしてくれなくなるのと関係あるのかな？
- SpringでMapperのテストをする時、例えばインサートのテストをしたいなら、インサート後にselectしたいわけだけどマッパー使うのは違うやん。どうすん？
- slf4jでログ出力する時、xmlにはルートとappLoggerにINFOで標準出力する様に設定してて、SOP用のクラスではappLoggerを指定したんだけど、すると各ログが同時に2つ出てた。なぜ？
- finalな変数は2重定義してもエラーにならない…? フィールドとローカル変数を作った時にならなかったのよね。
- th:actionとactionの違い
- actionで今のurlに送る方法
- mapperってメソッドの名前被ったらダメ？
- beanって名前被ってたり型が被っててもいいんだっけ
- mapperscanっていつ必要なん
- jsessionとは何で画面のものと何で違う
- 学生-座席-成績とかでアプリ作って技術検証用みたいなの作ってもいいんでね？
- Stringで＋が使えるのって何か仕組みなかったっけ
- インターセプターとaop
