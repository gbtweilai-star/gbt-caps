# `surface_bind`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`probe` / `sweep` / `keys` / `verify`） |
| 处理器 | `surface_bind` |

## 用途

通用「可控制面」绑定器（主人令 2026-09-27：「其他工具全部都要可控按键一个不漏的绑定好」）：**让每个工具自己报出可控制键**（ffmpeg -filters/-encoders/-formats… · git help -a · genoffice --help · freebuff --help · python 每个标准库模块一把键 · blender 走 bpy 枚举）→ 落清单 state/surfaces/<工具>.json → 绑到该工具的触手；**重扫对比：新键并入、消失的键=断连**。安全写法：探针**生成脚本 + 字面量 cmd 执行**（不把 exe 变量当程序名 —— 钩子拦过）。op=probe/sweep/keys/verify

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("surface_bind")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show surface_bind          # 本页内容的终端版
gbt-caps show surface_bind --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("surface_bind", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `probe`、`sweep`、`keys`、`verify`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `surface_bind`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
