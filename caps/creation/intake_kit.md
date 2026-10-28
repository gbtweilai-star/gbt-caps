# `intake_kit`

| 项目 | 值 |
|---|---|
| 域 | [`creation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`status` / `build` / `find` / `api` / `where`） |
| 处理器 | `intake_kit` |

## 用途

**外部件接入图鉴**（七件 · 七步法全走）：身份 · 许可 · **只读体检读数** · 知识面在哪。素材落 `_upstream/`：`motionsites.ai`（65 条设计提示词）· `impeccable`（设计语言系统 · 24 份 SKILL）· `hyperframes`（HTML→视频 · 40 份 SKILL）· `ai-engineering-from-scratch`（20 阶段 + 26 份 SKILL）· `Agent-Reach`（15 平台读取/搜索 CLI · llms.txt + docs）· `ponytail`（少写代码规则包 · 12 份 SKILL）· `DeepSeek-Bot`（长期存活 Bot 团队 · bot 间传话 · 群聊轮流发言 · 上下文管家 + FTS5 全文索引）。常用说法：设计提示词 / 落地页 / 设计语言 / 少写代码 / 读网页 / 搜索全网 / 视频渲染 / 学习路径 / 课程 / 长期存活 / bot 团队 / 群聊 / 上下文管家 / 记忆。op=status/build/find/api/where：`build` 扫六件的知识面（各件 `SKILL.md` · motionsites 提示词 · ai-engineering 阶段 · Agent-Reach 文档）⇒ 一条一行（**带 `文件#L行号`**）落 `store/intake_kit/index.jsonl`；`find` 人话 → **该读哪一件的哪一份**（**命中 0 就是 0**）；`api` 按准确名取一条。铁律：**只读 · 零执行 · 零出网**（不装依赖、不跑它们的代码）· **不改 `_upstream/**` 一个字节** · **体检读数带日期**（2026-10-13 探针），不许当实时值念。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("intake_kit")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show intake_kit          # 本页内容的终端版
gbt-caps show intake_kit --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("intake_kit", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `status`、`build`、`find`、`api`、`where`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `creation` · handler `intake_kit`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
