# `forge_mastery`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`roles` / `plan` / `judge` / `improve` / `recurse` / `check` / `route`） |
| 处理器 | `forge_mastery` |

## 用途

**节点即触手·专业生产与自我递归**（主人令 2026-10-16）：主人原话「ComfyUI 的每个节点就是一根触手，**根本不需要 ComfyUI 本体**；把这项原生能力发挥到极致，懂所有专业生产能力与完美作品，每次使用都要自我评判哪里不足，**无限制自我递归**」。落法：① **一节点=一触手**（用途/输入/输出/**判据**/坑/档位 六栏）② 真跑走 `comfy_native`（27 原生算子，**离线可跑、不需本体**）③ **六轴自评**（构图/光比/材质/物理一致/风格锁定/交付规格）④ **judge→improve→judge 无限递归**（每轮留痕；一次只动一处）。op=roles/plan/judge/improve/recurse/check/route（**全只读·零作用域**）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("forge_mastery")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show forge_mastery          # 本页内容的终端版
gbt-caps show forge_mastery --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("forge_mastery", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `roles`、`plan`、`judge`、`improve`、`recurse`、`check`、`route`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `forge_mastery`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
