# `god_view`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `god_view` |

## 用途

**上帝视角**（主人令 2026-10-09：「上帝视角也是一个超级导航和给你意见和建议也是一种给项目增加的定心丸」）。来历如实：索引里 OpenClaw Monitor → god_view，2026-09-20 盘上 0 命中、只能标 unverified；原先 V8 只有一块**只读总览**（自述「只呈现，不执行」），既不会导航也不会给意见 —— 本轮补成真能力位。四个 op：overview 全局一屏（能力位/域分布/报警/交付闸/今天动作，全现读）· navigate goal=<人话> **超级导航**（意图→域→档 A/B/C 排序，附可直接照抄的命令）· advise 按现读状态给**排好序的意见与建议**（每条带依据，定心丸）· where 一页说清现状与下一步。口径：**只读零作用域**（不起进程/不写盘/不出网）· **不猜**（导航给分与命中词）· **不许反问**（按 ux_doctrine 不开口闸，只给具体候选与命令）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("god_view")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show god_view          # 本页内容的终端版
gbt-caps show god_view --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("god_view", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `god_view`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
