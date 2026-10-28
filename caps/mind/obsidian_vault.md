# `obsidian_vault`

| 项目 | 值 |
|---|---|
| 域 | [`mind`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `provision` / `remember` / `sync_page` / `bind` / `recall` / `verify` / `where`） |
| 处理器 | `obsidian_vault` |

## 用途

Obsidian 永久记忆层（主人令 2026-09-27「让触手的吞天拥有永久记忆 Obsidian，所有触手每一根都绑定独立的 Obsidian，再把所有的 Obsidian 和本体的自研 Obsidian 双向绑定到一起互通共享」）：**227 根触手各一本独立库**（`vaults/<触手>/`：README MOC + 记忆.md + `.obsidian/app.json`，Obsidian 直接能开）· **本体的自研库**=brain_vault 认的那本（Documents\Codex\ObsidianVault）· 双向 = 触手页链回 [[GBT本体记忆]] + 本体 [[触手总索引]] 链到每一本（两条都查）。**只追加、无删除路径**；不写主人自己的库（只指向）。写主人 Documents 目录时走 filesystem_write 门（`root=documents`）。op=status/provision/remember/sync_page/bind/recall/verify/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("obsidian_vault")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show obsidian_vault          # 本页内容的终端版
gbt-caps show obsidian_vault --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("obsidian_vault", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`provision`、`remember`、`sync_page`、`bind`、`recall`、`verify`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `mind` · handler `obsidian_vault`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
