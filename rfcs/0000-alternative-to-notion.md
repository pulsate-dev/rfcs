---
- 提案名: Notion の代替サービスを GitHub 管理に変更する
- 提案日時: 2024-07-02
- 提案者署名: Sho Sakuma <m1sk9@pulsate.dev>
- RFCs Tracking PR: <!-- この提案を追跡するための PR のリンク (後で追加) -->
- RFCs Traching Issue: <!-- この提案を追跡するための Issue のリンク (オプション) -->
---


# Summary

Notion の代替先として rust-lang/mdbook, GitHub Pages を使った GitHub での管理を提案します.

# Motivation

[`rfc-0003`](./0003-abolition-notion.md) で Notion の廃止が決まったが, Unresolved issues として **既存の Notion のドキュメントをどのように扱うか** が未解決のため, この RFCs で解決を図ります.

# Explanation

この提案は Notion の代替先として rust-lang/mdbook, GitHub Pages を使った GitHub での管理を提案します.

開発系のドキュメントはすでに [dev-guide](https://dev-guide.pulsate.dev) への移行が始まっているため, それに倣い Notion のドキュメントも GitHub で管理することで統一性を持たせたい意図があります.

チーム専用のドキュメントとなるため, 透明化という観点からは離れますが, プライベートリポジトリとして管理しアクセス制限は Cloudflare Zero Trust で行います.

- rust-lang/mdbook: ドキュメントのビルドに使用. Rust 製のドキュメントジェネレータ. Rust 内でも広く使われている.
  - [The Rust Programming Language](https://doc.rust-jp.rs/book-ja/)

# Benefit
<!-- この提案のメリット -->

# Alternatives
<!-- この提案の代替案 (オプション) -->

# Unresolved issue
<!-- 未解決の問題点 (オプション) -->

# References
<!-- 参考文献 (オプション) -->
