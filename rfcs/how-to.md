# How to submit proposals

<!-- toc -->

## 提出までの流れ

1. `pulsate-dev/rfcs` リポジトリをフォークする

2. `proposal` ディレクトリにプロポーザルを追加し, PR を作成する
   - 基本的な構成などは [RFCs の書き方](#rfcs-の書き方) を参照してください.
   - ルートディレクトリにある `0000-template.md` をコピーして `proposal` ディレクトリに追加してください.

3. PR 内でプロジェクトチームとコミュニティとで提案に関する議論を行う
   - 他のコミュニティメンバーからのフィードバックを受けることをお勧めします.

## 提出する前に

以前に RFCs で却下された提案やロードマップに合わない提案, 実装することに見合わない提案はすぐに却下される可能性があります.

RFCs を提案する前に Discord などでユーザーや開発者など他のコミュニティメンバーあらのフィードバックを受けてから提案することをお勧めします.

## RFCs の書き方

### メタデータ

RFCs は以下のメタデータを持つ必要があります. これらは提案ファイルの Frontmatter に記述してください.

| メタデータ | 備考 | 必須かどうか |
| --- | --- | --- |
| 提案名 |  | ◯ |
| 提案日時 | YY-MM-DD の形式で記述する. | ◯ |
| 提案者署名 | `Name <email>` の形式で記述する. (有効なメールアドレスを持っていない場合は名前のみ) | ◯  |
| RFCs Tracking PR 番号 ( pulsate-dev/rfcs ) | `[#1](https://github.com/pulsate-dev/rfcs/pull/1)` の形式で記述する. | ◯ |
| RFCs Tracking Issue 番号 ( pulsate-dev/pulsate など) | 機能提案などの場合は記述する. `[#1](https://github.com/pulsate-dev/rfcs/pull/1)` の形式で記述する. | ✕ |

```markdown
----
- 提案名: 限定的な OAuth 認証のサポート
- 提案日時: 2024-06-26
- 提案者署名: `Sho Sakuma <me@m1sk9.dev>`
- RFCs Tracking PR: [#12](https://github.com/pulsate-dev/rfcs/pull/12)
----
```

### 構成

RFCs は以下の構成ではなければなりません.

| セクション | 要求される内容 | 必須かどうか |
| --- | --- | --- |
| Summary | RFCs の概要を簡潔にまとめる. | ◯ |
| Motivation | 提案の理由やモチベーション. | ◯ |
| Explanation | 提案の説明を Pulsate のユーザーに対して行うように記述する. | ◯ |
| Benefit | もし提案が承認されたとしてどのような恩恵があるのかどうか. | ◯ |
| Alternatives | 妥協案があれば記述する. | ✕ |
| Unresolved issue | 提案に存在している未解決の話題があれば記述する. | ✕ |
| References | 参考文献など. | ✕ |

### 雛形

```markdown
---
- 提案名: 
- 提案日時:
- 提案者署名:
- RFCs Tracking PR:
- RFCs Traching Issue:
---

# Summary

# Motivation

# Explanation

# Benefit

# Alternatives

# Unresolved issue

# References
```
