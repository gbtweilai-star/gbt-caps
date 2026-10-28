# `shot_director`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`plan` / `shot_table` / `rules` / `punctuation` / `moderation` / `evidence` / `check` / `route`） |
| 处理器 | `shot_director` |

## 用途

**镜头导演**（主人令 2026-10-16：把 **Seedance 2.0 Skill OS** 蒸进来）：蒸自 **Emily2040/seedance-2.0**（**MIT** · v6.7.0）的思想—— 视频模型 = **一个从没见过你的剧组**（不能提问 · 按字面渲染 · 只做第一个动作 · 跳剪忘光位站位 · 不告诉它就不移镜）。**十大坑 → 十修法**：字面但不死板（**感觉的一个普通词 + 一个物理锚**）· **一镜一动作** · 道具写手 · **每镜锁定句**（光/人/站位）· 位置与地理每镜重述 · **镜头表先于散文** · 提交前合规预筛（分类器拒的是词不是意图）。不代付生成费。op=plan/shot_table/rules/punctuation/moderation/evidence/check/route（**全只读·零作用域·不出网**）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("shot_director")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show shot_director          # 本页内容的终端版
gbt-caps show shot_director --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("shot_director", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `plan`、`shot_table`、`rules`、`punctuation`、`moderation`、`evidence`、`check`、`route`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `shot_director`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
