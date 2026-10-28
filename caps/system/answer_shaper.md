# `answer_shaper`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`check` / `shape` / `where`） |
| 处理器 | `answer_shaper` |

## 用途

行动优先输出核（蒸馏自 2026-09-28 主人给的周榜截图 ayghri/i-have-adhd——截图只给仓库名，**未联网核验、未引用该仓任何代码/文本**；纪律取自本仓自己的沟通纪律与已有技能 gbt-adhd-mode，本件补**运行时可机检的核**）：`check` 五条确定性规则逐条判定（R1 首行是行动不是铺垫 · R2 有编号步骤 · R3 步骤≤5 · R4 无客套收尾 · R5 有下一步），零模型零出网零幻觉、每条带命中细节；`shape` **纯机械重排**（剥铺垫/抽编号步骤/截到 5 步），抽不出的原样进「未判定」区标需人看——**不替作者补写一字**。op=check/shape/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("answer_shaper")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show answer_shaper          # 本页内容的终端版
gbt-caps show answer_shaper --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("answer_shaper", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `check`、`shape`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `answer_shaper`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
