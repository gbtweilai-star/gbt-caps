# `skill_watch`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`observe` / `snapshot` / `shortboards` / `advise` / `drift`） |
| 处理器 | `skill_watch` |

## 用途

**技能观察器**（主人令 2026-10-11「使用技能在每次使用的时候都要注意技能的**变化和短板**来打磨进化」）：每次用技能留三笔 —— **用成没成（读数）· 它变了没（面漂移）· 它短板在哪（打磨点）**。① observe：cap/成败/耗时/错误类/被门拦 ⇒ 只追加落账；② snapshot+drift：把技能当下可控制面（op 表/参数/节点/版本）与上次快照比，变了报 surface_changed（对齐「节点消失=断连」，升级改名也算）；③ shortboards+advise：按读数排行短板（失败率/耗时 P90/缺依赖/被门拒），每条给**可执行的打磨点**。铁律：只追加 · 不许编（无观测就报无观测）· **每条建议必须挂它对应的读数**。op=observe/snapshot/shortboards/advise/drift

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("skill_watch")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show skill_watch          # 本页内容的终端版
gbt-caps show skill_watch --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("skill_watch", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `observe`、`snapshot`、`shortboards`、`advise`、`drift`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `skill_watch`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
