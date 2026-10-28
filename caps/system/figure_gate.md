# `figure_gate`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `figure_gate` |

## 用途

**出图交付门**（蒸馏 `wheresryan22/anatomy` 与 `AirsupHQ/machine-skill` 两份开源 Skill 的铁律）：**"The object is the explanation" + "real numbers or nothing" + §8 像批评家一样看图（required）"**。op=checklist 列“不算完成”六条并**逐条标可检度**（M 机检 / A 需产物 / H 只能人看）；declare_numbers 必须说清屏幕上的数由谁算出来；record_round 记一轮看图与问题清单；verdict 是 **fail-closed** 交付判据：数未声明 / 轮次不足 4 轮 / 最新一轮还有未清问题 ⇒ 不可交付。标 H 的那几条**仍需人看**，本件不假装能自动判美丑。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("figure_gate")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show figure_gate          # 本页内容的终端版
gbt-caps show figure_gate --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("figure_gate", {'op': '<见描述>'})
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

- 注册表：`caps_registry.py` · 域 `system` · handler `figure_gate`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
