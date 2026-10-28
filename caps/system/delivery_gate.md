# `delivery_gate`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `delivery_gate` |

## 用途

**交付闸**（主人令 2026-10-09：「每一个能力必须单独跑通闭环才能交付，要不然我不管你做了多久我直接丢垃圾桶不带说的」）。移植来源 V9 core/delivery_gate.py，**设计借过来、件按 V8 自己造**：V8 的「独立验收器」= caps_sweep 真过唯一门调用那位能力 + 它自己的测试件。op=status 读全量扫账逐档计数 · check 单件**现跑** · audit 逐件判定 · gate 硬闸（不可交付⇒ok=false）。判据：通/如实否⇒可交付 · 如实拒⇒可交付但要写明缺哪张票 · 要参数/缺依赖/真坏/未扫⇒**禁交付**；参数型输入口要**登记**（DECLARED_NEEDPARAM）才放行，没登记一律照旧禁交付。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("delivery_gate")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show delivery_gate          # 本页内容的终端版
gbt-caps show delivery_gate --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("delivery_gate", {'op': '<见描述>'})
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

- 注册表：`caps_registry.py` · 域 `system` · handler `delivery_gate`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
