# `gods_eye`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`see` / `advisors` / `ask` / `daily` / `plan` / `panel`） |
| 处理器 | `gods_eye` |

## 用途

上帝之眼（主人令 2026-09-27）：**看得见创作页面**（7 个面板 + 服务端口真连）+ **两位顾问（权限机器可读）**——Claude 只出意见建议（架构/方向/评审，**无决策权**）· CodeBuddy 只做杂事（**对主项目没有执行权**，点主项目路径一律拒，只服从与待命）· **决策权在主体**（我）；**每日汇报** = GBT 探针汇报 + 全量扫描 ⇒ **缺点/短板/卡点**（每条带来源 src，不许编）；`plan` 把"提升整体实力"落成提案与决策（留痕 state/gods_eye_plan.jsonl）；`panel` 出上帝之眼页面。op=see/advisors/ask/daily/plan/panel

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("gods_eye")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show gods_eye          # 本页内容的终端版
gbt-caps show gods_eye --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("gods_eye", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `see`、`advisors`、`ask`、`daily`、`plan`、`panel`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `gods_eye`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
