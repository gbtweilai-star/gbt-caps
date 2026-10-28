# `console_hub`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`pages` / `graph` / `widgets` / `layout` / `scan` / `verify` / `where`） |
| 处理器 | `console_hub` |

## 用途

工作台中枢：**所有独立页面的唯一数据源**（主人令 2026-09-28「把所有触手连接全面专业化 3D 可视化…每个工作流的独立页面需要精细设计排布…必须先全面扫描确保不能遗漏」）：`pages` 页面登记表（单一真相）· `graph` 3D 图（30 域→209 能力→绑定弧→**运行脉冲=真台账尾**）· `widgets` Bento 九部件（**每个数带 src**）· `layout` 布局记忆 · `scan` **「不能遗漏」机检**（盘上现读 vs 登记表双向比对，未登记=盲区必须 0）。op=pages/graph/widgets/layout/scan/verify/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("console_hub")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show console_hub          # 本页内容的终端版
gbt-caps show console_hub --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("console_hub", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `pages`、`graph`、`widgets`、`layout`、`scan`、`verify`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `console_hub`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
