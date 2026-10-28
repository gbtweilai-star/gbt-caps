# `warm_switch`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `cost` / `on` / `off`） |
| 处理器 | `warm_switch` |

## 用途

**按需常驻开关**（主人 2026-10-12「可以通过隧道，你这么跳都一样」+「**触手就是最好的传输工具，比隧道还好**」）：开工挂热 / 收工放掉缩 0。口径：**心跳走本机桥（触手）**，不裸打云端 —— 走的同一条真实通路，顺带持续验链，协议差/门/审计全带上（裸隧道这些都没有）。实测口径：热时第一句 ~1 秒 / 冷时 ~300 秒；常驻期间 GPU 按秒计费 ≈$0.89/时（诚实标价，不替你决定）。op=status/cost/on/off

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("warm_switch")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show warm_switch          # 本页内容的终端版
gbt-caps show warm_switch --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("warm_switch", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`cost`、`on`、`off`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `warm_switch`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
