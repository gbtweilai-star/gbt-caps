# `rea_reverse`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `knowledge` / `commands` / `plan` / `cli` / `where`） |
| 处理器 | `rea_reverse` |

## 用途

REA 桥 —— 吞天吞进来的第一件「能装能跑」的外部能力（主人 2026-10-11 图片 ⇒ devour_github 真吞成胶囊 devoured_morluto_rea；上游 https://rea.tools/ · morluto/rea · npm rea-agents 6.4.0 · MIT）。给编码助手装上「逆向 / 反编译 / 无源码看懂程序」的取证面：Ghidra/IDA/Hopper 与 JS-Electron / .NET / APK / 网页 / 抓包，每条结论带证据与局限。**本位只读、零作用域、执行面故意没接**：status 现读本机 PATH 与胶囊 + 探测时刻的版本账（state/rea_probe.json）· knowledge 读吞噬胶囊正文 · commands 列真 help 解析出的 129 条命令名（带 help 指纹）· plan 只出可直接照抄的命令行（含 setup 的拒绝理由：它会改写各 agent 配置）· where 契约。**要接执行面**：先给 security/policy.py 加 kind == rea_reverse 分支（读类零 · 跑类 process_execute · 未知 op fail-closed），**执行面走已有的手**：cli（dry=False）把命令交给 desktop_commander 起进程 —— 门在它身上（process_execute），本位自身不起进程、不私接 subprocess；setup 一律拒（会改写别的 agent 配置）。op=status/knowledge/commands/plan/cli/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("rea_reverse")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show rea_reverse          # 本页内容的终端版
gbt-caps show rea_reverse --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("rea_reverse", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`knowledge`、`commands`、`plan`、`cli`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `rea_reverse`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
