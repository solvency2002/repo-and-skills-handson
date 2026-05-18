# ハンズオンカフェ: リポジトリ運用と Skills

SRWS-PSG ハンズオンカフェ (2026-06-24) 用のデモリポジトリです。

## このリポジトリの使い方

1. このリポジトリを **fork** または **clone** してください
2. ハンズオン中に `.gitignore` の編集、Issue 作成、Branch + PR の流れを体験します
3. `.claude/skills/` にある Skill を呼び出し、`SKILL.md` を書き換える演習を行います

## 構成

```
.
├── README.md              ← このファイル
├── SETUP.md               ← 事前準備の手順 (当日までに済ませる)
├── .gitignore             ← Part 1 で編集する (ビフォー状態)
├── .claude/
│   └── skills/
│       ├── check-handson-env/
│       │   └── SKILL.md   ← 環境チェック用 Skill (/check-handson-env)
│       └── humanizer-academic/
│           └── SKILL.md   ← Part 2 で description を書き換える演習用 Skill
└── draft.md               ← Skill の動作確認用サンプル文書
```

## 事前準備

詳細は **[SETUP.md](SETUP.md)** を参照してください。

clone したらまず Antigravity (または Claude Code / Codex) でこのフォルダを開き、AI にこう頼んでください:

```text
このリポジトリの check-handson-env スキルを使って、ハンズオンの事前準備を
チェックしてください。できていない項目があれば、その場でセットアップまで
進めてください。
```

→ GitHub 認証 / ブラウザ版 Claude / Zenodo Sandbox / AI ツール動作の4点を AI が順に確認し、足りなければセットアップ手順まで案内してくれます。
