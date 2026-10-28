# `digital_human`

| 项目 | 值 |
|---|---|
| 域 | [`video`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`start` / `stop` / `status`） |
| 处理器 | `digital_human` |

## 用途

数字人「以图生视频」（本地 SadTalker，零账号/零验证）：**一张照片 + 一段配音 ⇒ 带头部动作与口型同步的说话视频**。ops：status/probe 只读（引擎·权重·venv 缺件如实报）· capabilities 读边界 · render 写（异步出片回 task_id；写面自收窄在 outputs/dh-talk/ 与 state/digital_human/）· task/jobs 读任务账 · socket start/stop/status 把本能力包成 **OpenAI 兼容端点**（只监听回环），主脑用 omni_plug.ai_control（远端 https）或 _local_ai_call（回环）反向调用 —— **对面跑的是我们自己的权重，借的只是 CPU/GPU**，换远端只改 base_url。实测边界（2026-10-19）：成片画质上限由**取景**决定（脸在画面里越小口型越看不清 ⇒ 传头肩景，如 outputs/ref/face-tight.png）；本机纯 CPU 约 13.6 s/帧（14.8s 配音≈80 分钟），GPU 通常 1~2 分钟。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("digital_human")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show digital_human          # 本页内容的终端版
gbt-caps show digital_human --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("digital_human", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `start`、`stop`、`status`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `video` · handler `digital_human`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
