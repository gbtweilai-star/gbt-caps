# `event_ledger`

| 项目 | 值 |
|---|---|
| 域 | [`security`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`append` / `verify` / `tail` / `status` / `where`） |
| 处理器 | `event_ledger` |

## 用途

签名事件账（蒸馏自 2026-09-28 主人给的周榜卡 buzz block/buzz 34,934★，只取**账本纪律**「每条消息都是签名记录」，不引 Nostr 中继/网络面——出网归门与它自己的闸；人机同室协作已有 collab_gateway）：哈希链 + HMAC 签名，`hash=sha256(prev+规范化body)`、`sig=HMAC(key,hash)` ⇒ **改任意一条，它之后每一条都对不上，定位到第一条被改的**；钥匙随机生成 **DPAPI 落盘无明文**（复用仓内 deepseek_key 帮手），DPAPI 不可用 ⇒ fail-closed；**只增不删**（作废走 append retract）。op=append/verify/tail/status/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("event_ledger")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show event_ledger          # 本页内容的终端版
gbt-caps show event_ledger --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("event_ledger", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `append`、`verify`、`tail`、`status`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `security` · handler `event_ledger`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
