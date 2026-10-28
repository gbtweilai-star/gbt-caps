# `review_gate`

| 项目 | 值 |
|---|---|
| 域 | [`security`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`lr_submit` / `lr_tick` / `handoff`） |
| 处理器 | `review_gate` |

## 用途

独立终审位（C-15「验收方 ≠ 产出方」的最小实现 · 2026-10-08 在册）：接线件 `tools/codex-scripts/terminal-review.py`。`review` **只读盘**现算 sha256/字节/空否/BOM/关键词，判据只用非 LLM 四族（file_exists:/contains:/no_error/status_ok，与 longrun._judge 同口径），可选 producer_run 取产出方**自报**与盘上真值逐项对账（背离逐条列；自报一概不采信）；`escalate` 从任务真读数出「五选项 + 决策人 + 期限」；`retro` 冲刺三问；`reflow` 差异化重试（失败数据回流 _prev_error/_prev_attempts/_prev_fingerprints）。**默认零写盘**（只打印读数与判决）；写面一律走**既有账本位**（lr_submit/lr_tick/handoff），不另造第二本账；判据未知一律拒（fail-closed；退出码 0=过 / 1=拒，可当闸）。op=review/escalate/retro/reflow/status/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("review_gate")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show review_gate          # 本页内容的终端版
gbt-caps show review_gate --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("review_gate", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `lr_submit`、`lr_tick`、`handoff`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `security` · handler `review_gate`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
