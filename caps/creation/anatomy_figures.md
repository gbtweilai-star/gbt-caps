# `anatomy_figures`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`poster` / `drawing` / `detailed`） |
| 处理器 | `anatomy_figures` |

## 用途

Anatomy 等轴详解图（外部成熟件 · 主人 2026-10-19 指名抓取「这两个能力不就可以完美补齐缺失了吗」 · 上游 wheresryan22/anatomy · MIT · 15.9k★）：**把一个概念做成一台真机器**的等轴 SVG 图（零件级 40~150 件 · 四色明暗 · 画家排序 · 卡框带活读数）+ 可交互 HTML（悬停/键盘/巡览/WebGL 火水光焦散同一等轴相机）+ 会转的 3D 图（turn*.mjs 逐帧重投影 + 轨道审计）+ A4/Letter 三种版式 PDF（poster/drawing/detailed）。**几何自证** `--audit`（互不穿插/终端落在实处/无折/深度序）+ **线端自证** `lines.mjs`（line ends: 0）。本机依赖只三个：node≥20.10（现读 v24.15）、Chrome（标准位在）、无 npm 依赖无 postinstall；**零付费接口、零出网**（上游 publish.mjs 提 PR 那条不接）。op=status/examples/docs/where（纯读）· build/verify（写盘+起 node ⇒ filesystem_write 门在处理器层）。生成新图：模型按 SKILL.md+references/craft.md 写 examples/<名>/build.mjs → build → verify

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("anatomy_figures")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show anatomy_figures          # 本页内容的终端版
gbt-caps show anatomy_figures --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("anatomy_figures", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `poster`、`drawing`、`detailed`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `anatomy_figures`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
