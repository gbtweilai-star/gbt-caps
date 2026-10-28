# `vision_grounding`

| 项目 | 值 |
|---|---|
| 域 | [`vision`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`domain_index` / `domain_read` / `domain_act` / `domain_type`） |
| 处理器 | `vision_grounding` |

## 用途

**视觉/定位通道契约**（主人令 2026-10-11「视觉必须达到 VLX-Flow 水平，脑-手同步**不能使用传统截图**看来在操作」）：把「看」分层钉死 —— **L1 结构层**（UIA 控件树 domain_index/domain_read/domain_act/domain_type · CDP DOM browser op=native · HTTP/API 读数）优先；**L2 接地层**（像素 + 模型 grounding，VLX-Flow 级）**仅兜底**（自绘 UI/Canvas/游戏/无 a11y 窗口）；**L3 回读层**（每次动手后用 L1 再读一次确认）。铁律：**先结构后像素**（用 L2 而无 L1 尝试记录 ⇒ 记违规 struct_first）· **动完没回读 ⇒ unverified** · 不编（读不到就如实报控件不在 a11y 树里）。op=channels/record/audit

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("vision_grounding")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show vision_grounding          # 本页内容的终端版
gbt-caps show vision_grounding --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("vision_grounding", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `domain_index`、`domain_read`、`domain_act`、`domain_type`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `vision` · handler `vision_grounding`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
