# `tentacle_scale`

| 项目 | 值 |
|---|---|
| 域 | [`tentacle`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`space` / `addr` / `parse` / `shard` / `key` / `master`） |
| 处理器 | `tentacle_scale` |

## 用途

亿万触手寻址（逻辑 · 只读）：10^8 地址空间按算不占盘（t00000001…）+ 1024 分片 + 每根钥匙由主密钥 HMAC 派生（同一根永远同一把、彼此不同、可复算）· 钥匙只回指纹。**实体化/落盘不做**（新增位无 policy 分支 = 零作用域，属登记在册的坑，要开请主人在 security/policy.py 挂作用域）；主密钥不在就如实报「未配」，不代建。op=space/addr/parse/shard/key/master

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("tentacle_scale")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show tentacle_scale          # 本页内容的终端版
gbt-caps show tentacle_scale --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("tentacle_scale", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `space`、`addr`、`parse`、`shard`、`key`、`master`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `tentacle` · handler `tentacle_scale`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
