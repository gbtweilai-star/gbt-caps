# `diagram_distill`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`method` / `source` / `provenance` / `where`） |
| 处理器 | `diagram_distill` |

## 用途

**蒸馏件**（不是外挂）：把吞入件 wheresryan22/anatomy（MIT · 7551★ · 零依赖 Node）的 **craft 取法**提炼成我们自己的**概念物化图判据**：①概念物化（先把抽象概念发明成一个「它怎么转就是这个概念」的物理机构）②单一数源（图上每个数来自同一个驱动模型的读数）③几何不变量要有审计（不穿模，静止/拆解/过渡每一帧都查）④逐关节自检（交付前自己放大挨个关节看）。op=source 现读胶囊（尺寸+逐文件 sha256）· op=provenance 逐条指回原话（含**未蒸馏**两行：33 figures 画廊/WebGL/3D 引擎不取 · npx 安装不取）。**零作用域**：无 subprocess / 无 urllib / 无写盘。边界：接入端 ≡ 我们**已有**的出图位（code_art / scene_anchor / projection_card）；本位只蒸取法，**不建平行位**。op=method/source/provenance/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("diagram_distill")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show diagram_distill          # 本页内容的终端版
gbt-caps show diagram_distill --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("diagram_distill", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `method`、`source`、`provenance`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `diagram_distill`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
