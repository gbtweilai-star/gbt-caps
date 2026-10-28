# `pod_link`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `ls` / `up` / `down` / `run` / `where`） |
| 处理器 | `pod_link` |

## 用途

**云卡触手**（她自己的传输器官：本机 ⇄ GPU 卡 · 在卡上跑命令 · 看卡状态）。op=status/ls/up/down/run/where：`status` 读卡清单（id/状态/价/卷/端口/公网IP）+ Jupyter 通不通；`ls` 列卡上目录；**`up` 本机→卡**（字节级 base64 上传，**传完回读对账 sha256**）；**`down` 卡→本机**（`/files` 取回 + 落盘对账）；**`run` 在卡上跑一段 Python**（内核通道）。常用说法：传上云 / 从卡上取回来 / 在卡上跑 / 卡上现在有什么 / 云卡 / 4090 / GPU 传输 / 上云。铁律：**令牌不回显**（只报已配/未配）· **传完必须回读对账哈希**（不一致一律 ok=false）· **不创建/不删除/不重启 Pod**（花钱动作要主人点头）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("pod_link")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show pod_link          # 本页内容的终端版
gbt-caps show pod_link --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("pod_link", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`ls`、`up`、`down`、`run`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `pod_link`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
