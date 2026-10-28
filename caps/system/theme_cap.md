# `theme_cap`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`state` / `theme` / `templates`） |
| 处理器 | `theme_cap` |

## 用途

**主题能力位**（蒸馏自 Omarchy 的 "colors.toml 主色 + 模板重生成全系统配置"）：**一份取值空间（[colors] + [dims]） ⇒ 四个界面 CSS 的主题块一起变**。op=list/show 看色源；check 判据（漂移 + 悬空引用 + 颜色尺寸各有人用）；render 预览（可 --outdir 落别处，**原件一字不动**）；discover 现读收录；apply 真写（先留 .bak）。**模板独立成件**（state/theme/templates/*.tpl），**块外一字不动**，没有标记块的文件跳过并点名。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("theme_cap")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show theme_cap          # 本页内容的终端版
gbt-caps show theme_cap --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("theme_cap", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `state`、`theme`、`templates`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `theme_cap`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
