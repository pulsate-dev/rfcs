- 提案名: プロポーザルのメタデータを Frontmatter で管理しないようにする
- 提案日時: 2024-07-03
- 提案者署名: Sho Sakuma <m1sk9@pulsate.dev>
- RFCs Tracking PR: [#7](https://github.com/pulsate-dev/rfcs/pull/7)

# Summary

プロポーザルのメタデータ (提案名, 提案日時) などを Frontmatter で管理せず, 箇条書きで管理するように規定を修正する.

# Motivation

Frontmatter は内部的に YAML として解釈しますが, Pulsate RFCs プロセス上での Frontmatter の扱い方は YAML の形として成立していないことや, mdbook が Frontmatter に対して特殊な表示をするわけではないので, `RFCs Tracking PR` をハイパーリンクとして成立させるためにも Frontmatter は削除し, 箇条書きでの記述に変更する.

# Explanation

[提案のメタデータに関する規定](https://rfcs.pulsate.dev/how-to.html#メタデータ) にて Frontmatter での記述ではなく, 単なる箇条書きでの記述として規定します.

```markdown
- 提案名: 限定的な OAuth 認証のサポート
- 提案日時: 2024-06-26
- 提案者署名: `Sho Sakuma <me@m1sk9.dev>`
- RFCs Tracking PR: [#12](https://github.com/pulsate-dev/rfcs/pull/12)
```

# Benefit

- Frontmatter が不要になるため, プロポーザルの記述が簡略化される.
- YAML 形式ではなくなるため, GitHub 上のエラーが解消される.

# Alternatives

なし.

# Unresolved issue

なし.

# References

- [`rfcs-0003` - review](https://github.com/pulsate-dev/rfcs/pull/4/files#r1660572683)
