# `motion_kit`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `build` / `find` / `api` / `prove` / `where`） |
| 处理器 | `motion_kit` |

## 用途

**动效引擎的口**（人话 → anime.js 的真 API，并**本机原生真跑**证明引擎可用）。素材：`juliangarnier/anime`（**MIT** · ★73546 · animejs v4.5.0 · **67 导出**）落 `_upstream/anime`。常用说法：动画 / 动效 / 补间 / 时间线 / 定时器 / 滚动驱动 / 视差 / 拖拽 / 弹簧 / 回弹 / 缓动曲线 / 贝塞尔 / 步进 / 打字机 / 逐字 / 乱码 / 变形 / 沿路径 / 描边 / 交错 / 错开 / 随机 / 映射 / 插值 / 布局 / 三维 / WebGL / 作用域 / 可动画对象 / Web 动画。op=status/build/find/api/prove/where：`build` 扫 `dist/modules` 提 **API 名·模块·签名（现读 .d.ts）·定义行** 落 `store/motion_kit/index.jsonl`（只追加）；`find` 人话取候选（**命中 0 就是 0**）；`api` 按准确名取一条；`prove` **Node 原生真跑**（真算纯函数 + `consistent` 咬索引条数）。铁律：**零出网 · 零执行上游脚本 · 不改 `_upstream/anime/**` 一个字节** · 签名/说明只从 `.d.ts` 现读，取不到留空。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("motion_kit")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show motion_kit          # 本页内容的终端版
gbt-caps show motion_kit --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("motion_kit", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`build`、`find`、`api`、`prove`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `motion_kit`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
