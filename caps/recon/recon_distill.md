# `recon_distill`

| 项目 | 值 |
|---|---|
| 域 | [`recon`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`claim` / `evidence` / `unknown` / `limitation`） |
| 处理器 | `recon_distill` |

## 用途

**蒸馏件**（不是外挂）：把吞入件 morluto/rea 的方法论提炼成**我们自己的**逆向取证骨架（主人令 2026-10-12「我们吞噬都是加入蒸馏提炼出契合我们的能力」「蒸馏提炼出契合我们的能力才是我们的」）。四条蒸馏：①证据契约 op=evidence（claim/evidence/unknown/limitation 四件齐才算过，「无」也要写）②静态优先 op=fingerprint（只读字节、**不执行目标**）③确定性义务现算 op=obligations（看懂/复刻一个产物还缺哪些证据，每条带判据，**不落盘**）④引擎现读 op=engines（Ghidra/IDA/Hopper/JADX/apktool/binwalk/wabt/adb… 在不在 PATH，缺就如实说缺）。op=provenance 逐条指回 REA 原话（含**未蒸馏**的如实标注）。**零作用域**：无 subprocess / 无 urllib / 无写盘。边界：接入端 ≡ rea_reverse（外部引擎那条线）；本位 ≡ 蒸出来的我们自己的判据。op=fingerprint/engines/evidence/obligations/provenance/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("recon_distill")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show recon_distill          # 本页内容的终端版
gbt-caps show recon_distill --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("recon_distill", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `claim`、`evidence`、`unknown`、`limitation`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `recon` · handler `recon_distill`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
