# `desktop_distill`

| 项目 | 值 |
|---|---|
| 域 | [`tentacle`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`method` / `rhythm` / `source` / `provenance` / `where`） |
| 处理器 | `desktop_distill` |

## 用途

**蒸馏件**（不是外挂）：把吞入件 CursorTouch/Windows-MCP（MIT · 8871★ · MCP Server for Computer Use in Windows）的**取法**提炼成我们自己的桌面操作判据（主人令 2026-10-12「我们吞噬都是加入蒸馏提炼出契合我们的能力」）。四条：①状态先行（动手前先取一帧窗口/UI 状态）②UIA 优先、视觉可选（层级=UIA 直取→DOM 降噪→视觉兜底）③DOM 模式给浏览器降噪（Firefox 无 RootWebArea ⇒ 要 IAccessible2 兜底）④动作节律 op=rhythm（它的 0.2–0.5s 基线**现算**成「动后等稳定」等待，带上限防死等）。op=source 现读胶囊尺寸+逐文件 sha256 · op=provenance 逐条指回原话（含**未蒸馏**两行：起服务/装计划任务故意不取 · App-Tool 依赖英文 Windows 只当坑记）。**零作用域**：无 subprocess / 无 urllib / 无写盘。边界：win-mcp 干的事我们**已有**（tentacle / desktop_commander / browser）⇒ 本位只蒸取法，不建平行位。op=method/rhythm/source/provenance/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("desktop_distill")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show desktop_distill          # 本页内容的终端版
gbt-caps show desktop_distill --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("desktop_distill", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `method`、`rhythm`、`source`、`provenance`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `tentacle` · handler `desktop_distill`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
