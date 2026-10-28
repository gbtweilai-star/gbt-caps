# `install_selfcheck`

| 项目 | 值 |
|---|---|
| 域 | [`security`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`cron` / `systemd` / `rc`） |
| 处理器 | `install_selfcheck` |

## 用途

**装机自检 · 查病毒木马/后门**（主人 2026-10-17 令「安装上我们的大模型就自动自检一遍排除病毒木马等」）：按 **OS 结构**做只读检查 —— Windows(Run/RunOnce 自启键·计划任务·服务·Winlogon·监听端口·PE 头) · Linux(cron/systemd/rc.local/ld.so.preload·ELF·setuid) · macOS(LaunchAgents/Daemons·Gatekeeper/隔离位·SIP·Mach-O)；跨平台戳危险特征（powershell -enc·mshta 远程·certutil-urlcache·bitsadmin·curl|bash·base64 执行·反连 shell）· 双扩展名/伪装脚本/隐藏可执行；模型文件复核 sha manifest。**只读**：命中≠定罪，不擅自杀/删，给人工复核与建议。op=status/scan/persistence/plan/where

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("install_selfcheck")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show install_selfcheck          # 本页内容的终端版
gbt-caps show install_selfcheck --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("install_selfcheck", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `cron`、`systemd`、`rc`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `security` · handler `install_selfcheck`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
