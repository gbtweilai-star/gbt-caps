# `freellmapi`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`api` / `auth` / `login`） |
| 处理器 | `freellmapi` |

## 用途

FreeLLMAPI（本机免费大模型池 127.0.0.1:31415，34 家供应商 / 635 免费端点汇成一个 OpenAI 兼容 /v1）**接入层的**能力位：`status` 总表（探活 + 文档 + 可选供应商读数）· `probe` 探活（`/api/ping`，**明确无鉴权**的口，不拿需要登录的端点探活以免把「没登录」误判成「服务没起」）· `docs` 文档可用性（`/v1/openapi.json`）· `models` 列免费池可用模型（`GET /v1/models`，**只要统一 key、不用登录**）· `framework_env` 算给框架网关用的环境变量（`GBT_LLM_BASE_URL/API_KEY/PROVIDER`，**只算不写盘**）· `where` 给设置页看接线契约；写面：`login`/`providers`/`list_keys`/`add_key`/`health_check`/`set_enabled`/`remove_key`/`unified_key`。⚠️ 端口**三级发现**（env → 桌面版 config.json → 默认 3001），绝不写死；实测本机为 31415。⚠️ 三条不商量纪律：① **绝不从 SQLite 掏 session token 绕过登录**（要配置就让主人登录一次走官方 /api/auth/login）② **绝不打印/返回明文密钥**（一律 mask）③ **不改 FreeLLMAPI 源码**（别人的项目，改了没法升级）。⚠️ 门禁口径与 `automation_keys` 同源：**只读面（status/probe/docs/models/framework_env）不过门**（本地回环、不花积分、不出公网）；**写面/传凭据过 `filesystem_write`**。policy.py 无本位分支（owner-only，AI 无权改）⇒ 门在模块内自闸（auth_gate 唯一校验入口），缺授权如实报缺、不绕门。safe=true（只读面为主）。type=internal

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("freellmapi")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show freellmapi          # 本页内容的终端版
gbt-caps show freellmapi --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("freellmapi", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `api`、`auth`、`login`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `freellmapi`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
