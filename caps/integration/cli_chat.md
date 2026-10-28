# `cli_chat`

| 项目 | 值 |
|---|---|
| 域 | [`integration`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `cli_chat` |

## 用途

外部 CLI 助手**对话面板**（把「集成」面板真的接到对话上）：`agents` 只读底表（装没装/版本/**能不能一次性驱动**/一次形态）· `send` **真发一句话**给选定的 CLI 助手（claude `-p` / codebuddy `-p` / codex `exec` / copilot `-p`，形态**现跑 --help 亲验**）· `transcript` 会话账 · `verify`/`where`。**「免费」的确切含义**：走各 CLI **自己的登录态/额度**（订阅额度），不经框架 API key ⇒ **不吃 API 账单**（≠ 无额度上限）。⚠️ 与 freebuff 的**本质差别**：这 4 位**都有**非交互一次性入口（freebuff 是 TUI-only）⇒ 面板**能真聊**。⚠️ `send` = 起外部进程 + 把 prompt 送出本机 ⇒ 挂 `process_execute`+`external_llm`；policy.py 无本位分支（owner-only，AI 无权改）⇒ 门在模块内自闸（auth_gate 唯一校验入口），缺授权如实报缺。未装位/图形位 fail-closed 如实报缺 + 给装法，**不编**。safe=false：send 起进程且内容出本机（不是纯只读面）。type=internal

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("cli_chat")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show cli_chat          # 本页内容的终端版
gbt-caps show cli_chat --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("cli_chat", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。

## 出处

- 注册表：`caps_registry.py` · 域 `integration` · handler `cli_chat`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
