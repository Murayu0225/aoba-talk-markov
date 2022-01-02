## Text Generator (from LINE TALK)
**The beginning of Botchan's talk in the sample is in talk.txt. In the production environment, please enter the other party's talk here and use it.**

This is a text generator that uses Mecab to contextualize my past LINE talks with ****, and generates new sentences that she might talk about using Markov.

### How it works?
[ ] is a branch.

Enter the text that **** typed in `talk.txt`.[add/***]<br/>
↓<br/>
Merge to [develop] branch.<br/>
↓<br/>
Run `Mecab`.(contextual analysis)[develop] {GitHub Action}<br/>
↓<br/>
Run `Make Dictionary`.(dictionary generation)[develop] {GitHub Action}<br/>
↓<br/>
Merge into [main] branch.<br/>
↓<br/>
Build by `heroku`.<br/>
↓<br/>
Reflect LINE Bot.

The webhook destination is [https://aoba-s.murayu.com/sample](https://aoba-s.murayu.com/sample).

### How to test
- The LINE account is not open to the public. If you want to build it, please link heroku with the cloned repository to make it work. You can refer to [this article](https://qiita.com/shimajiri/items/cf7ccf69d184fdb2fb26) for more details.

### About Issue and PR
- Issue and PR are always welcome. If you have any concerns, please post them.

### If you have any problems
- If you need any help, please send a DM to the developer's Twitter account([@yuuuuu_mmmmu](https://twitter.com/yuuuuu_mmmmu)). I will respond as soon as possible.

### Documentation
- [Messaging API Reference](https://developers.line.biz/en/reference/messaging-api/)
- [LINE Messaging API SDK for Python](https://github.com/line/line-bot-sdk-python)

### License
[MIT license](./LICENSE).

---

## Text Generator (from LINE TALK)
**サンプルで坊っちゃんの冒頭がtalk.txtに入ってます。本番環境では、ここに相手のトークを入力して利用してください。**

****との過去のLINEトークをMecabで文脈解析。Markovを使って **** が話しそうな新たな文章を生成します。

### 仕組み

[ ]内は、ブランチ

`talk.txt`に **** が打った文章を入力[add/***]<br/>
↓<br/>
[develop]ブランチにマージ<br/>
↓<br/>
`Mecab`を走らせる(文脈解析)[develop] {**GitHub Action**}<br/>
↓<br/>
`Make Dictionary`を走らせる(辞書生成)[develop] {**GitHub Action**}<br/>
↓<br/>
[main]ブランチにマージ<br/>
↓<br/>
herokuによるビルド<br/>
↓<br/>
LINE Bot反映

Webhook先については、[https://aoba-s.murayu.com/sample](https://aoba-s.murayu.com/sample)になってます。

### テスト方法
- LINEアカウントの公開は行っておりません。ビルドする場合には、herokuとクローンしたリポジトリを連携させて動作させてください。herokuとLINE Botの連携方法は、[この記事](https://qiita.com/shimajiri/items/cf7ccf69d184fdb2fb26)を参照にすると良いです。

### Issue·PRについて
- いつでも受け付けています。気になったことがあれば投稿してください。

### 困ったら
- もし何かあれば、開発者のTwitterアカウント([@yuuuuu_mmmmu](https://twitter.com/yuuuuu_mmmmu))までDMを送ってください。可能な限り早く対応します。

### ドキュメント
- [Messaging APIリファレンス](https://developers.line.biz/ja/reference/messaging-api/)
- [LINE Messaging API SDK for Python](https://github.com/line/line-bot-sdk-python)

### ライセンス
[MITライセンス](./LICENSE)を利用。
