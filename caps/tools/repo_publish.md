# `repo_publish`

| 项目 | 值 |
|---|---|
| 域 | [`tools`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`store` / `repo_publish` / `ledger`） |
| 处理器 | `repo_publish` |

## 用途

**远端发布面**（补 `git_write` 的另一半 · 主人 2026-10-11 当场指出：tools 域只有 `git_read` 与只能 stage/commit 的 `git_write`⇒ **push 到远端 / 建仓 / 发 Release 根本没有能力位** ⇒ 前面全靠手搓 git push/wrangler ✗）。口径：**不可逆外部动作 ⇒ 过 `deploy_publish` 一次性门**；出网硬钉（只许 https + github.com/api.github.com/huggingface.co）；**凭据永不回显**（本件第一版吃过把 token 带进报错的亏）；只追加落账 store/repo_publish/ledger.jsonl；不假装（没权限如实报）。op=status/plan/push

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("repo_publish")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show repo_publish          # 本页内容的终端版
gbt-caps show repo_publish --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("repo_publish", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `store`、`repo_publish`、`ledger`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `tools` · handler `repo_publish`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
