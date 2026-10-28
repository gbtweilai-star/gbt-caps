# `voice_studio`

| 项目 | 值 |
|---|---|
| 域 | [`voice`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `capabilities` / `transcribe` / `plan` / `mcp_info` / `where`） |
| 处理器 | `voice_studio` |

## 用途

VoiceStudio（debpalash · AGPL-3.0 · 只蒸馏思想不搬代码）**两层面**。① **桥接面**（要上游后端在线）：status/capabilities/transcribe/plan/mcp_info/where —— 上游 Local API 现读**只给「听」不给「说」**（/v1/audio/transcriptions + WS 流式 + MCP，**没有 TTS 端点**，合成在 Electron 应用本体里）⇒ 要出声走 `voice`(SAPI) 或 `hf_voice`(云)，要克隆得上游装应用且声纹需主人授权。② **三工作流面**（AI 短剧/电影/音乐 · **纯本地、零引擎、零出网**）：`cast` 角色↔音色台账（state/voice-cast.json，三工作流共用的音色一致性根）· `align` 音频节奏测绘（ffmpeg→20ms 帧能量→门限切段→每句 start/end/dur，**切不出就报 0 段不编时间轴**）· `fit` 台词→时长预算（CJK 按字/西文按词，给每行秒数与建议语速）· `subtitle` 段+行→SRT（**行数≠段数就拒**，绝不硬配）· `say` 台词→音频（engine=edge 云端 / sapi 本机 / upstream 转发；缺网或缺引擎如实报，音色名不对先拒不去撞网）· `timeline` 每句一音频件→按**实测时长累加**出精确边界与 SRT（`wrap` 按标点折行）· `brief` 三工作流各自的语音配方。写面自收窄在 state/ 与 projects·outputs·.scratch（只有 cast 的 set/rm 与 subtitle 落盘会写，落盘限 projects·outputs·.scratch）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("voice_studio")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show voice_studio          # 本页内容的终端版
gbt-caps show voice_studio --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("voice_studio", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`capabilities`、`transcribe`、`plan`、`mcp_info`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `voice` · handler `voice_studio`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
