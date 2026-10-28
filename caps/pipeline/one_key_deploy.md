# `one_key_deploy`

| 项目 | 值 |
|---|---|
| 域 | [`pipeline`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | `target` |
| 形态 | 一位一动作 |
| 处理器 | `one_key_deploy` |

## 用途

一指定江山乾坤换位：抓取(GitHub/本地)→镜像→验证→晋升一条命令，一次性上线零修改

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("one_key_deploy")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show one_key_deploy          # 本页内容的终端版
gbt-caps show one_key_deploy --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("one_key_deploy", {'target': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `target` | 是 | GitHub 仓库/子目录 URL 或本地目录路径；且必须显式声明落点 room="<房间名>" 或 into_global_production=true |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `pipeline` · handler `one_key_deploy`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
