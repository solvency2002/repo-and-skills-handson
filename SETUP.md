# 事前準備: SRWS-PSG ハンズオンカフェ — リポジトリ運用とSkills

> **当日までにこの1枚に書かれたセットアップを済ませてください。**

- **開催日**: 2026-06-24 (水) 17:30〜18:30 (60分)
- **形式**: オンライン・ハンズオン (各自PC持参)
- **講師**: youkiti (SRWS-PSG)

---

## 事前準備の進め方

**やることは1つだけ**: このリポジトリを clone し、AI に「`check-handson-env` スキルを使って、足りないところはセットアップして」と頼む。

### Step 1: リポジトリを clone

```
https://github.com/youkiti/repo-and-skills-handson
```

### Step 2: Antigravity (または Claude Code / Codex) でフォルダを開く

### Step 3: AI にこう頼む

```text
このリポジトリの check-handson-env スキルを使って、ハンズオンの事前準備を
チェックしてください。できていない項目があれば、その場でセットアップまで
進めてください。
```

→ AI が以下を順番に確認し、足りないものは具体的な手順 (インストールコマンド・ログイン手順) を案内してくれます。

1. **GitHub に push できる** (`gh auth status` / リポジトリの有無)
2. **ブラウザ版 Claude にログインできる** (https://claude.ai/)
3. **Zenodo Sandbox にログインできる** (https://sandbox.zenodo.org/ — ⚠️ 本番ではなく Sandbox)
4. **AI コーディングツールが動いている** (Antigravity / Claude Code / Codex のいずれか)

すべて ✅ になったら準備完了です。

---

## 補足

- 前回ハンズオンカフェ「Writing with AI」(2026-05-13) の配布資料・スライドにも目を通しておくと、当日 Part 2 で出てくる「ポン出し / 部分修正 / 手で修正」の3段が理解しやすくなります
- ⚠️ Zenodo は **必ず Sandbox** (https://sandbox.zenodo.org/) を使ってください。本番は取り消し不可です

---

*本資料は事前準備のみを対象としています。当日の手順・コマンド集はスライド・WS中に共有します。*
