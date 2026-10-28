# `devour_github`

| 项目 | 值 |
|---|---|
| 域 | [`devour`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | `repo` |
| 形态 | 一位一动作 |
| 处理器 | `devour_github` |

## 用途

吞天：吞噬 GitHub 仓库为知识胶囊（自我进化的核心——吸收外部能力）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("devour_github")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show devour_github          # 本页内容的终端版
gbt-caps show devour_github --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("devour_github", {'repo': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `repo` | 是 | 要吞噬的 GitHub 仓库 URL（也认 url=） |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `devour` · handler `devour_github`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
