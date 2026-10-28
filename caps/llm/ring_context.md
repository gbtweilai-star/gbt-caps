# `ring_context`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`stats` / `window` / `push` / `recall`） |
| 处理器 | `ring_context` |

## 用途

**环形自动化上下文**（主人令 2026-10-11「设计一个圆型的自动化上下文，一直保持上下文长度却不会顶到溢出；另一边直接进数据库，需要查秒查」）：把上下文做成**一屏环**+**全量落库**+**秒查**。① 环形窗口：window() 恒定 ≤ window_chars，滑进来的进来、最老的挤出去 ⇒ **永不溢出**；② 溢出落 SQLite FTS5（seq 单调，只追加）⇒ **一条不丢**；③ recall(q,k) 走 FTS5 + CJK 兜底 ⇒ **秒查**（实测 60 轮/7200 字，查已滑出的老内容 2.97ms）。铁律：挤出≠删除（落库失败就不挤出）· 长度恒定 · 只追加 · 一屏给模型、全量给查询。实测治的病：框架 system 13480 字 + max_tokens 2000 顶爆端点窗口 ⇒ 502。op=stats/window/push/recall

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("ring_context")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show ring_context          # 本页内容的终端版
gbt-caps show ring_context --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("ring_context", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `stats`、`window`、`push`、`recall`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `ring_context`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
