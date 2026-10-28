# `record_grid`

| 项目 | 值 |
|---|---|
| 域 | [`data`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | `text`, `path` |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `record_grid` |

## 用途

行式记录网格：陌生文本结构画像/草案骨架/逐行解析/回写自证/词表校验（op=profile|draft|parse|emit|verify|vocab|presets）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("record_grid")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show record_grid          # 本页内容的终端版
gbt-caps show record_grid --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("record_grid", {'op': '<见描述>', 'text': ..., 'path': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `text` | 是 | 要画像/解析的内容：内联 text 或框架内相对路径 path（二选一）；parse 另需 plan 或 plan_name；emit 还要 records（记录列表） |
| `path` | 是 | 要画像/解析的内容：内联 text 或框架内相对路径 path（二选一）；parse 另需 plan 或 plan_name；emit 还要 records（记录列表） |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `data` · handler `record_grid`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
