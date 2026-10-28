# `brain_council`

| 项目 | 值 |
|---|---|
| 域 | [`mind`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | `op`, `question` |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `brain_council` |

## 用途

脑会·编队群决策引擎：各脑出本域提案，委员长聚合裁决（纯推演·不出网·不落盘）；执行仍走主脑既有授权门

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("brain_council")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show brain_council          # 本页内容的终端版
gbt-caps show brain_council --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("brain_council", {'op': ..., 'question': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `op` | 是 | op=status（默认，读群与脑清单）| op=convene & question=…（召开脑会，返回裁决与提案） |
| `question` | 是 | op=status（默认，读群与脑清单）| op=convene & question=…（召开脑会，返回裁决与提案） |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `mind` · handler `brain_council`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
