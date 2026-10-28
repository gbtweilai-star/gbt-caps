# `ledger_note`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `ledger_note` |

## 用途

**台账登记**（R-H600 立）：三原语 RULES（读七道硬闸）/ PREVIEW（只读预演，不落盘）/ APPEND（**唯一写原语**）。七道机械闸全做成闸、不是口号：**目标固定**（只能写 gbt_allinone/docs/待落刀登记.md，**调用方传不了路径**）· **只追加**（目标末尾必须是换行，否则拒写，不修不补）· **单物理行**（行内不许换行 ⇒ 一刀一个物理行）· **禁半角双引号**（中文串用「」）· **行首形状**（`> **<label> 补记`，复核脚本按行首锚定）· **幂等**（同 label 已存在 ⇒ 拒写）· **缺前驱拒写**（给了 after 就必须是当前最后一条，防插队防回填）。⚠️ 它**不判内容对错**（那是取证 + 独立复核的活）；写失败一律抛错，不返回半成功。type=internal

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("ledger_note")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show ledger_note          # 本页内容的终端版
gbt-caps show ledger_note --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("ledger_note", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `ledger_note`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
