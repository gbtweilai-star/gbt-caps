# `skill_forge`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`think` / `radar` / `experience` / `style` / `anti` / `check` / `route`） |
| 处理器 | `skill_forge` |

## 用途

**技能蒸馏五式**（主人令 2026-10-16：把五个 skill 蒸成我们的原生能力）：蒸自五个 MIT 仓的思想—— ① **女娃**（nuwa-skill）不是复制人、是提炼思维框架（心智模型/决策启发式/表达 DNA/边界）② **last30days**：agent 主导的搜索、按投票与真实金额计分（非编辑评分），跨 Reddit/X/YouTube/HN/Polymarket/web ③ **同事**（distilly）：经验/对话→可复用技能 ④ **前任**（ex-skill）：原材料→说话方式 DNA ⑤ **反蒸馏**（anti-distill）：交出版消毒 + **私有备份留核心**。op=think/radar/experience/style/anti/check/route（**全只读·零作用域·不出网**）；边界：MIT 只蒸思想 · **隐私**（原材料不外发、第三方脱敏、不做人脸声纹建模）· **不冒充真人**。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("skill_forge")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show skill_forge          # 本页内容的终端版
gbt-caps show skill_forge --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("skill_forge", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `think`、`radar`、`experience`、`style`、`anti`、`check`、`route`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `skill_forge`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
