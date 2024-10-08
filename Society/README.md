# 社会

税金や制度や会社についてなど、社会的な部分をまとめる。

- [社会](#社会)
  - [給与所得と税金など](#給与所得と税金など)
    - [月収や手取りの違い](#月収や手取りの違い)
    - [給与所得](#給与所得)
      - [給与所得控除](#給与所得控除)
    - [税金の種類](#税金の種類)
    - [所得税](#所得税)
      - [収入から所得税額などの計算](#収入から所得税額などの計算)
      - [課税所得金額(所得税)](#課税所得金額所得税)
      - [所得控除(所得税)](#所得控除所得税)
      - [医療費控除](#医療費控除)
      - [社会保険料控除](#社会保険料控除)
      - [生命保険料控除](#生命保険料控除)
      - [地震保険料控除](#地震保険料控除)
      - [寄附金控除](#寄附金控除)
      - [配偶者控除](#配偶者控除)
      - [配偶者特別控除](#配偶者特別控除)
      - [扶養控除](#扶養控除)
      - [基礎控除](#基礎控除)
    - [住民税](#住民税)
      - [収入から住民税額などの計算](#収入から住民税額などの計算)
    - [ふるさと納税](#ふるさと納税)
      - [疑問](#疑問)
    - [年金](#年金)

## 給与所得と税金など

### 月収や手取りの違い

| 名称   | 内訳                        | 備考                                             |
| ------ | --------------------------- | ------------------------------------------------ |
| 月給   | 基本給+固定給               | 固定給=毎月一定額が支払われる手当                |
| 月収   | 月給+変動手当               | 額面=月収。変動手当=月によって金額が変わる手当。 |
| 手取り | 月収-(税金・社会保険料など) |                                                  |

参考：[doda](https://doda.jp/guide/money/036.html)

### 給与所得

給与所得=収入-給与所得控除

なお、給与等の収入金額が600万円未満の場合には[所得税法別表第五(年末調整等のための給与所得控除後の給与等の金額の表)](https://laws.e-gov.go.jp/law/340AC0000000033/#Mpat_5)で給与所得が決まる。

※年金と給与所得があると所得金額調整控除がかかる。

参考：

- [給与所得 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1400.htm)
- [所得金額調整控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1411.htm)

#### 給与所得控除

給与等の収入金額に応じて決まる控除。前述の通り、給与等の収入金額が600万円未満の場合には別表で給与所得が決まる。

600万円を超えた場合には計算式がある。

参考：[給与所得控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1410.htm)

### 税金の種類

給与に関係する税金は主に以下のものがありそう。

- 所得税
- 住民税・県民税

※所得税と住民税で、配偶者控除などの同じ名前のものが出てくるが、控除額や控除の条件が違ったりするので注意。

### 所得税

#### 収入から所得税額などの計算

- 所得金額=収入金額-(収入から差し引かれる金額)
- 課税所得金額=所得金額-所得控除額
- 所得税額=課税所得額*所得税率
- 基準所得税額=所得税額-(所得税額から差し引かれる金額)
- 復興特別所得税額=基準所得税額*2.1%
- 所得税等の申告納税額=基準所得税額+復興特別所得税額-(源泉徴収税額など)

一部の解説。その他は各見出しを参照。

- 収入から差し引かれる金額：給与所得の場合、収入から引く給与所得控除のことだと思われる。
- 所得税額から差し引かれる金額：令和6年の定額減税額、
- 源泉徴収税額：TODO

#### 課税所得金額(所得税)

| 課税される所得金額                 | 税率 | 控除額      |
| ---------------------------------- | ---- | ----------- |
| 1,000円 から 1,949,000円まで       | 5%   | 0円         |
| 1,950,000円 から 3,299,000円まで   | 10%  | 97,500円    |
| 3,300,000円 から 6,949,000円まで   | 20%  | 427,500円   |
| 6,950,000円 から 8,999,000円まで   | 23%  | 636,000円   |
| 9,000,000円 から 17,999,000円まで  | 33%  | 1,536,000円 |
| 18,000,000円 から 39,999,000円まで | 40%  | 2,796,000円 |
| 40,000,000円 以上                  | 45%  | 4,796,000円 |

<details>

<summary>本来の計算式</summary>

上記は本来の計算式ではなく、本来のものを簡単に計算できるようにしたもの。

本来は累進課税なので、例えば500万円だとすると、

```text
所得税額=195*0.05+135*0.1+170*0.2=9.75+13.5+34=57.25
```

となる。先ほどの表の計算について考えると、

```text
所得税額=500*0.2-42.75=(195+135+170)*0.2-(29.25+13.5)
=(195*0.2-195*0.15)+(135*0.2-135*0.1)+170*0.2
=195*(0.2-0.15)+135*(0.2-0.1)+170*0.2
=195*0.05+135*0.1+170*0.2
```

となる。要は控除額の部分でうまいこと調整することで簡単に計算できるようにしている。

</details>

参考：

- [所得税の税率 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm)
- [所得税のしくみ - 国税庁](https://www.nta.go.jp/publication/pamph/koho/kurashi/html/01_1.htm)

#### 所得控除(所得税)

簡単に以下の控除が出てきそう。

- 医療費控除：自己または自己と生計を一にする配偶者やその他の親族のために支払った医療費が一定額を超えるとき
- 社会保険料控除：自己または自己と生計を一にする配偶者やその他の親族の負担すべき社会保険料を支払ったとき
- 生命保険料控除：納税者が生命保険料、介護医療保険料および個人年金保険料を支払ったとき
- 地震保険料控除：納税者が特定の損害保険契約等に係る地震等損害部分の保険料または掛金を支払ったとき
- 寄附金控除：納税者が国や地方公共団体、特定公益増進法人などに対し、「特定寄附金」を支出したとき
- 配偶者控除：納税者に所得税法上の控除対象配偶者がいるとき
- 配偶者特別控除：配偶者に48万円を超える所得があるため配偶者控除の適用が受けられないときの、配偶者の所得金額に応じた控除
- 扶養控除：納税者に所得税法上の控除対象扶養親族となる人がいる
- 基礎控除：納税者本人の合計所得金額に応じた控除

参考：[所得控除のあらまし - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1100.htm)

#### 医療費控除

医療費控除額=(実際に支払った医療費の合計額)-(1)-(2)

- (1)：保険金などで補てんされる金額
  - 例：生命保険契約などで支給される入院費給付金や、健康保険などで支給される高額療養費・家族療養費・出産育児一時金など
- (2)：10万円
  - その年の総所得金額等が200万円未満の人は、総所得金額等の5パーセントの金額

※セルフメディケーション税制

特定一般用医薬品等購入費を支払った場合に、健康の保持増進および疾病の予防への取組として一定の健康診査や予防接種などを行っているときは、通常の医療費控除との選択により、特定一般用医薬品等購入費の一部を控除できる。

つまり、医療費が10万円を超えなくても、体の不調などでOTC医薬品をよく利用する人に控除がある。

対象商品には「セルフメディケーション税控除対象」のマークが記載されている。

参考：

- [医療費を支払ったとき（医療費控除） - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1120.htm)
- [セルフメディケーション税制とは？ - 第一三共ヘルスケア](https://www.daiichisankyo-hc.co.jp/health/knowledge/self_taxsystem/)

#### 社会保険料控除

社会保険料控除=実際に支払った金額または給与などから差し引かれた金額の全額

- 簡単に以下が対象になる。

  1. 健康保険、国民年金、厚生年金保険で被保険者として負担するもの
  2. 国民健康保険の保険料または国民健康保険税
  3. 雇用保険の被保険者として負担する労働保険料
  4. 国民年金基金の加入員として負担する掛金

参考：[社会保険料控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1130.htm)

#### 生命保険料控除

以下は平成24年1月1日以降の新契約を前提とする。

- 新生命保険料控除：最高4万円
- 介護医療保険料控除：最高4万円
- 新個人年金保険料控除：最高4万円

上記のそれぞれに対して、以下の計算式で控除額が決まる。

| 年間の支払保険料等       | 控除額                    |
| ------------------------ | ------------------------- |
| 20,000円以下             | 支払保険料等の全額        |
| 20,000円超、40,000円以下 | 支払保険料等*1/2+10,000円 |
| 40,000円超、80,000円以下 | 支払保険料等×1/4+20,000円 |
| 80,000円超               | 一律40,000円              |

参考：[生命保険料控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1140.htm)

#### 地震保険料控除

| 区分                | 年間の支払保険料の合計   | 控除額                                                       |
| ------------------- | ------------------------ | ------------------------------------------------------------ |
| (1)地震保険料       | 50,000円以下             | 支払金額の全額                                               |
| (1)                 | 50,000円超               | 一律50,000円                                                 |
| (2)旧長期損害保険料 | 10,000円以下             | 支払金額の全額                                               |
| (2)                 | 10,000円超、20,000円以下 | 支払金額×1/2＋5,000円                                        |
| (2)                 | 20,000円超               | 15,000円                                                     |
| (1)と(2)の両方      | -                        | (1)、(2)それぞれの方法で計算した金額の合計額（最高50,000円） |

参考：[地震保険料控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1145.htm)

#### 寄附金控除

寄付金控除額=(1.または2.のいずれか低い金額)-2000円

1. その年に支出した特定寄附金の額の合計額
2. その年の総所得金額等の40パーセント相当額

- 特定寄付金には簡単に以下がある

  1. 国、地方公共団体に対する寄附金
  2. 公益社団法人、公益財団法人その他公益を目的とする事業を行う法人または団体に対する寄附金のうち、要件を満たすと認められるものとして財務大臣が指定したもの
  3. 所得税法別表第一に掲げる法人その他特別の法律により設立された法人のうち、教育または科学の振興、文化の向上、社会福祉への貢献その他公益の増進に著しく寄与するものとしてうんぬん
  4. 特定公益信託のうち、その目的が教育または科学の振興、文化の向上、社会福祉への貢献その他公益の増進に著しく寄与する一定のものの信託財産とするために支出した金銭
  5. 認定特定非営利法人等に対する寄附金のうち一定のもの
  6. 特定新規中小会社により発行される特定新規株式を払込みにより取得した場合の特定新規株式の取得に要した金額のうち一定の金額（800万円を限度)

※学校の入学に関してするもの、寄附をした人に特別の利益がおよぶと認められるものは該当しない

ふるさと納税の所得税に関する部分はこれに当たる。

参考：[一定の寄附金を支払ったとき(寄附金控除) - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1150.htm)

#### 配偶者控除

以下は控除対象配偶者が70歳未満を前提とする。
控除を受ける納税者本人の合計所得金額によって以下の通りとなる。

| 合計所得金額           | 控除額 |
| ---------------------- | ------ |
| 900万円以下            | 38万円 |
| 900万円超950万円以下   | 26万円 |
| 950万円超1,000万円以下 | 13万円 |

- 控除対象配偶者となる人の範囲

  以下の4つの要件のすべてに当てはまること。

  1. 民法の規定による配偶者であること
  2. 納税者と生計を一にしていること
  3. 年間の合計所得金額が48万円以下であること(給与のみの場合は給与収入が103万円以下)
  4. 青色申告者の事業専従者としてその年を通じて一度も給与の支払を受けていないことまたは白色申告者の事業専従者でないこと

参考：[配偶者控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1191.htm)

#### 配偶者特別控除

横軸が控除を受ける納税者本人の合計所得金額、縦軸が配偶者の合計所得金額。

|                        | 900万円以下 | 900万円超、950万円以下 | 950万円超、1,000万円以下 |
| ---------------------- | ----------- | ---------------------- | ------------------------ |
| 48万円超、95万円以下   | 38万円      | 26万円                 | 13万円                   |
| 95万円超、100万円以下  | 36万円      | 24万円                 | 12万円                   |
| 100万円超、105万円以下 | 31万円      | 21万円                 | 11万円                   |
| 105万円超、110万円以下 | 26万円      | 18万円                 | 9万円                    |
| 110万円超、115万円以下 | 21万円      | 14万円                 | 7万円                    |
| 115万円超、120万円以下 | 16万円      | 11万円                 | 6万円                    |
| 120万円超、125万円以下 | 11万円      | 8万円                  | 4万円                    |
| 125万円超、130万円以下 | 6万円       | 4万円                  | 2万円                    |
| 130万円超、133万円以下 | 3万円       | 2万円                  | 1万円                    |

- 配偶者特別控除を受けるための要件

  1. 控除を受ける納税者本人のその年における合計所得金額が1,000万円以下であること
  2. 配偶者が、次の要件すべてに当てはまること
     1. 民法の規定による配偶者であること
     2. 控除を受ける人と生計を一にしていること
     3. その年に青色申告者の事業専従者としての給与の支払を受けていないことまたは白色申告者の事業専従者でないこと
     4. 年間の合計所得金額が48万円超133万円以下であること
  3. 配偶者が、配偶者特別控除を適用していないこと
  4. 配偶者が、給与所得者の扶養控除等申告書または従たる給与についての扶養控除等申告書に記載された源泉控除対象配偶者がある居住者として、源泉徴収されていないこと（配偶者が年末調整や確定申告で配偶者特別控除の適用を受けなかった場合等を除きます）
  5. 配偶者が、公的年金等の受給者の扶養親族等申告書に記載された源泉控除対象配偶者がある居住者として、源泉徴収されていないこと（配偶者が年末調整や確定申告で配偶者特別控除の適用を受けなかった場合等を除きます）

参考：[配偶者特別控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1195.htm)

#### 扶養控除

| 区分                              | 控除額 |
| --------------------------------- | ------ |
| 一般の控除対象扶養親族            | 38万円 |
| 特定扶養親族                      | 63万円 |
| 老人扶養親族-同居老親等以外のもの | 48万円 |
| 老人扶養親族-同居老親等           | 58万円 |

- 扶養親族に該当する人の範囲

  1. 配偶者以外の親族(6親等内の血族および3親等内の姻族)または都道府県知事から養育を委託された児童(里子)や市町村長から養護を委託された老人であること
  2. 納税者と生計を一にしていること
  3. 年間の合計所得金額が48万円以下であること(給与のみの場合は給与収入が103万円以下)
  4. 青色申告者の事業専従者としてその年を通じて一度も給与の支払を受けていないことまたは白色申告者の事業専従者でないこと

- 控除対象扶養親族に該当する人の範囲

  1. 扶養親族のうち、その年12月31日現在の年齢が16歳以上の人
  2. 非居住者である扶養親族については、次に掲げるいずれかに該当する人に限り、控除対象扶養親族に該当します
     1. その年12月31日現在の年齢が16歳以上30歳未満の人
     2. その年12月31日現在の年齢が70歳以上の人
     3. その年12月31日現在の年齢が30歳以上70歳未満の人であって次に掲げるいずれかに該当する人
        1. 留学により国内に住所および居所を有しなくなった人
        2. 障害者である人
        3. 納税者からその年において生活費または教育費に充てるための支払を38万円以上受けている人

参考：[扶養控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1180.htm)

#### 基礎控除

| 納税者本人の合計所得金額 | 控除額 |
| ------------------------ | ------ |
| 2,400万円以下            | 48万円 |
| 2,400万円超2,450万円以下 | 32万円 |
| 2,450万円超2,500万円以下 | 16万円 |
| 2,500万円超              | 0円    |

参考：[基礎控除 - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm)

### 住民税

正確には個人住民税と呼ぶ。個人住民税は、都道府県と市町村が課する地方税、所得税は国が課する国税であるため、国税庁のページに住民税についての説明は無さそう。

[マイナポータル](https://myna.go.jp)から税を開くと、個人住民税額が確認できる。

控除の金額などの詳細な部分は各市町村区によって変わるかもしれないが、大体同じように見える。

均等割(所得にかかわらない税額)と所得割(前年の所得に応じた税額)の両方で住民税は徴収される。

参考：

- [個人住民税 - 総務省](https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/150790_06.html)

#### 収入から住民税額などの計算

以下はとある市町村の計算式。

- 課税総所得金額=総所得金額-所得控除合計
- 税額控除前所得割額=課税総所得金額*税率
- 所得割額=税額控除前所得割額-税額控除額
- 特別徴収税額=所得割額+均等割額+森林環境税
- 差引納付額=特別徴収税額-控除不足額

それぞれの意味。細かい金額などは各市町村で検索。

- 所得控除合計：所得控除の合計額
  - 医療費控除
  - 社会保険料控除
    - 生命保険料控除
    - 地震保険料控除
  - 配偶者控除
  - 配偶者特別控除
  - 基礎控除
- 税額控除額：税額控除の合計額
  - 調整控除
  - 配当控除
  - 住宅借入金など特別税額控除
  - 寄付金税額控除
  - 配当割額または株式等譲渡所得割額の控除
- 控除不足額：所得割額より控除ができなかった配当割額又は株式等譲渡所得割額

### ふるさと納税

- 所得税の控除は寄付金控除と同様
  - 参考のHPなどでは所得税額を掛けているが、所得税の控除額として見るか手取り等に対しての控除額として見るかの違いではなかろうか
- 個人住民税(基本分)：(ふるさと納税額-2,000円)*10%を税額控除
- 個人住民税(特例分)：(ふるさと納税額-2,000円)*(100%-10%-所得税率)
  - ①および②により控除できなかった額を、③により全額控除している。
  - 基本分も特例分も合わせた額が寄付金税額控除として引かれていそう。

- ワンストップ特例制度
  - 確定申告が不要な給与所得者等で、寄付する自治体の数が5団体以下などの条件を満たす場合、確定申告をせずに税額控除を受けられる制度のこと。
  - 利用した場合、所得税からの控除は行われず、所得税控除分も含めた控除額全額が翌年度の住民税減額という形で控除されます。

参考：

- [ふるさと納税(寄附金控除) - 国税庁](https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1155.htm)
- [ふるさと納税とは？仕組みやメリットをわかりやすく解説 - りそな銀行](https://www.resonabank.co.jp/kojin/column/credit/column_0006.html)
- [ふるさと納税ワンストップ特例制度 - ふるさと納税ポータルサイト](https://www.soumu.go.jp/main_sosiki/jichi_zeisei/czaisei/czaisei_seido/furusato/topics/20150401.html#block02)

#### 疑問

- ふるさと納税(寄付金控除)は実質負担2千円になっているのか？

所得税の部分

ふるさと納税額-2000円=ふるさと控除額とすると、
  
- ふるさと納税がない場合：

  ```text
  給与所得-所得控除=課税所得額
  ```

- ふるさと納税がある場合：

  ```text
  給与所得-(所得控除+ふるさと控除額)=課税所得額
  ```

- つまり：

  上記それぞれの課税所得額に対して、所得税率をかけたものが所得税額となり、引かれる。そのため、

  ```text
  (ふるさと納税がある場合の所得税額)-(ふるさと納税がない場合の所得税額)
  =-(ふるさと控除額*所得税額)
  ```

  が、ふるさと納税がある場合の所得税額の差分となり、`ふるさと控除額*所得税額`だけ得をしていることがわかる。

### 年金

TODO
