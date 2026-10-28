# `flow_canvas`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`from_wf` / `from_dag` / `render` / `where`） |
| 处理器 | `flow_canvas` |

## 用途

工作流画布（蒸馏自 2026-09-28 主人给的周榜卡 Langflow 155.3k★，只取**可视化架构**，不引拖拽编辑器）：工作流定义 → 图（nodes/edges，数据只走引擎正规出口 `engine.list_workflows()`，R-H99b，不偷读 store/workflows.json）+ dag 运行账 → 运行图（带 done/failed 读数）→ **自包含 SVG 画布页**（零外链零脚本，离线可开可审计）落 outputs/flow-canvas/。**只画不跑**：执行仍走 wf_run/dagrun 的门，产物不掺页面登记面。op=from_wf/from_dag/render/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("flow_canvas")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show flow_canvas          # 本页内容的终端版
gbt-caps show flow_canvas --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("flow_canvas", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `from_wf`、`from_dag`、`render`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `flow_canvas`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
