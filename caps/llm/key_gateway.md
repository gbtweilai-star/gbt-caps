# `key_gateway`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `whoami` / `energy` / `plan` / `keys` / `compat` / `mask` / `classify` / `verify` / `selftest`） |
| 处理器 | `key_gateway` |

## 用途

统一密钥网关：**唯一密钥真源**（链序/冷却/禁用/耗尽/换道）+ 触手统一密钥（`gbtv8-<32hex>`，库内只存 blake2b 摘要）的铸造与校验 —— 也是触手密钥 Y 字端口的取钥处（R-H201：不另开第二条取密钥的路）。op=status/whoami/energy/plan/keys/compat/mask/classify/verify/selftest 为**读类直连**（只读账本与配置，不落盘、不外发、不铸钥）；mint/revoke/note/reset 改**密钥账本与运行态** ⇒ 过 filesystem_write 门；materialize 是**唯一返回明文密钥**的路 ⇒ 按 external_llm 收口；作用域声明挂在 **cap 边界**（security/policy.py::evaluate），与本域同口径

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("key_gateway")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show key_gateway          # 本页内容的终端版
gbt-caps show key_gateway --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("key_gateway", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`whoami`、`energy`、`plan`、`keys`、`compat`、`mask`、`classify`、`verify`、`selftest`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `key_gateway`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
