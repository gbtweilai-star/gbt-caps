# `vision_print`

| 项目 | 值 |
|---|---|
| 域 | [`vision`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`store` / `vision_print` / `ledger`） |
| 处理器 | `vision_print` |

## 用途

**视觉打印**（主人令 2026-10-13「看到的东西都可以原样以代码打印并渲染成看到的样子」）：五段链 —— ①see 原生眼取帧（`tentacle/omni_core._screen_capture`：dxcam→mss→pyautogui，或直接喂图）②print 码落地（**码由她/调用方给**，本件**不编码**）③render 真 Chromium/Edge 渲（纪律同 `render_page.py`：只放行 file:/data:/blob:，其余**逐条记拦获**；pageerror / console / requestfailed 三条都记）④diff 与所见帧比（指纹尺子**只许一把**：`tentacle/vision_bus`）⑤judge 成档。**五个现算数**：aHash 汉明距离 · 块变化率 · 平均亮度差 · **变化像素占比** · **最大块平均差**（后两个是局部敏感项 —— 本件自测实测：只改一处文字颜色时整图 aHash 距离 = 0，靠这两个数才抓到，否则就是假绿）。档位 同款/接近/不像 写在 `_BANDS`（可复核可改）。抽不出代码块 ⇒ 如实报 no_code（不拿散文去渲）；`op=ask_model` 的看图回码靠**外部视觉模型**（她的底座是 Qwen2，**没有视觉塔**），缺依赖如实报 needs_dependency。每跑一次落 `store/vision_print/ledger.jsonl`（只追加）+ 框架审计一条。op=see/print/diff/loop/ask_model/status/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("vision_print")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show vision_print          # 本页内容的终端版
gbt-caps show vision_print --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("vision_print", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `store`、`vision_print`、`ledger`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `vision` · handler `vision_print`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
