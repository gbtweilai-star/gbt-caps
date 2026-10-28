# `dh_pose`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `semantics` / `compile`） |
| 处理器 | `dh_pose` |

## 用途

数字人动作控制（主人令 2026-10-13「触手化作骨架操控数字人的所有动作」+「连带手指脚趾都要绑骨」）：`status` 读现状 · `semantics` 读 42 条「意图→骨/轴/符号」语义表 · `compile` 把人话（抬臂/屈指/转身…）编译成骨角度 JSON · `pose` 编译+渲染一张（经 `blender` 位，写盘门在它那层）。轴系来自**旋转轴探针实测**（自转＝局部 Y；v1 用骨末端位移当探针时 Y 恒 0，是量错了地方）；指/趾骨已绑：65 骨中指骨 40 有 30 带权重、趾骨 4 有 2 带权重，其余 13 根全是末端骨。status/semantics/compile 纯读；pose 会写盘。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("dh_pose")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show dh_pose          # 本页内容的终端版
gbt-caps show dh_pose --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("dh_pose", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`semantics`、`compile`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `dh_pose`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
