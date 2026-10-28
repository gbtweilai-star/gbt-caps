# `lobehub`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`state` / `surfaces` / `lobehub`） |
| 处理器 | `lobehub` |

## 用途

LobeHub 桌面端（Electron 2.2.18）全控 —— 主人令 2026-09-27「把 LobeHub.lnk 做成**可执行的插件**装到工具区，功能是真的多，**只要是可控制的都要绑上**」：**七大面 76 把可控制键**（设置 23 + **可控制按键 4** + 桌面端真调的接口操作 27 + 助理 9 + 目录 9 …），每把都在 state/surfaces/lobehub.json，**消失即断连**。硬口径：凭据只回形状、**按键名掩码**（密文永不回值）· 在跑的库只读**副本** · 本地文件桥只连 127.0.0.1 且端口取自应用自己的日志（**非 ASCII 路径实测撑不住**，如实标）。launch/close 过 process_execute 门；settings 写=白名单 + filesystem_write 门 + 先备份。op=status/surface/settings/shortcuts/ops/agents/runtime/bridge/launch/close/verify/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("lobehub")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show lobehub          # 本页内容的终端版
gbt-caps show lobehub --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("lobehub", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `state`、`surfaces`、`lobehub`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `lobehub`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
