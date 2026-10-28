# `creation_camp`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`sources` / `caps` / `plan` / `where`） |
| 处理器 | `creation_camp` |

## 用途

创造营编排（「AI 视觉创造营」形式蒸馏）：**主题 → 逐日营计划**——7 天基准节奏（开营定题→采样风格→构图分镜→批量出图→修饰选片→编排成片→展陈复盘），每天三件（任务/产出物/验收点）。**零网络零 LLM**（确定性）；点名的能力位**现读注册表**，缺的落「缺口」（幽灵能力红）；视觉工具**只引用现成位、不重造**。op=sources/caps/plan/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("creation_camp")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show creation_camp          # 本页内容的终端版
gbt-caps show creation_camp --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("creation_camp", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `sources`、`caps`、`plan`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `creation_camp`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
