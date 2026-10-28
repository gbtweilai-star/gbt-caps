# `offload_distill`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `where` / `mechanism` / `map` / `probe`） |
| 处理器 | `offload_distill` |

## 用途

**内存墙蒸馏件**（Edge0 思路 → 我们的运行纪律 + **触手映射**）。上游 `Edge0-AI/Edge0`（**Apache-2.0** · ★4612 · arXiv 2609.18063）做到「35B 只吃 ~2.5 GB 内存」。四条机制：**权重离芯**（SSD 流式 + mmap 懒读）· **槽位+LRU+双缓冲**（每步零主机同步）· **prerouter 提前一步预判**（IO 与前向重叠 · 吞吐最高 +59%）· **Recover-LoRA**（int4 底座 + 蒸馏小适配器补质量 · **适配器不合并**）。常用说法：内存压缩 / 省内存 / 流式加载 / 权重放盘 / 预取 / 量化 / LoRA / 内存墙 / 跑大模型。op=status/where/mechanism/map/probe：`mechanism` 逐条给「**上游原文** → 我们的话 → 对我们用处 → 判据」；`map` 给**触手映射**；`probe` **只读现读**本机就绪面（内存/磁盘/工具）并**逐条路线说能不能走**。铁律：**只蒸思路不搬代码 · 只读上游零执行**（不装依赖、不下 23 GB 权重）· **边界不许说反**（本机跑不了它的 MLX 路线；我们是 dense 不是 MoE）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("offload_distill")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show offload_distill          # 本页内容的终端版
gbt-caps show offload_distill --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("offload_distill", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`where`、`mechanism`、`map`、`probe`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `offload_distill`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
