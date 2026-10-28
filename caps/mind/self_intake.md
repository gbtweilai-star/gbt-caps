# `self_intake`

| 项目 | 值 |
|---|---|
| 域 | [`mind`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`known` / `gate` / `rules`） |
| 处理器 | `self_intake` |

## 用途

**未命中即取源 · 自递归改进**（主人令 2026-10-15：「在她的知识库未命中的时候转抓取全网国内外的论文来实现自我递归改进，这样就不会出现自己都不懂的东西就无脑操作了」。回路：**known（先查本地知识库）→ 未命中 ⇒ intake（抓取全网取源）→ 蒸馏胶囊（带出处）→ 钢印护照 + 入 context_vault 索引 → 再查就命中**。op：known/gate/rules（只读）· intake（写）。**主执行器是万能插**（`five-dim.py cap self_intake`），不是传统执行器。铁律：未命中且无出处 ⇒ 拒绝干活；取不到就写「未读到」。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("self_intake")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show self_intake          # 本页内容的终端版
gbt-caps show self_intake --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("self_intake", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `known`、`gate`、`rules`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `mind` · handler `self_intake`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
