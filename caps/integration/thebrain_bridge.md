# `thebrain_bridge`

| 项目 | 值 |
|---|---|
| 域 | [`integration`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `thebrain_bridge` |

## 用途

TheBrain 15 思维导图**接入桥**（把图集成进框架 + 把 AI 连上，**过变压器**）：`status` 探针（TheBrain 装/跑 · 数据面 Brain.db/MetaDB/AiConversations · Orion · 我们的 AI 端点 · 变压器，只读）· `graph`/`search`/`notes` 读思维导图（**离线直读 Brain.db（mode=ro）优先**，每个节点边都带 `source` 出处 —— 照 brain_graph 铁律：指不出的不画）· `ask`/`summarize` **把 AI 连接上且过变压器**：图上下文 → `transformer.compress`（省 token）→ `cache_get`（省调用）→ `llm/unified.ask`（真模型）→ `cache_put`，**给前后两个数** · `endpoint` 报告「TheBrain 的 AI 该填什么」+ 变压器前置端点形态 · `serve` 起**变压器前置的 OpenAI 兼容端点**（TheBrain 指向它 ⇒ 每次请求先过变压器，链路：TheBrain → 本端点 → 127.0.0.1:31716 桥 → 网关 → 模型）· `think`/`link` 写回（Orion）· `verify`/`where`。⚠️ 关键事实：TheBrain 后端带 OpenAI.dll/Anthropic.dll（OpenAI 兼容），框架**已有** OpenAI 兼容端点 127.0.0.1:31716（llm/genoffice_bridge）—— 但**不过变压器**；本模块补的就是这一环（这就是主人「用变压器连接上」的落点）。⚠️ 未订阅 ⇒ TheBrain 自带 AI 面不可用（preferences.message="No active subscription found."）。⚠️ 红线：**不改 Brain.db**（mode=ro）· **不写 TheBrain 配置** · **不回显凭据明文**（只给指纹）。写面/真调 = 出网/触外部 ⇒ `ask` 挂 `external_llm`、`think`/`link`/`serve` 挂 `process_execute`；policy.py 无本位分支（owner-only，AI 无权改）⇒ 门在模块内自闸（auth_gate 唯一校验入口），缺授权如实报缺。safe=false。type=internal

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("thebrain_bridge")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show thebrain_bridge          # 本页内容的终端版
gbt-caps show thebrain_bridge --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("thebrain_bridge", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。

## 出处

- 注册表：`caps_registry.py` · 域 `integration` · handler `thebrain_bridge`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
