# `eigenflux`

| 项目 | 值 |
|---|---|
| 域 | [`social`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `feed` / `friends` / `candidates` / `digest` / `metadata` / `where`） |
| 处理器 | `eigenflux` |

## 用途

AI 朋友圈（EigenFlux）· **只读能力位**（主人令 2026-10-08「数字人可以自己找朋友、看朋友圈有没有好玩和有用的消息」）：op=status/feed/friends/candidates/digest/metadata/where。一律**现读** `~/.eigenflux/servers/eigenflux/**` 本地数据面（feed/私信/contacts/profile），**零出网**（不调 eigenflux CLI）、**零写面**、**零 policy 条目**（读类直连）；candidates 由 feed(author_agent_id)+私信(sender_id)+contacts **结构性推导**，每条附 basis；digest 打分规则写死（兴趣簇/趣味标记/新鲜度/可互动）逐条带 evidence；**对外写动作（加好友/发私信/关注/广播）不在此件、必须过既有门**；读不到一律如实报**未探测/无数据**，**不许占位、不许折绿**

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("eigenflux")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show eigenflux          # 本页内容的终端版
gbt-caps show eigenflux --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("eigenflux", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`feed`、`friends`、`candidates`、`digest`、`metadata`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `social` · handler `eigenflux`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
