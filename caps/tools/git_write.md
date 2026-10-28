# `git_write`

| 项目 | 值 |
|---|---|
| 域 | [`tools`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | `paths`, `message` |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `git_write` |

## 用途

**版本库写面**（只两个 op，且**永远要点名路径**）：stage（`git add -- <paths>`）· commit（**pathspec-limited**：`git commit -m … -- <paths>`，只提交点名的路径，**不动索引里别的暂存内容**）。为什么必须点名：本仓脏行可能上万，`commit -a` 一次就把不相干的全卷进去。**永远挂 `filesystem_write`**（不按 op 判 —— 拆成独立能力位就是为了让门的判据平凡正确）。与 `git_read` 分开登记：`safe` 是按能力位记的，不是按 op 记的。type=internal

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("git_write")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show git_write          # 本页内容的终端版
gbt-caps show git_write --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("git_write", {'op': '<见描述>', 'paths': ..., 'message': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `paths` | 是 | paths=要动的仓内路径列表（**必填、不许空**）；commit 还要 message；op=stage|commit |
| `message` | 是 | paths=要动的仓内路径列表（**必填、不许空**）；commit 还要 message；op=stage|commit |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `tools` · handler `git_write`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
