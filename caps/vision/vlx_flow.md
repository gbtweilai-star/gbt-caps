# `vlx_flow`

| 项目 | 值 |
|---|---|
| 域 | [`vision`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`gbt_allinone` / `tentacle` / `vision_bus`） |
| 处理器 | `vlx_flow` |

## 用途

**流式观察 + 两层记忆**（接自 om-ai-lab/VLX-Flow · 七步法第一步落 _upstream/VLX-Flow/）。上游当前是**纯文档仓**（Checkpoints: Coming soon）⇒ 按七步法「招一 纯逻辑直取」取它的**架构契约**、按「招三 手用我们自己的」语义那步留给自己的模型链。落点**长在现有眼上**：视觉缓存层复用 gbt_allinone/tentacle/vision_bus.py（snapshot / _ahash / diff_regions / stream_record / stream_replay）；语义记忆层**本件新增**，落 store/vision/semantic_memory.jsonl（**只追加**）。op=status/memory/timeline/recall/digest/remember（读面免门 · digest+remember 过 filesystem_write）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("vlx_flow")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show vlx_flow          # 本页内容的终端版
gbt-caps show vlx_flow --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("vlx_flow", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `gbt_allinone`、`tentacle`、`vision_bus`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `vision` · handler `vlx_flow`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
