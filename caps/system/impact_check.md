# `impact_check`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | `target` |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `impact_check` |

## 用途

**影响面检查（多域监控的读数面）**（主人令 2026-10-19：「修改一个地方的时候要分出触手关注跟这个修复的地方相连的所有地方，确保你修改其他地方不会被连带故障」）：读 `state/model-pack/wiring.json` 邻接图（现读 **6301 节点 / 951536 有向边 / 单连通分量 100%**），给一个目标（能力位名 / 代码路径 / 页面路径）就算出它 1~2 跳的影响面。**不是 selfscan**（那是框架五维自检），本位只管刀口宽度。op=status（图的规模·连通性·构建时间，取不到如实报 missing 不编 0）· op=impact（必填 target 或 targets，depth≤3 ⇒ 影响面构成 + **1 跳必验清单**；目标不在图里**如实拒绝**，绝不把空集当"没影响"）· op=risky（n ⇒ 按 1 跳邻居数排最危险的件，并如实标注"本图不分强弱边"）· op=where。**全部纯读免门**：不写盘、不出网、不起进程。已知读数：`code:gbt_allinone/api.py` 1 跳 = 337 个能力位 · depth=2 = 4859 节点 · `cap:tentacle_arm` 2 跳 = 342 节点

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("impact_check")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show impact_check          # 本页内容的终端版
gbt-caps show impact_check --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("impact_check", {'op': '<见描述>', 'target': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `target` | 是 | target=要查的目标，如 code:gbt_allinone/api.py / cap:tentacle_arm / holo_pet_w3/omni-arm/index.html；**op=status / risky / where 不用传**；也可用 targets=[…] 一次查多处；depth 默认 2（上限 3） |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `impact_check`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
