# `image_scout`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`min_width` / `min_height` / `aspect` / `license` / `extension`） |
| 处理器 | `image_scout` |

## 用途

**美图精准抓取**（主人令 2026-10-17「去精准抓取美图能力给她注入」）：只做"找对图+把关质量与许可"，不做下载/写盘。多源（Openverse 免钥匙 CC 系 · Unsplash/Pexels 有钥匙才用）· 质量门槛（min_width/min_height/aspect/license/extension）· `curate` 按 像素量×比例契合×许可优先 排序并逐条给**署名行**。出网硬钉：只许 https + 三源白名单 + 拒重定向 + 密钥只回掩码 + **绝不下载图片字节**；缺钥匙/不可达如实报未配/未读到。修饰接棒 `zimage_rewash`（upscale lanczos+unsharp / reverse 反推提示词 / rewash 重绘）。op=status/sources/search/curate/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("image_scout")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show image_scout          # 本页内容的终端版
gbt-caps show image_scout --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("image_scout", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `min_width`、`min_height`、`aspect`、`license`、`extension`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `image_scout`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
