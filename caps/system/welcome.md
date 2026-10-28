# `welcome`

| 项目 | 值 |
|---|---|
| 域 | [`system`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `welcome` |

## 用途

**启动欢迎语**（主人令 2026-10-10：「启动APP数字人的欢迎语，你来看看说什么，要有 GBT小土豆V8 和 开发者：自由的风，其他你来想要有未来感的语言」）。文字是**单一真源**（gbt_allinone/welcome.py 的 WELCOME；必含项由 check() 机械咬住）。三个 op：text 取全文+必含项判据 · audio 预生成音频的落点与状态 · boot 启动用**一次给全**（显示什么 + 播哪个文件）。🔴 音频**必须预生成**：本机 TTS 走 CPU，约 **150 倍慢于实时**（实测 2.36 秒用 327 秒）⇒ 启动时现造要等几十分钟；造一次缓存到盘，启动直接播；**没造就如实报**，界面退化成只显示文字 —— 不许静默、不许假装播了。只读零作用域。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("welcome")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show welcome          # 本页内容的终端版
gbt-caps show welcome --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("welcome", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。

## 出处

- 注册表：`caps_registry.py` · 域 `system` · handler `welcome`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
