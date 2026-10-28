# `dh_brain`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `spec` / `actions` / `voice` / `metadata` / `health`） |
| 处理器 | `dh_brain` |

## 用途

数字人本体（只读能力位·2026-10-08 主人点名「元数据没接入」补齐）：把她（数字人）的**元数据经统一门暴露**——op=status/spec/actions/voice/metadata/health。op 一律**现读单一真源**（state/digital-human-rig.json / digital-human.json / dh_status_audit.json / voice-control-route.json / voicestudio_acceptance.json / projects/digital-human/out/*.json），**不复制第二份**；读不到如实报**未探测**（不折绿）；**零写面**（不改 rig/不渲染/不刷页/不记账）⇒ 读类直连，**无需 policy 条目**

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("dh_brain")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show dh_brain          # 本页内容的终端版
gbt-caps show dh_brain --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("dh_brain", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`spec`、`actions`、`voice`、`metadata`、`health`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `dh_brain`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
