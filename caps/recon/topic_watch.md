# `topic_watch`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | `need` |
| 形态 | 一位多操作（入参含 `op` / `action` 选择器） |
| 处理器 | `topic_watch` |

## 用途

话题追踪：追踪/盯着/有变化/告诉/话题/持续关注/每天给我/早报/动态/最新/行业/新闻/股价/行情/视频。追踪你关心的话题，梳理最新动态，有变化就告诉我。触发词表全量见 topic_watch.INTENT_MAP；命中后转邻域技能链，不新增进程、不复制技能实现。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("topic_watch")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show topic_watch          # 本页内容的终端版
gbt-caps show topic_watch --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("topic_watch", {'op': '<见描述>', 'need': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `need` | 是 | 一句需求，例如「帮我盯着 AI 行业动态」（op=route 默认路必需） |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `topic_watch`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
