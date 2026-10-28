# `omni_web`

| 项目 | 值 |
|---|---|
| 域 | [`tentacle`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | `op` |
| 形态 | 一位多操作（描述中枚举：`path` / `content` / `mode`） |
| 处理器 | `omni_web` |

## 用途

万能触手·Web六态：看结构/读源码/读讲解/改文件/交给AI/跑项目；git+github+stackblitz一键触达

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("omni_web")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show omni_web          # 本页内容的终端版
gbt-caps show omni_web --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("omni_web", {'op': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `op` | 是 | op=看结构|读源码|读讲解|改文件|gitingest|跑项目；repo=GitHub URL或本地路径；files=[…]（read_source）；path/content/mode（edit_file，mode=write|append|replace）；max_files/max_chars（gitingest） |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `tentacle` · handler `omni_web`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
