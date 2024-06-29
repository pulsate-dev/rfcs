---
- 提案名: Change JavaScript Runtime to Node.js
- 提案日時: 2024-01-20
- 提案者署名: laminne <laminne@pulsate.dev>
---

> [!NOTE]
>
> Pulsate RFCs プロセスが出来る前に提案された RFC です。この RFC は Pulsate RFCs プロセスに従っていません。また内容は古いものです.


# Summary

(少なくともCoreモジュールでの)Denoの使用をやめ、Node.js(またはBun)に移行する

# Motivation

1. ライブラリの数が少ない
サーバーサイドJS/TS界隈で多く使われているライブラリがDeno向けに書かれていないことが多い

npm:によってnpmで管理されているライブラリを使用することも可能ではあるが、動作するかの保証がなくまたDeno向けライブラリとの相性問題などもありそういった場合の対応に工数を割く必要がある

また、npmで管理されているライブラリを使用する事によって「Denoである意味」というのが薄れるのではないかという問題もある(これは個人の感想です)

2. Denoの不具合を踏んだ
これは他の処理系でも同じことが言えるかもしれないが、Deno fmtなどのビルトインツールの不具合でlintエラーが発生するような事象が発生した。
ビルトインツールではなくprettierやESLintを利用することによってこれらの不具合を避けることは可能ではあるが、hackyなうえにDenoを利用するメリットが失われてしまう懸念がある

3. renovateが正しく動作しない
依存関係の自動更新に使われるrenovateだが、Denoには正式に対応しておらず正規表現を利用した非公式な方法でしか動作しない。
当プロジェクトでも既に設定されているが、正常に動作していないように見える。

4. IDEのコード補完プラグインが正常に動作しない
JetBrainsのIDEにはVSC版のDenoプラグインをフォークしたプラグインがあるが、現在プロジェクトで使用されているImportMapに対応しておらず、コードジャンプなどが使用できない不具合が発生している。
また、VSC版のプラグインでも不具合(詳細は不明であるが)が発生するとの報告もある。

# Explanation

- Mikuroさいな:
  - Node.js + pnpm + Vite (vitest) への移行でよいと思う. Bun はまだ不安定かつ機能不全.
- aqyuki:
  > Mikuroさいな: Node.js + pnpm + Vite (vitest) への移行でよいと思う. Bun はまだ不安定かつ機能不全.
  - 僕もコレでいいと思う。ただ、asdf・mise・nvmなど何らかの方法でNodeのバージョンを固定してほしい
- la:
  > aqyuki: ただ、asdf・mise・nvmなど何らかの方法でNodeのバージョンを固定してほしい
  - これは`package.json`の設定でパッケージマネージャー/nodeバージョンを固定できるのでそこまで問題にはならないと思います
  > aqyuki: Node.js + pnpm + Vite (vitest) への移行でよいと思う. Bun はまだ不安定かつ機能不全.
  - 同意見
- Mido:
  > Mikuroさいな: Node.js + pnpm + Vite (vitest) への移行でよいと思う. Bun はまだ不安定かつ機能不全.
  - いいと思います
  > la: これは`package.json`の設定でパッケージマネージャー/nodeバージョンを固定できるのでそこまで問題にはならないと思います
  - 主なNode.jsバージョンマネージャーはNode.jsバージョンの取得に.node-versionもしくは.nvmrcを使用していることが多い ([nvm](https://github.com/nvm-sh/nvm#nvmrc), [nodenv](https://github.com/nodenv/nodenv#choosing-the-node-version), [fnm](https://github.com/Schniz/fnm#shell-setup), [asdf-nodejs](https://github.com/asdf-vm/asdf-nodejs#nvmrc-and-node-version-support)) ため、`package.json`のみでは不十分だと思います
- Meru:
  > Mikuroさいな: Node.js + pnpm + Vite (vitest) への移行でよいと思う. Bun はまだ不安定かつ機能不全.
  - 大方賛成です.
  - 限界開発鯖のメンバーがちょろっと話していたのは Yarn v4 がキャッシュのアルゴリズムが  pnpm よりも改善されていて pnpm に匹敵するようなのでもし差し支えなければ Yarn v4 も検討したいと思っています.  npm や Yarn v1 や v2 (Berry) などは提案する気ないので大丈夫です.
    - Yarn Plugin が標準で同梱している
    - lockfile の検証をセキュアに行ってくれる など
  > aqyuki: 僕もコレでいいと思う。ただ、asdf・mise・nvmなど何らかの方法でNodeのバージョンを固定してほしい
  - Node.js バージョンの固定には賛成です. 提案されているツールについては Volta を提案します.
  > la: これは`package.json`の設定でパッケージマネージャー/nodeバージョンを固定できるのでそこまで問題にはならないと思います
  - `engines` プロパティのことを言っているのだと思いますが, あれは実行環境の Node.js バージョンが古かったときの実行を禁止するだけで, バージョン自体の管理機能はないです.
- aqyuki:
  - Voltaで良さそう
- la: yarn v4に関しては詳しく調査する必要はありそう

# Benefit

開発体験の向上による外部コントリビューター獲得の難易度の低下, 開発スピードの向上, 自動化によるメンテナンスの合理化

- npmのパッケージがそのまま利用可能になる
- フォーマッタの選定などが容易になる
- 多くのIDEでプラグインなしでサポートされているため、環境構築が容易
- Renovateによるパッケージ自動更新

# Unresolved issue

- 現在使用しているライブラリの再選定
- 設定の書き直し
- DenoのAPIに依存している部分の再実装
- インポートの書き直し
- 開発者向け資料の書き直し
