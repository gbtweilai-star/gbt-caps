# `policy_gate`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `policy_gate` |

## 用途

**权限／付款直答门**（fact_gate 同族 · 主人令「拿实质性证据说话」）：能不能做／要不要授权**也是事实**，不该过模型。实测病根：终考里「买 4090」不是机器事实 ⇒ 没过 fact_gate ⇒ 模型又编市场数据（编出「本机 4194x2 已满」「4090 价格带 150-250 元」+ 一个 URL）。做法：① 现读**真门** `auth_gate.SCOPES` 原文 → ② 意图与真表描述对一遍 + 意图对照（**真表过滤**，表里没有的作用域绝不出现）→ ③ 代码判定命中哪些作用域／哪些一次性 → ④ 直答，模型只许在后面加「所以怎么办」。付款类再钉一句：**市场价／库存／商家／型号一律不许编**。op=classify/answer

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("policy_gate")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show policy_gate          # 本页内容的终端版
gbt-caps show policy_gate --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("policy_gate", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 见「用途」）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `policy_gate`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
