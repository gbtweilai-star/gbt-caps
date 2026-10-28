# `llm_watch`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`review` / `queue` / `ack` / `status`） |
| 处理器 | `llm_watch` |

## 用途

大脑执行层·**守望**（主人令 2026-10-13「监控触手LLM的监控，只要发现不对主脑要第一时间知道」）：每次 LLM 输出过后**当场过机器判据** —— 无证据的「已完成」声明 / 越权（自我授权）声明 / 机器事实无现读 / 自相矛盾 / claims 无 evidence / 数字对不上；命中就**立刻进主脑注意力队列**（queue.jsonl）。🔴 **只认可机检的错**：语义幻觉这一层**判不了就如实写判不了**，不冒充判过（防幻觉的正主是 fact_gate/policy_gate）。op=review/queue/ack/status

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("llm_watch")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show llm_watch          # 本页内容的终端版
gbt-caps show llm_watch --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("llm_watch", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `review`、`queue`、`ack`、`status`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `llm_watch`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
