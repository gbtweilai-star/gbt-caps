# `pulse_direct`

| 项目 | 值 |
|---|---|
| 域 | [`tools`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `pulse_direct` |

## 用途

**脉冲直达**（主人令 2026-10-11「把脉冲给大模型，让她把所有的能力按触手双向绑定的部署方式**急速运行**、**省去不必要的多绕** —— 本来向前跨一步就到的东西，别跑一大圈才跨那一步」）：一句意图 => **一步**解析到能力位 => 给出那一条命令与要过的门，并把 **hops（绕弯数）写进账**：hops=1 直接命中 / hops=2 命中页面包装层（该收敛）/ hops=0 没命中（如实报，不编）。op=audit 读回**一步命中率** => 「省多绕」变成可量的事。三根支柱现读：能力位册 / 双向绑定(cap-bindings+page-caps) / 唯一门 run_task。与既有 tools/pulse.py（每日情报调研执行层）不是一件东西，不覆盖不合并。op=resolve/audit

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("pulse_direct")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show pulse_direct          # 本页内容的终端版
gbt-caps show pulse_direct --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("pulse_direct", {'op': '<见描述>'})
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

- 注册表：`caps_registry.py` · 域 `tools` · handler `pulse_direct`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
