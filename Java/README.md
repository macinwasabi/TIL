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

#### [Spring](./spring.md)

#### Seasar2

#### JUnit

- [JUnit 5 ユーザーガイド](https://oohira.github.io/junit5-doc-jp/user-guide/#overview)

## POJO

POJO(Plain Old Java Object:普通のJava)について。

### 総括的なページ

ひしだまさんのページ
- [Java](http://www.ne.jp/asahi/hishidama/home/tech/java/index.html)
- [新機能メモ](http://www.ne.jp/asahi/hishidama/home/tech/java/uptodate.html)

### WEB+DBの記事

- 

### 特定の機能についてのページ

- モジュール：[モジュールシステムを学ぶ - Qiita](https://qiita.com/opengl-8080/items/93c8e0cf58654d5f73cb)、[【Java】モジュール](https://qiita.com/suema0331/items/121e23300527832cc117)
- [【Java】Serializableの実装、役割、使い方、危険性とその対策【serialVersionUIDとは】](https://debimate.jp/2021/02/20/【java】serializableの実装、役割、使い方、危険性とその対/)

### 個人的メモ

- ほとんどのJavaコンパイラではpublicクラスのクラス名とファイル名を同じにしなくてはならない。大文字小文字が異なっていてもダメ。

### 疑問

- - Spring BootのものをDockerで動かすには、tomcatが内蔵されてるからJDKを動かせばよい？
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
