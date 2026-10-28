# `cadgen`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `where` / `version` / `doctor` / `help` / `snapshot`） |
| 处理器 | `cadgen` |

## 用途

**本机 CAD 链的口**（2026-10-13 建位）：只调真件 `cadgen`，不手搓几何。常用说法（人这么问就命得中）：建模 / 零件 / 三维 / 模型渲染 / 渲染 / 出图 / 看图 / 看件 / 工程图 / 导出 STEP / STL / 3MF / GLB / DXF / 3D 打印。能力面（照真件自己的 `--help` 现读）：**建模/零件/三维** · `step / 3mf / glb build`（导出 **STEP/3MF/GLB**）· `dxf / sdf / srdf validate` · `snapshot`（把 STEP/STL/GLB/DXF/URDF 真**渲染/出图**成 PNG，可做工程图/审图/3D 打印前看件）· `doctor` 自检（现读：kernel OK · OCP）· `mcp`（serve CAD over MCP stdio，**本位不接** —— 长驻服务，要接须主人点头）。铁律：参数照真件 `--help` **现读不编**；判码走 `tools/native_rc.run_native`（`shell=False` · **只认原生 rc**）；二进制不在 ⇒ `needs_dependency`；未知 op ⇒ fail-closed；`status` 连 `--version` 都不跑（纯探）。⚠️ 本机**没有 FreeCAD** —— 本位接的是 `cadgen`，不接 FreeCAD-MCP 那条壳。op=status/where/version/doctor/help/snapshot

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("cadgen")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show cadgen          # 本页内容的终端版
gbt-caps show cadgen --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("cadgen", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`where`、`version`、`doctor`、`help`、`snapshot`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `cadgen`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
