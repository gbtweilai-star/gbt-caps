# `case_mine`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`sources` / `fetch` / `ingest` / `save` / `search` / `where`） |
| 处理器 | `case_mine` |

## 用途

案例挖掘（starter story 架构蒸馏）：**公开盈利案例 → 结构化案例卡**——`sources` 登记源与抓取口径 · `fetch` **经唯一门**取公开页正文（`run_task('tentacle', web_read)`，本件自己不发 HTTP）· `ingest` 正文→案例卡（营收/起步/工具/渠道，**读不到落「未读到」不编**）· `save` 追加落盘（去重）· `search` 本地语料检索。每条卡必带 `source_url + fetched_at + text_sha256`；只留短引文（≤240 字）**不搬全文**。op=sources/fetch/ingest/save/search/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("case_mine")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show case_mine          # 本页内容的终端版
gbt-caps show case_mine --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("case_mine", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `sources`、`fetch`、`ingest`、`save`、`search`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `case_mine`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
