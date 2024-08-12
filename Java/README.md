# Java

- [Java](#java)
    - [個人的メモ](#個人的メモ)
    - [疑問](#疑問)

### 個人的メモ

- ほとんどのJavaコンパイラではpublicクラスのクラス名とファイル名を同じにしなくてはならない。大文字小文字が異なっていてもダメ。
- Stringの比較で==でも成功することがある([参考](https://qiita.com/awesam86/items/5d3461ecd4af30d88d71))

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
