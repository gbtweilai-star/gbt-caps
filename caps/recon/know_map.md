# `know_map`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `layers` / `tour` / `ask` / `impact`） |
| 处理器 | `know_map` |

## 用途

**理解任何事**（主人令 2026-10-15 蒸馏自 GitHub Trending #1 「Understand Anything」）：把任何仓/库/文档变成一张**可点、可搜、可问的分层知识图**。三步：scan（走盘+找入口）→ build（三层建图，**每条边带 evidence = path:line**）→ 四功能 tour（引导导览）·ask（词面检索，不冒充语义）·impact（变更影响）·layers（分层视图）。op=status/layers/tour/ask/impact（只读）· scan/build（build 写 state/know_map）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("know_map")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show know_map          # 本页内容的终端版
gbt-caps show know_map --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("know_map", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`layers`、`tour`、`ask`、`impact`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `know_map`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
