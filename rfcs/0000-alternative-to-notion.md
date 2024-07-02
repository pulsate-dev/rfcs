---
- 提案名: Notion の代替サービスを GitHub 管理に変更する
- 提案日時: 2024-07-02
- 提案者署名: Sho Sakuma <m1sk9@pulsate.dev>
- RFCs Tracking PR: [#6](https://github.com/pulsate-dev/rfcs/pull/6)
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

- Notion など外部に依存しないドキュメント管理が可能になる.
- Cloudflare Zero Trust は比較的自由度が高いため, アクセス制限を細かく設定できる.
  - 例: 外部の一部のメンバーにのみ閲覧権限を与える など.

# Alternatives

- 自前ホスト可能な Notion の OSS オルタナティブ [AppFlowy](https://appflowy.io/) を使用する.
  - ただし後述の [コスト](#unresolved-issue) はこの案でも発生するので一概にベストアンサーとは出来ない.

# Unresolved issue

- プライベートリポジトリ上での GitHub Actions 実行制限
  - デプロイなどに使用する.
  - Pulsate の GitHub Org は課金していないため, プライベートリポジトリの場合 実行制限が発生する.

# References

- [RFCs 0003: Notion の廃止](./0003-abolition-notion.md)
- [AppFlowy](https://appflowy.io/)
- [About billing for GitHub Actions - GitHub Docs](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions)
