# `quant_plan`

| 项目 | 值 |
|---|---|
| 域 | [`llm`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `plan` / `layer` / `route` / `speed` / `check`） |
| 处理器 | `quant_plan` |

## 用途

**压缩与直达**（主人令 2026-10-16 深度蒸馏自 Bonsai 2 27B）：把**压缩体积**与**直达线路**变成她的原生能力。①压缩：每档 bits/weight ⇒ 估算体积（27B × b/w ÷ 8 × 容器开销 1.3）⇒ 能否落在 8GB 级；参考一手读数（ternary PTQ1_0 = 1.75 b/w · 语言模型 7.67GB · 保留 98.2% FP16 · 同体积胜 IQ2_XXS 12 分）。②直达：意图 ⇒ 能力位 ⇒ 车道 ⇒ 端点，每步都有固定落点、不经本机中转。③执行层三层映射（路由/搬运/内存）对接已施工图。铁律：本地不承载任何大模型（主人 2026-10-08 与 10-16 令），端点不许写 127.0.0.1。op=status/plan/layer/route/speed/check（全只读·零作用域）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("quant_plan")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show quant_plan          # 本页内容的终端版
gbt-caps show quant_plan --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("quant_plan", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`plan`、`layer`、`route`、`speed`、`check`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `llm` · handler `quant_plan`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
