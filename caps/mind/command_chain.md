# `command_chain`

| 项目 | 值 |
|---|---|
| 域 | [`mind`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`plan` / `commit` / `close` / `assignments` / `roster` / `status` / `where`） |
| 处理器 | `command_chain` |

## 用途

指挥链·总指挥参谋部（主人令 2026-10-01「全部统一品牌统一智能体以 GBT小土豆V8 为主延申…不能重复和错误指挥」）：五段全踩已有件不重造 —— ①接令·理解意图（brain_route）②双顾问意见（大脑执行层读数 + gods_eye 顾问席，主人 9-28 分工口径）③总指挥决策（确定性合并成工作单元，**必须引用双顾问出处**）④专业提示词（prompt_bridge 四段，带原意保真自检）⑤触手智能体分派台账（commit 只落账，**执行仍走各能力的门**）。两条铁律做成判据：**防重复**（work_key 唯一 · plan_hash 幂等 · 开放分派互斥）与**防错指挥**（幽灵能力/幽灵执行席/缺双顾问出处 全红）。op=plan/commit/close/assignments/roster/status/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("command_chain")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show command_chain          # 本页内容的终端版
gbt-caps show command_chain --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("command_chain", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `plan`、`commit`、`close`、`assignments`、`roster`、`status`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `mind` · handler `command_chain`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
