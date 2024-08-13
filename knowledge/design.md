# 設計

- [設計](#設計)
  - [WebAPI](#webapi)
    - [WebAPIとは](#webapiとは)
    - [RPC](#rpc)
    - [REST](#rest)
      - [RESTとは](#restとは)
      - [RESTful](#restful)
      - [WebAPIとの違い](#webapiとの違い)
      - [RPCとREST](#rpcとrest)
  - [デザインパターン](#デザインパターン)
    - [Abstract FactoryとFactory Methodについて](#abstract-factoryとfactory-methodについて)
  - [外部リンク](#外部リンク)
  - [疑問](#疑問)

## WebAPI

### WebAPIとは

- HTTPまたはHTTPSによって通信を行う
- 特定のHTTPメソッドを用いてアクセスできる
- 特定のURIにおいて提供される
- URIのクエリパラメータやHTTPリクエストボディに一貫した呼び出し方の決まりがある
- HTTPレスポンスのヘッダやボディの行元方法に一定の決まりがある

(TODO:要出典)

### RPC

遠隔手続き呼び出し(Remote Procedure Call)。プログラムから別ホストにある関数の呼び出しをすること。

### REST

#### RESTとは

REpresentation State Trasfer。RESTfulであるAPI。ROAの実装そのもの。

#### RESTful

RESTの規則に従っていること。以下は例だけど、まあROAだよねという感じ。

- URIに対してメソッドを送ることでサービスを得る
- ステートレスなクライアント/サーバープロトコル
- リソースを一意に識別する
- XMLやJSONなどの構造化テキストを返す

#### WebAPIとの違い

URLに動詞が入ること、/apiや/jsonなどの規格、アーキテクチャが入ること、バージョンが入ることなど、URLはリソースの住所であるべきなのに、他のものが入るのはRESTではない。

REST風ということでREST-ishと言うこともある。

#### RPCとREST

RPCとは「何をするか」を指定する。オブジェクト指向的に言うと、ウェブサーバーを通して公開される静的なインスタンスをURLを通じて発見し、そのメソッドを呼ぶ。

[RPC と REST の違いはなんですか?](https://aws.amazon.com/jp/compare/the-difference-between-rpc-and-rest/)

## デザインパターン

### Abstract FactoryとFactory Methodについて

- Abstract Factory

  どう部品を生成するかは置いといて、複数の部品から製品を生成する、ということをインターフェースとサブクラスに分けた。

- Factory Method

  利用するインスタンスの生成をサブクラスに任せ、メインの処理だけ用意(ここはTemplate Method)する。

- したがって、Abstract Factoryはインスタンス生成をFactory MethodでやったりPrototypeでやったりする。

- そしたら、Factory MethodはAbstract Factoryである、と言えてしまいそう。
Factory MethodでありAbstract Factoryでない部分というのは、

## 外部リンク

## 疑問

- RESTならJSONプロパティはスネークらしいけどどこで決まってるの？
