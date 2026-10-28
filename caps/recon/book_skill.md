# `book_skill`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`plan` / `contract` / `extract` / `pack` / `budget` / `check` / `route`） |
| 处理器 | `book_skill` |

## 用途

**书→技能**（主人令 2026-10-16：把 book-to-skill 变成我们的原生能力）：蒸自 **virgiliojr94/book-to-skill**（MIT）—— 把任何技术书/文档集（PDF·EPUB·DOCX·MD·HTML·RTF·MOBI）变成**结构化技能、按需加载**：提取器（确定性）与生成器（spec 驴动）分开；产物五件（SKILL.md 心智模型+章节索引 · 章节文件按需加载 · 术语表 · 模式表 · 决策表）；**提结构不提摘要**，每条能指回章节:行；按需加载对比全文省 **24×–51×** token（对方实测，未复现）。我们刻意不同：只落**自己的托管目录**、必指出处、必回读验证。op=plan/contract/extract/pack/budget/check/route（**全只读·零作用域**）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("book_skill")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show book_skill          # 本页内容的终端版
gbt-caps show book_skill --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("book_skill", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `plan`、`contract`、`extract`、`pack`、`budget`、`check`、`route`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `book_skill`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
