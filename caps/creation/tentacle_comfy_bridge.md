# `tentacle_comfy_bridge`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`store` / `tentacle_comfy` / `ledger`） |
| 处理器 | `tentacle_comfy_bridge` |

## 用途

**第 1530 根触手 · ComfyUI 桥**（主人令 2026-10-11「ComfyUI 不是生图工具，是第 1530 根触手的底座」）：把外部 ComfyUI 当**贴图工厂／概念工厂**用，并**双向绑定** —— ① 工作流 = 契约（`state/comfy_workflows/*.json`，ComfyUI 原生节点连线格式）；② 产物**先过闸才允许落盘**（闸口径与 `comfy_native.gate_image` 同源：最短边/格式/非空/可解码）；③ **溯源自证**：workflow_sha256 + seed + ckpt_hash 全部落 `store/tentacle_comfy/ledger.jsonl`（只追加）。出网硬钉照抄 `comfyui_surface`：只许本机 http + 主机白名单 + 端口 8188 + 路径前缀 + 拒重定向。**不在位就如实回 needs_dependency（绝不假装出图）**；断连判据同源（节点数 < 900 = 断连）。op=status/queue/workflows/verify

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("tentacle_comfy_bridge")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show tentacle_comfy_bridge          # 本页内容的终端版
gbt-caps show tentacle_comfy_bridge --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("tentacle_comfy_bridge", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `store`、`tentacle_comfy`、`ledger`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `tentacle_comfy_bridge`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
