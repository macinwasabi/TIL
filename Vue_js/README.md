# Vue.js

- [Vue.js](#vuejs)
  - [総括的なページ](#総括的なページ)
  - [WEB+DBの記事](#webdbの記事)
  - [特定の機能についてのページ](#特定の機能についてのページ)
  - [個人的メモ](#個人的メモ)
    - [疑問](#疑問)

## 総括的なページ

- [公式ドキュメント](https://ja.vuejs.org/guide/introduction.html)
- [公式チュートリアル](https://ja.vuejs.org/tutorial/#step-1)

## WEB+DBの記事

- Vol.101 連載 どんとこい!フロントエンド開発/3Vue.jsでお手軽UI構築......シンプルに始められて大規模にも対応!
- Vol.112 特集1 React/Vue.jsで実践!コンポーネント設計 樋口 剛
- Vol.120 特集2 最新Vue.js 3入門

## 特定の機能についてのページ

## 個人的メモ

### 疑問

- 「WEB+DB Vol.120 最新Vue.js 3入門」の2章「入力フォームと追加ボタンを実装」の「入力フォームを実装」で思ったこと。リアクティブ機能って変数にref()で包んだものを渡すことでvalueが変更されても追跡できる、と思ってた。v-modelを使ってるだけでも同じ機能が得られてるのは、v-modelを使うことで裏ではinputValueにref('')が格納されてるってこと？
  - 以下に答えがあるのでTODO:要確認。
  - [コンポーネントの v-model](https://ja.vuejs.org/guide/components/v-model.html)
