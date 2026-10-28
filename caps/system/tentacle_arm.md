# `tentacle_arm`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `limits` / `plan` / `where`） |
| 处理器 | `tentacle_arm` |

## 用途

**触手操控臂**（主人令 2026-10-19「你要以这些能力的思路来操控触手，本身触手就是我们的手，所以必须学会这样的操控精度」）：把 Omni-Arm 的五层精度模型套到能力位上 —— 关节 = 一次 (kind, op, payload)；`dof` = 该位在注册表登记的几个 op；`limits` **现算**（policy.evaluate 的作用域 ＋ preflight.is_side_effect 判出的处理器层闸），不手写；`reversible` 只读 op 才算可逆。op=status/limits/plan/where（纯读免门）· op=move 逐关节走 `run_task`，**票由那一位自己的门收**（本位不另加门、也不绕门），动完按 `expect` **量误差**（不把"调了"当"到了"）。冲击保护：缺票/缺必填参/读不出 op 一律**动手前**拒（fail-closed）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("tentacle_arm")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show tentacle_arm          # 本页内容的终端版
gbt-caps show tentacle_arm --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("tentacle_arm", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`limits`、`plan`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `tentacle_arm`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
