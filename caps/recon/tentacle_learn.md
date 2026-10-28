# `tentacle_learn`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`scan` / `collect` / `extract` / `learn` / `loop` / `check` / `route`） |
| 处理器 | `tentacle_learn` |

## 用途

**触手扫描·采集·学习**（主人令 2026-10-16：这是必要的）：四步闭环 **scan → collect → extract → learn**，末尾**复验**“真的进了语料/可被现读”。面：能力面·页面面·文件面·设备面·网面（只对授权域）。红线：只扫/只采**授权与公开**面 · 隐私脱敏 · 采集物与语料**不外发** · 每步留痕 · 拿不准的不进 learn。op=scan/collect/extract/learn/loop/check/route（**全只读·零作用域·不出网**）；真扫真采走 browser/native_browser/sec_sweeper/触手眼。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("tentacle_learn")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show tentacle_learn          # 本页内容的终端版
gbt-caps show tentacle_learn --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("tentacle_learn", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `scan`、`collect`、`extract`、`learn`、`loop`、`check`、`route`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `tentacle_learn`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
