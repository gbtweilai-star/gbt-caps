# `omni_arm`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `spec` / `where`） |
| 处理器 | `omni_arm` |

## 用途

Omni-Arm（主人 2026-10-19 六件设计稿的实现版）：**22DoF 手 + 9 骨手臂 + 8 段触手 = 40 骨**，真几何（1080 顶点）/真蒙皮（每顶点权重和=1）/真 GLB，Blender 4.2 本地建件零付费。设计稿归档在 `vendor/omni-arm/source/`；原件**跑不动**（fk 只算 2D、ik 非 CCD、random 决定骨轴 ⇒ 不可复现、生成的 Blender 脚本语法坏、导出路径写死 /mnt/data），本器是**重做后的确定性实现**（零随机：轴/长度/限位全查表）。八条自检：骨 40（skin.joints）/单网格单蒙皮/关节 40/未绑 0/权重归一/顶点>300/尺寸合理/GLB 落盘。op=status/spec/where（纯读）· build（跑 Blender 落件 ⇒ filesystem_write 门在处理器层）。看件页 `holo_pet_w3/omni-arm/index.html`（骨架开关+骨骼树+sha16 自证）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("omni_arm")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show omni_arm          # 本页内容的终端版
gbt-caps show omni_arm --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("omni_arm", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`spec`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `omni_arm`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
