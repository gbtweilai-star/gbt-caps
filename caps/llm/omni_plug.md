# `omni_plug`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`process` / `file` / `api` / `web`） |
| 处理器 | `omni_plug` |

## 用途

万能插：把「能力位」拓成「插座」——任何外部对象（process/file/api/web/**app**）插一个描述符就变成一根可扫可控的分支。op=status/sockets/energy/selftest 为**读类直连**；plug 只做存在性探测；run **真执行**（按插座类型过门：process→process_execute · file写→filesystem_write · api→external_llm+data_export · web/app→desktop_control+privacy_read（app 还能 do=launch 起进程）· 未知插座 fail-closed）。本件**从 V8 自己的树里长出**（不 import V9）：抽插座照 V9 那套，**门留在 V8 这边** —— V9 的 run_plugged 里 process 直接 subprocess、file 直接写盘，没有作用域校验，正是它缺的一环。三条纪律：不攻击/不绕授权校验 · 凭据只从 env 取且绝不回显原文 · 每插每跑都落账。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("omni_plug")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show omni_plug          # 本页内容的终端版
gbt-caps show omni_plug --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("omni_plug", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `process`、`file`、`api`、`web`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `omni_plug`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
