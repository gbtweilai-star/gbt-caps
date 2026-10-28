# `bi_distill`

| 项目 | 值 |
|---|---|
| 域 | [`data`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`genoffice` / `datakit` / `record_grid`） |
| 处理器 | `bi_distill` |

## 用途

**蒸馏件**（不是外挂）：把吞入件 dataease/dataease（**GPL-3.0**〔README 徽章明写 GPL v3；GitHub 未识别才标 NOASSERTION〕· 24603星 · Java「人人可用的开源 BI 工具」）蒸成三条取法+一条红线：①拖拽即建模（先把数据做成可拖拽的字段模型，再谈图）②连接面如实列（「支持 X」= 真连得上；OLTP/OLAP/数仓/文件/API 五类照实登记，连不上如实说）③可分享是产品属性（分析产物必须能交出去，不留在自己盘里）④🔴**许可红线 GPL-3.0：只引用不复制**（复用其实现要先过 GPL）。op=source 现读胶囊尺寸+逐文件 sha256 · op=provenance 逐条指回原话（含**未蒸馏**一行：离线安装包/install.sh 不取）。**零作用域**。边界：接入端 ≡ 我们**已有**的 genoffice/datakit/record_grid；本位只蒸取法，**不建平行位**。op=method/source/provenance/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("bi_distill")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show bi_distill          # 本页内容的终端版
gbt-caps show bi_distill --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("bi_distill", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `genoffice`、`datakit`、`record_grid`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `data` · handler `bi_distill`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
