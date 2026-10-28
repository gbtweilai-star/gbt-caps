# `genoffice_bridge`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `genoffice_bridge` |

## 用途

GenOffice AI 线 → 统一密钥网关的**本地 OpenAI 兼容桥**（127.0.0.1:31716）：GenOffice 侧只需握一把 gbtv8- 统一密钥，换道/冷却/禁用/耗尽全由网关机械闸管 ——**不新增 AI 线，只换接头**（保留其 custom provider）。op=status/probe 为**读类直连**（只读接线状态 + 回环 GET /health 探活）；selftest 会铸一把测试钥 + 起临时端口 + 真出网 ⇒ 过门；**serve 不在能力位上**（serve_forever 常驻会挂住调用方 · 纪律第 35 条"穿透传输不阻塞"），走 CLI；作用域声明挂在 cap 边界（security/policy.py::evaluate）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("genoffice_bridge")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show genoffice_bridge          # 本页内容的终端版
gbt-caps show genoffice_bridge --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("genoffice_bridge", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 见「用途」）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `genoffice_bridge`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
