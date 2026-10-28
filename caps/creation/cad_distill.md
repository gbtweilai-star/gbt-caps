# `cad_distill`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`method` / `source` / `provenance` / `where`） |
| 处理器 | `cad_distill` |

## 用途

**蒸馏件**（不是外挂）：把吞入件 neka-nat/freecad-mcp（MIT · 2833星 · Python：「Control FreeCAD from Claude Desktop and other MCP clients … run FEM analyses」）的**挂载取法**提炼成我们自己的判据：①挂真内核不另起（addon 装在 FreeCAD 里面 + 只连在跑的那个 RPC server）②脚本即接口（run Python scripts，不把动作硬编码成几百条命令）③改前先读回（inspect documents，同铁律1先看再动）④工程结论必须算（run FEM analyses，同 machine_distill ①）。op=source 现读胶囊尺寸+逐文件 sha256 · op=provenance 逐条指回原话（含**未蒸馏**一行：改 claude_desktop_config.json + 起 RPC 服务不取）。**零作用域**。边界：接入端 ≡ 我们**已有**的 cadgen；本位只蒸取法，**不建平行位**。op=method/source/provenance/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("cad_distill")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show cad_distill          # 本页内容的终端版
gbt-caps show cad_distill --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("cad_distill", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `method`、`source`、`provenance`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `cad_distill`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
