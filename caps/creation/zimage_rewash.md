# `zimage_rewash`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `zimage_rewash` |

## 用途

洗图流水线（看图→反推提示词→重绘→放大）：**放大环已可用**（ffmpeg lanczos+unsharp，零依赖）；反推环**已接线**（2026-10-15 起 zimage_rewash_cap 走 vision 通道；2026-10-16 增形式化反推件 tools/codex-scripts/img-reverse.py）；**语义反推**仍待外部理解通道（teamorouter 401 / 本地 8111 未监听）——缺什么就写什么；重绘环**未接线**（未装 ComfyUI；pollinations img2img 需公网可达图 URL）；含降噪强度口径表 0.15→0.85 四档。⚠️ **2026-10-13 收敛（主人令「每一个调节都要触手可控」）**：本位是**历史腿**，主腿 = `comfy_native.upscale_4k`（PIL LANCZOS + USM；`vision_print.polish` 的清晰度腿走它）。收敛**分两类做、不搞假统一**：① **几何旋钮真统一** —— `scale`（新名，倍数）＝旧名 `factor`，且都接受 `size`（目标绝对宽，按源图宽换算成倍数走同一条路）；两个名字同时给且不等 ⇒ **fail-closed**。② **锐化旋钮不统一、且显式拒** —— 本位只有 `unsharp`（**ffmpeg unsharp 滤镜的 amount**），主腿是 `sharpen`（**PIL USM 的 percent 比例**），**两个算法两个量纲**；把 `sharpen` 传给本位 ⇒ **当场 fail-closed 并指路主腿**（改名冒充＝假统一，更害人）。参数判在**过门之前**（参数错不消耗授权）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("zimage_rewash")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show zimage_rewash          # 本页内容的终端版
gbt-caps show zimage_rewash --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("zimage_rewash", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `zimage_rewash`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
