# `genoffice`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`info` / `pdf` / `guide` / `capabilities`） |
| 处理器 | `genoffice` |

## 用途

办公文档（GenOffice **蒸馏版** · 本地 CLI 0.10+）：info/pdf/guide/capabilities + convert/create/merge/slides/sheet/docs/render **全部接通**（文档处理全本地、零云依赖）；search/image/media 保留（走主人自配 provider ⇒ **耗积分**，不许念成"全免费"）；**控制端类命令（open/selection/mcp/install-cli/skill）默认不接 —— 主人点名放行并留痕**（state/genoffice_control.jsonl）；读类直连、写类过 filesystem_write 门（处理器层挂闸，不碰 policy）。op=status/ops/<命令名>/run

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("genoffice")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show genoffice          # 本页内容的终端版
gbt-caps show genoffice --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("genoffice", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `info`、`pdf`、`guide`、`capabilities`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `genoffice`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
