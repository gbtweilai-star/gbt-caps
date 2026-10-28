# `project_drift`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`bytes` / `mtime` / `sha16`） |
| 处理器 | `project_drift` |

## 用途

**全项目变化监控（第三块监控：全控变化）**（主人 2026-10-19：「多余监控还缺了一个全控变化，也就是要有一个看着整个项目变化的」）：跟 heartbeat（每根触手还通不通）与 impact_check（这一刀会撞到谁）并列 —— 本位回答「**整个项目从基线到现在变了什么、变得合不合理**」。基线不重扫全仓：把 `outputs/repo-pack/files.jsonl`（308,075 件 · 带 bytes/mtime/sha16）收成基线，每次只 stat 一遍，**只对变了的少数件真算 sha16**（单件 >8MB 与超出预算的如实标「内容未验」，不冒充没变）。op=status（基线在哪·多旧·覆盖多少件；没基线就明说"还不知道"）· op=drift（新增/改动/删除/仅碰时间 四类 + 异常项 + 用时；**mtime 早于基线时刻的差异归「基线漏收/旧差异」，不当新变化报**）· op=baseline（冻结新基线，写盘 ⇒ filesystem_write 挂在处理器层）· op=where。异常判据五条：在役/冻结/敏感面被动 · 成批变动(新增>500/删除>100) · 新增可执行件 · 0 字节新件 · 基线过期>24h。实测：全仓 stat 一遍 93 s / 308,291 件

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("project_drift")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show project_drift          # 本页内容的终端版
gbt-caps show project_drift --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("project_drift", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `bytes`、`mtime`、`sha16`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `project_drift`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
