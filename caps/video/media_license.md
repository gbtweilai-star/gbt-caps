# `media_license`

| 项目 | 值 |
|---|---|
| 域 | [`video`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位一动作 |
| 处理器 | `media_license` |

## 用途

素材许可账（三方向流程台「家规第 2 条：没有许可的素材不许进成品格」的数据源）：`register` 逐件登记（**现算 sha256** + 出处 + 授权 + 时间）、`unregister` 撤销（**必须写 why**，留档在 removed）、`status`/`list`/`check` 只读核对（账↔盘：陈旧 / sha 对不上 / 漏登）。🔴 **source 与 license 为空一律拒绝**——空着的许可记录比没有记录更坏（让人以为查过了）。只登记盘上真有的仓内素材；写面只落 `projects/_shared/licenses/`。**只登记与核对，不判定授权是否真实/充分**（那是主人的事）。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("media_license")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show media_license          # 本页内容的终端版
gbt-caps show media_license --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("media_license", {})
```

## 参数

该位不要求入参，空调用即可成立。若实现需要更多上下文，按描述里的说明补 `payload`。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。

## 出处

- 注册表：`caps_registry.py` · 域 `video` · handler `media_license`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
