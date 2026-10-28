# `ui_kit`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `build` / `find` / `take` / `where`） |
| 处理器 | `ui_kit` |

## 用途

**UI 组件库的口**（吞天吞来的素材 → 可检索 · 可取件 · 读数如实）。素材：`uiverse-io/galaxy`（**MIT** · ★13478 · 3802 件 · 11 类目）落 `_upstream/galaxy`。常用说法：UI 组件 / 按钮 / 卡片 / 加载动画 / 开关 / 输入框 / 表单 / 复选框 / 工具提示 / 通知 / 悬浮提示 / 图案 / 霓虹 / 渐变 / 毛玻璃。op=status/build/find/take/where：`build` 扫素材提语义（类目·可见文案·效果标签·主色·外链数）落 `store/ui_kit/index.jsonl`（只追加）；`find` 人话取件（**命中 0 就是 0，不硬塞**）；`take` 拷一件到 `outputs/ui-kit/` 并**如实报它带几条外链**。铁律：**零出网 · 零执行**（不跑组件里任何东西）· **不改 `_upstream/galaxy/**` 一个字节** · 效果标签只认代码里真出现的特征串。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("ui_kit")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show ui_kit          # 本页内容的终端版
gbt-caps show ui_kit --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("ui_kit", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`build`、`find`、`take`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `ui_kit`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
