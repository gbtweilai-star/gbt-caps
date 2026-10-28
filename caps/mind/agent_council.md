# `agent_council`

| 项目 | 值 |
|---|---|
| 域 | [`mind`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`convene` / `speak` / `speak_auto` / `vote` / `minutes` / `verify` / `status` / `where`） |
| 处理器 | `agent_council` |

## 用途

多智能体议事会（蒸馏自 2026-09-28 主人给的周榜卡 AutoGen 61.2k★ 微软开源，只取**开会这一面**；并行干活已有 agent_rig/orca，拍板已有 Jev 四角色引擎，不重造）：`convene` 定题定角色（默认对位 Jev 四角色）· **发言权** round_robin 下抢话 ⇒ 结构化拒绝 · `speak_auto` 大脑走门（llm_chat，external_llm 闸，没票如实报）· `vote` **终止要全员**投「结束」或轮次用尽，主持人不许独断 · `minutes` 纪要带全文 sha，篡改 ⇒ verify 当场报被改过。op=convene/speak/speak_auto/vote/minutes/verify/status/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("agent_council")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show agent_council          # 本页内容的终端版
gbt-caps show agent_council --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("agent_council", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `convene`、`speak`、`speak_auto`、`vote`、`minutes`、`verify`、`status`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `mind` · handler `agent_council`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
