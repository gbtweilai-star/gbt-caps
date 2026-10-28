# `auto_switch`

| 项目 | 值 |
|---|---|
| 域 | [`mind`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `auto_switch` |

## 用途

自动化切换引擎（只读骨架·内调）：意图分析(L1解析+L2交叉验证+L3置信度)→任务分级→模型切换→原生执行→验证审计；接线点只有 Intent JSON；五条红线（低置信先问主人/不许直接执行/每次切换记 model_used/不可逆二次确认/身份不许改写）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("auto_switch")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show auto_switch          # 本页内容的终端版
gbt-caps show auto_switch --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("auto_switch", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。

## 出处

- 注册表：`caps_registry.py` · 域 `mind` · handler `auto_switch`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
