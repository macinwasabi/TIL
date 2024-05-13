# SQL

- [SQL](#sql)
  - [総括的なページ](#総括的なページ)
  - [特定の機能についてのページ](#特定の機能についてのページ)
  - [個人的メモ](#個人的メモ)
    - [INNER JOINとOUTTER JOIN](#inner-joinとoutter-join)
      - [INNER JOIN(=JOIN)](#inner-joinjoin)
      - [OUTER JOIN](#outer-join)
    - [悲観ロックと楽観ロック](#悲観ロックと楽観ロック)
  - [外部リンク](#外部リンク)

## 総括的なページ

## 特定の機能についてのページ

- [30分で理解するORACLE MASTER](https://www.oracle.com/jp/a/tech/docs/technical-resources/120814-30mins-om.pdf)

## 個人的メモ

### INNER JOINとOUTTER JOIN

どちらも、結合先に合わせて結合元が複製される。

#### INNER JOIN(=JOIN)

結合先が無ければ、結合元も無くなる。

#### OUTER JOIN

片方のテーブルに結合するものが無くても、nullにして結合してくれる。

- 結合元が結合先に無くても表示するが左外部結合(LEFT JOIN=LEFT OUTER JOIN)
- 結合先にあるものが結合元に無くても表示するのが右外部結合(RIGHT JOIN=RIGHT OUTER JOIN)
- 両方を行うのがFULL JOIN=FULL OUTER JOIN。

### 悲観ロックと楽観ロック

- 楽観ロック：めったに同時更新は起きない、という楽観的な前提の排他制御。データにロックは行わず、更新対象が取得時と同じであることを確認してから更新する。バージョン、更新日時(コンマ秒の問題はあるが)などのロックキーを確認するなど。
- 悲観ロック：頻繁に同じデータに変更を加える、という悲観的な前提の排他制御。データにロックを行う。

## 外部リンク

- [排他制御（楽観ロック・悲観ロック）の基礎 - Qiita](https://qiita.com/NagaokaKenichi/items/73040df85b7bd4e9ecfc)
