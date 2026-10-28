# `rig_audit`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `dh_rig` |

## 用途

绑骨体检（Blender 4.2 · 本地 · 零付费）：DCC 级量骨架/骨数/层级深度/每骨权重顶点数与权重和/未绑顶点/非归一化权重/零长骨/左右镜像/包围盒/缩放是否已应用；**自动剔除 Blender 导入器造的 42 顶点 Icosphere 显示形状**（文件里没有它，别当杂物球）。op=status（纯读）· run（写派生 .js 给页吃 ⇒ filesystem_write 门在处理器层）· check（只对账 .js 与 GLB 的 sha）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("rig_audit")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show rig_audit          # 本页内容的终端版
gbt-caps show rig_audit --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("rig_audit", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 见「用途」）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `dh_rig`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
