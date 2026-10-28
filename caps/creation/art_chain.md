# `art_chain`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `art_chain` |

## 用途

**作品链**（一条命令：挑组件 → 取件 → **真渲** → 调优，每步带读数）。① `ui_kit.find(q)` 挑头一件（带外链数）② `ui_kit.take` 拷进 `outputs/art-chain/`③ 调 `render_page.py` **真 Chromium 渲**（该件自带禁网 + 逐条记拦获）④ `vision_print.polish` 清晰度+补光。常用说法：出作品 / 挑组件出图 / 一键出图 / 拿这个组件做张图。旋钮：`q`(人话) · `look`(味道，**默认「原样」= 只调旋钮不套味道**) · `size` · `sharpen` · `grain` · `grade_fmt`(.png 无损)。铁律：每步走**既有门/既有件**（不重写渲染器、不绕门）· 失败**停在原地并说清哪一步**（不把半成品念成作品）· 上游 `_upstream/galaxy/**` 一个字节不动。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("art_chain")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show art_chain          # 本页内容的终端版
gbt-caps show art_chain --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("art_chain", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `art_chain`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
