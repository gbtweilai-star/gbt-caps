# `code_patch`

| 项目 | 值 |
|---|---|
| 域 | [`tools`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | `path`, `find`, `replace` |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `code_patch` |

## 用途

**改代码的唯一过门入口**（2026-09-23 接）：此前 agent 直接 edit/write 落盘 ⇒ **不过门、没审计、没信封、没改前改后凭据**。三原语 dry_run（**默认，只算不写**）/ apply（落盘，挂 filesystem_write）/ rollback（按回执退回）。九道机械闸：**仓内**（路径解析后必须在仓内）· **find 恰好一次**（0 次 not_found；>1 次 ambiguous —— **绝不替你挑一个**）· **空改动拒写** · `expect_sha256` 对不上拒（防拿陈旧内容改）· **二进制拒改**（前 8KB 有 NUL）· >4MB 拒改 · **逐字节替换**（换行/BOM 一个字节不动 —— 文本层替换会把整个文件行尾改掉）· **原子写**（tmp+os.replace）· **回执可回滚**（记 find/replace/改前改后哈希；回滚前先核 after_sha256，对不上就拒）。type=internal

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("code_patch")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show code_patch          # 本页内容的终端版
gbt-caps show code_patch --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("code_patch", {'op': '<见描述>', 'path': ..., 'find': ..., 'replace': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `path` | 是 | path=仓内相对路径；find=必须**恰好出现一次**的原文；replace=新文；默认 op=dry_run（只算不写），要落盘给 op=apply（要 filesystem_write 授权） |
| `find` | 是 | path=仓内相对路径；find=必须**恰好出现一次**的原文；replace=新文；默认 op=dry_run（只算不写），要落盘给 op=apply（要 filesystem_write 授权） |
| `replace` | 是 | path=仓内相对路径；find=必须**恰好出现一次**的原文；replace=新文；默认 op=dry_run（只算不写），要落盘给 op=apply（要 filesystem_write 授权） |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `tools` · handler `code_patch`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
