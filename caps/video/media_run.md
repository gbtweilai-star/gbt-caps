# `media_run`

| 项目 | 值 |
|---|---|
| 域 | [`video`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `media_run` |

## 用途

三方向自动化工作流**执行器**：一次调用把一条链从头走到尾，每步落真件 + 同批登记许可。链取自 `media_pipeline.KINDS`（music: lyrics→arrangement→audio→master→export · short_video: script→storyboard→assets→edit→export · film: concept→script→shots→sound→edit→export）。🔴 **没有实现器的步如实标 `not_implemented`**（人/未实现的活不许当成跑过了）；自产输入（本机 ffmpeg 合成）⇒ 许可可如实写自有。落点只在 `projects/<方向>/<格>/`，命名合家规。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("media_run")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show media_run          # 本页内容的终端版
gbt-caps show media_run --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("media_run", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。

## 出处

- 注册表：`caps_registry.py` · 域 `video` · handler `media_run`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
