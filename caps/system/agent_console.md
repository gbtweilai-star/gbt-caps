# `agent_console`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`ok` / `stale` / `failed`） |
| 处理器 | `agent_console` |

## 用途

代理驾驶舱：**任务监督循环 + 连接请求审批桥**（蒸馏自 GitHub 周榜 #05 paperclip，只取架构）：`add` 登记被监督任务（判活看**读数有没有如期更新**，不是 exit code）· `tick` 定时检查出 ok/stale/failed 并列出该做什么（**不擅自执行**）· `retry`/`wake` 要 process_execute 门 · `request`/`pending`/`approve` 连接请求审批桥：**approve 要求 TTY + 手打 YES ⇒ AI 批不了**。op=add/tick/board/retry/wake/request/pending/approve/verify/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("agent_console")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show agent_console          # 本页内容的终端版
gbt-caps show agent_console --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("agent_console", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `ok`、`stale`、`failed`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `agent_console`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
