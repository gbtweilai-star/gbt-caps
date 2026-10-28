# `art_brief`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `where` / `plan` / `run`） |
| 处理器 | `art_brief` |

## 用途

**作品策划位**（人话一次问，四路知识同时到位 + 给出可直接照抄的出片命令）。四路： `ui_kit` **可渲件**（纯 HTML/CSS，能直接进渲染器）· `bits_kit` **参考件**（react-bits 的 React 实现，**只读来学**——许可禁止再分发/移植）· `motion_kit` **动效API**（anime.js 真 API，带签名与 `文件#L行号`）· `design_atlas` **技法节**（18 份手册里该读哪一节，带 `文件#L行号`）；出片交给 `art_chain`。常用说法：出作品 / 做个动效 / 一键出图 / 帮我策划一下 / 这个效果怎么做。op=status/where/plan/run：`plan` 走**四路零作用域的读**（命中 0 就是 0，**不拿别的路凑数**，缺哪一路就如实列出来）并给出 `art_chain` 的下一步命令；`run` 真出片，失败**停在原地**并原样带出`inner_*`（内层门缺什么）。铁律：每路都走既有门 `run_task`（不直连模块、不绕门、不重写任何一环）· 缺就如实报缺 · `bits_kit` 那一路只读来学、**不搬成品**。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("art_brief")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show art_brief          # 本页内容的终端版
gbt-caps show art_brief --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("art_brief", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`where`、`plan`、`run`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `art_brief`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
