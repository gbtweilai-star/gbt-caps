# `sec_sweeper`

| 项目 | 值 |
|---|---|
| 域 | [`security`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`eval` / `exec` / `shell`） |
| 处理器 | `sec_sweeper` |

## 用途

安全棒（主人令 2026-09-27）：一根专职安全触手，**每半天**把尺子挨个过唯一门跑一遍 —— 全量穿透式交叉扫描（钩子/步骤锁/交叉验证/遗漏补扫）+ 安全模式分诊（eval/exec/shell/凭据/反序列化…）+ 覆盖无死角 + 双向绑定 + 技能源↔装；结果收成**健康账**，异常即**报警**；**独立健康面板**（快照内联·异常红色置顶）；**专用口**=keys（只引用+掩码）/energy（能源池+免费池真连）/start；**同步记忆上下文**=每棵树记指纹（文件数/最新mtime/总字节），指纹未变则复用上次结果（标 reused），**不重扫**。op=start/sweep/keys/energy/panel/health

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("sec_sweeper")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show sec_sweeper          # 本页内容的终端版
gbt-caps show sec_sweeper --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("sec_sweeper", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `eval`、`exec`、`shell`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `security` · handler `sec_sweeper`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
