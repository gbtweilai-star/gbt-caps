# `memory_manager`

| 项目 | 值 |
|---|---|
| 域 | [`mind`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`index` / `find` / `store` / `stats`） |
| 处理器 | `memory_manager` |

## 用途

记忆管理 + 万能精准秒搜（主人令 2026-09-27）：SQLite **FTS5 全文索引**（实测中文可检索）·六类源（记忆/文档/技能/状态/**能力位**/代理）⇒ find 秒级返回「路径+类型+高亮片段」，并**同时端出匹配的能力位**（"想到匹配面出现的能力"）；index 增量（mtime+sha 未变即跳过；**不许整表清空** —— 实测因此丢过索引）；store 存记忆过 filesystem_write 门。SQL 纪律：全部内联字面量 + `?` 占位符，不用变量拼 SQL（安全钩子实测拦过两次）。op=index/find/store/stats

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("memory_manager")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show memory_manager          # 本页内容的终端版
gbt-caps show memory_manager --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("memory_manager", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `index`、`find`、`store`、`stats`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `mind` · handler `memory_manager`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
