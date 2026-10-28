# `bits_kit`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `build` / `find` / `api` / `where`） |
| 处理器 | `bits_kit` |

## 用途

**动效组件图鉴的口**（人话 → react-bits 哪个组件 · 干什么 · **源码在哪 · 会不会联网 · 依赖什么**）。素材：`DavidHDev/react-bits`（**MIT + Commons Clause v1.0** · ★49005 · 216 组件 · 5 类：Animations 39 / Backgrounds 62 / Components 48 / Micro 34 / TextAnimations 33）落 `_upstream/react-bits`。常用说法：动画 / 背景 / 文字动画 / 微交互 / 手风琴 / 画廊 / 卡片 / 光标跟随 / 粒子 / 网格 / 渐变 / 流光 / 毛玻璃 / 滚动 / 计数 / 故障 / 极光 / 波浪 / 液态 / 三维 / 音频 / 拖拽 / 轮播 / 开关 / 加载 / 翻牌 / 解密 / 描边 / 磁性。op=status/build/find/api/where：`build` 扫 `src/content`（**盘上目录是真相**）提 名·类目·说明（取自官方 `public/llms.txt`）·源码路径·注册表·依赖·**联网标**，落 `store/bits_kit/index.jsonl`（只追加），并把「清单与盘上对不上的地方」如实带出来；`find` 人话取候选（**命中 0 就是 0**，可 `only_offline=true` 只看不联网的）；`api` 按准确名取一条。🔴 铁律：**只读 · 零执行 · 不搬成品**（许可禁止再分发/移植）· **不碰 `public/rbp/**`**（付费版 Pro）· **不改 `_upstream/react-bits/**` 一个字节** · 说明只取原文，取不到留空。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("bits_kit")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show bits_kit          # 本页内容的终端版
gbt-caps show bits_kit --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("bits_kit", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`build`、`find`、`api`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `bits_kit`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
