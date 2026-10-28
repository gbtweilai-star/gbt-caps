# `comfyui`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`checkpoints` / `loras` / `controlnet`） |
| 处理器 | `comfyui` |

## 用途

ComfyUI（秋叶整合版）全控（主人令 2026-09-27「这个必须也是一个不漏的双向绑定，才能实现无限制审查生产」）：**966 个节点**（每把一把键）+ 11 个 API 端点 + 14 个启动开关 + 模型清单（checkpoints/loras/controlnet）；**节点消失=断连**（要解释或补）。出网硬钉（SSRF 防线）：只许本机 http + 主机白名单(127.0.0.1/localhost/::1) + 端口 8188 + 路径前缀白名单 + **拒重定向**；读类直连、提交/释放过 filesystem_write 门。op=status/nodes/models/submit/queue/history/free/interrupt/surface/verify

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("comfyui")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show comfyui          # 本页内容的终端版
gbt-caps show comfyui --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("comfyui", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `checkpoints`、`loras`、`controlnet`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `comfyui`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
