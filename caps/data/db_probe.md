# `db_probe`

| 项目 | 值 |
|---|---|
| 域 | [`data`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`sources` / `tables` / `schema` / `counts` / `jsonl` / `where`） |
| 处理器 | `db_probe` |

## 用途

本地只读查询台（dbx 蒸馏）：**SQLite 概览 + JSONL 行统计**——`sources` 列可查本地源 · `tables` 静态 SQL 列表/视图 · `schema` 参数化取 DDL + Python 解析列 · `counts` 每表行数（iterdump 文本计数）· `jsonl` 行统计/筛选（纯 Python 可自由筛）。🔴 **零动态 SQL**（两版被安全钩子按"SQL 注入"拦下 ⇒ 静态字面量 + 参数取值 + Python 层解析；连接 mode=ro）；结果不落盘；不提供按条件查行（要就说，请主人给门加分支）。op=sources/tables/schema/counts/jsonl/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("db_probe")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show db_probe          # 本页内容的终端版
gbt-caps show db_probe --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("db_probe", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `sources`、`tables`、`schema`、`counts`、`jsonl`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `data` · handler `db_probe`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
