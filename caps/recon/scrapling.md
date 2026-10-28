# `scrapling`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `scrapling` |

## 用途

网页抓取（Scrapling 0.4）：自适应选择器+反爬对抗；只抓公网（每个 URL 过 net_guard 边界，内网一律拒）；缺库如实报缺不冒充；响应体限量 2MB；浏览器级隐身抓取需另装内核，缺哪个说哪个

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("scrapling")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show scrapling          # 本页内容的终端版
gbt-caps show scrapling --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("scrapling", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `scrapling`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
