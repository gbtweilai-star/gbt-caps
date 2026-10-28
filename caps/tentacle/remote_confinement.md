# `remote_confinement`

| 项目 | 值 |
|---|---|
| 域 | [`tentacle`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `remote_confinement` |

## 用途

**执行者隔离**（主人 2026-10-09 点破：「沙盒隔离的是被测试的靶标，没隔离执行的人」）：exec 中继若在宿主以主人账号跑，云端敲的命令就跑在真机上。op=assess/verdict 现读执行身份（whoami+是否提权）与三条隔离路（Docker 守护/WSL 发行版/低权账号）**并真验每条能不能跑**；ttl 读看门狗（中继最长 TTL）；grant **只查**主人发的 remote_device 票（AI 不发）；guard 是启中继前的最后一道闸：**未隔离 + 无票 ⇒ 一律拒启**（fail-closed），拒了说清怎么开。本件已焊进 desktop_commander.remote_start。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("remote_confinement")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show remote_confinement          # 本页内容的终端版
gbt-caps show remote_confinement --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("remote_confinement", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 见「用途」）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `tentacle` · handler `remote_confinement`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
