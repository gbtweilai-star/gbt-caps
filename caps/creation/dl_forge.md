# `dl_forge`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `chain` / `map` / `find` / `plan` / `gaps` / `sources`） |
| 处理器 | `dl_forge` |

## 用途

3D 锻造融合位（只读骨架）：**秋叶节点 × 原生触手 × 专业标尺 三合一**。主人令「把学到的跟秋叶版的哪些节点以及契约，和我们的原生触手融合，实现原生能力也能做出高级作品和 3D 建模，都要达到专业水准」。**八段链**：①形象进件(控图预处理) ②图生3D ③网格(体素→网格/减面/平滑) ④贴图与烘焙 ⑤绑骨与权重 ⑥动作 ⑦渲染 ⑧交付(钢印+LOD+达标)。每段写清「秋叶有哪些节点（2027 契约里 3D 相关 **96 个真名**）/ 派哪根原生触手 / 判据是什么」。融合公式=**秋叶节点（怎么做）× 原生触手（谁来做）× 专业标尺（算不算达标）**。op=status/chain/map/find/plan/gaps/sources

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("dl_forge")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show dl_forge          # 本页内容的终端版
gbt-caps show dl_forge --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("dl_forge", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`chain`、`map`、`find`、`plan`、`gaps`、`sources`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `dl_forge`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
