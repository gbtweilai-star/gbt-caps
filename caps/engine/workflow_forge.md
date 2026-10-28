# `workflow_forge`

| 项目 | 值 |
|---|---|
| 域 | [`engine`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`browser` / `code_audit` / `aesthetic`） |
| 处理器 | `workflow_forge` |

## 用途

**工作流十式**（主人令 2026-10-16：skills.sh 累计安装 TOP10 蒸馏）：① **find_skill**（先现读名册再看外部，不重造）② **grill**（连续追问厘清目标/范围/判据/边界，上限 8 轮）③ **grill_docs**（追问+术语表与决策记录）④ **arch_review**（结构体检与重构机会，不动手）⑤ **browser_ops**（点/填/抽，先看后动）⑥ **tdd_loop**（红-绿-重构，没先红不算 TDD）⑦ **setup_rules**（状态/标签/文档规则一次定死）⑧ **style**（先定视觉契约）⑨ **handoff**（现状+资料位置+下一步）⑩ **triage**（四档分类与状态推进，不下模棱两可）。**不重造**：真执行走既有位（browser/code_audit/aesthetic）；**先看后动**（第 37 条）。op=grill/grill_docs/find_skill/arch_review/browser_ops/tdd_loop/setup_rules/style/handoff/triage/check/route（**全只读·零作用域）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("workflow_forge")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show workflow_forge          # 本页内容的终端版
gbt-caps show workflow_forge --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("workflow_forge", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `browser`、`code_audit`、`aesthetic`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `engine` · handler `workflow_forge`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
