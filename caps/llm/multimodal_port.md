# `multimodal_port`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`text` / `vision` / `image` / `video` / `code`） |
| 处理器 | `multimodal_port` |

## 用途

多模态维度 × 触手密钥 **Y 字端口**：请求在一处分叉、**一次只走一臂** ——独立臂（该维度专属密钥）/ 共享臂（共享密钥对按维度分账，须恰好成对、指纹互不相同、带 owner_ai_id 可追）；覆盖 text/vision/image/video/code 五维度，七道闸 Y0-Y6 机械把关，返回值**永不含明文**（只 key_id/掩码/指纹），没钥匙就如实报缺。status/port/catalog/redlines/selftest 为**读类直连**（port 只回密钥引用且标 readonly）；probe **真出网**探端点 ⇒ 过 external_llm 门；作用域声明挂在 cap 边界（security/policy.py::evaluate）

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("multimodal_port")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show multimodal_port          # 本页内容的终端版
gbt-caps show multimodal_port --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("multimodal_port", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `text`、`vision`、`image`、`video`、`code`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `multimodal_port`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
