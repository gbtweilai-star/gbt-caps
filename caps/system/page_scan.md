# `page_scan`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `page_scan` |

## 用途

**按绑定逐页并发扫**（主人 2026-10-12 定的架构「触手随每一页绑定好，扫的时候按绑定一页一页传回来」）：源 = state/page-bindings.json 的逐页（页→落点→正向_能力位，全在盘）；**按契约判色**——绿=跑通 / 黄=需参数或需授权（契约与门，不是故障）/ **红=契约也满足却仍失败**；页/落点/在册三项独立判；并发用满（实测引擎 ≥4096 根零失败）。op=scan/status

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("page_scan")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show page_scan          # 本页内容的终端版
gbt-caps show page_scan --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("page_scan", {'op': '<见描述>'})
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

- 注册表：`caps_registry.py` · 域 `system` · handler `page_scan`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
