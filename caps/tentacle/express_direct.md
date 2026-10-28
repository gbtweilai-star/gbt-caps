# `express_direct`

| 项目 | 值 |
|---|---|
| 域 | [`tentacle`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`gbt_allinone` / `tentacle` / `express_bridge`） |
| 处理器 | `express_direct` |

## 用途

确定性直达（主人令 2026-10-13：「全部以触手来实现，砍掉『理由』这个不定因数」）：**指名派单、不猜**——给能力名即直达；执行一律经统一门 run_task（权限门/审计/钢印/禁用名单照旧生效，危险动作/付款由护栏+人工审核兜底）。**不给名字一律拒（fail_closed）**，不许替她猜一个去跑。入参：kind=能力名、payload=给它的入参。对位件 gbt_allinone/tentacle/express_bridge.py::direct

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("express_direct")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show express_direct          # 本页内容的终端版
gbt-caps show express_direct --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("express_direct", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `gbt_allinone`、`tentacle`、`express_bridge`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `tentacle` · handler `express_direct`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
