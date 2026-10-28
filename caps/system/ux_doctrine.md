# `ux_doctrine`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `ux_doctrine` |

## 用途

**交互铁律**（主人令 2026-10-09）：「在框架里面出来必须要用户求助帮忙的其他全部禁止掉……你开口要求用户的时候你就输了」「可以跟用户商量项目架构和排布，严禁要求用户帮助」「每次停下要么是项目部署完成，要么就是真正需要用户来操作的可以停下，其他时候你停下干嘛」。移植自 V9 core/ux_doctrine.py（教义照搬，危险清单按 V8 真门重写）。op=doctrine 读全部规则 · ask **不开口闸**（14 条正则抓「要用户做事」，唯一例外=身份登录）· dismissal **敷衍闸**（不影响/忽略即可/下次再说 全禁）· triage **报警闭环闸**（{现象→根因→处置→证据} 四件齐才算闭环）· owner 判要不要停人要授权 · stop **停点闸**（只有「部署完成带证据」与「危险清单授权」两种理由合法，其余一律不许停）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("ux_doctrine")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show ux_doctrine          # 本页内容的终端版
gbt-caps show ux_doctrine --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("ux_doctrine", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 见「用途」）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `ux_doctrine`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
