# `project_context`

| 项目 | 值 |
|---|---|
| 域 | [`project`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`find` / `callers` / `callees` / `trace` / `dead_code`） |
| 处理器 | `project_context` |

## 用途

项目上下文：**文档面**（blueprint 蓝图 / brief 简报 / search 只读检索 / status）＋ **代码结构四面**（2026-09-23 接，补上「专业级编程AI」缺的那半身）：`symbols` 符号（顶层 def/class，可按名问「在哪定义」）· `deps` 依赖（内部 import 边 + 外部三方名）· `calls` 调用图（**复用现成 `tools/call_graph.py`**：find/callers/callees/trace/dead_code，4.2s / 351 文件）· `tests` 测试面（模块被哪些测试**提到**过）· `structure` 三面速览（4.4s，**刻意不含调用图**）。全部只读。⚠️ 四处诚实边界随结果一起带出：符号只收**顶层**；依赖只看 **import 语句**；调用图带**未解析率**（本仓约 0.66，所以「没人调用」先天有缺口）；测试面是**提到过**的代理**不是行覆盖**。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("project_context")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show project_context          # 本页内容的终端版
gbt-caps show project_context --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("project_context", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `find`、`callers`、`callees`、`trace`、`dead_code`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `project` · handler `project_context`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
