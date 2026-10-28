# `hf_voice`

| 项目 | 值 |
|---|---|
| 域 | [`voice`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `arms` / `models` / `sing` / `rotate` / `verify` / `where`） |
| 处理器 | `hf_voice` |

## 用途

Hugging Face 歌声/语音（**3 臂轮询**，主人令 2026-09-28「把插件连接好部署语音…安装 3 个这个插件轮询使用避免卡壳」）：本机零算力跑不动歌声合成（语音中枢 v2.0 一手实测）⇒ 真唱走云。**3 臂（hf-1/2/3）按轮询 + 冷却换道**用（与 key_gateway 同一纪律）：单臂连续失败 3 次冷却 300s、自动投下一臂 ⇒ 避免单点卡壳。**出网硬钉**：只 https + 主机白名单（HF 三个官方域）+ 显式拒私有/环回/保留地址 + 拒重定向；**只回掩码**，密钥只走 env:/vault: 引用。`sing` 过 external_llm 门；模型表全部**未验**（本机无 token）。op=status/arms/models/sing/rotate/verify/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("hf_voice")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show hf_voice          # 本页内容的终端版
gbt-caps show hf_voice --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("hf_voice", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`arms`、`models`、`sing`、`rotate`、`verify`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `voice` · handler `hf_voice`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
