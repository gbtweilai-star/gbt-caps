# `omarchy_bridge`

| 项目 | 值 |
|---|---|
| 域 | [`tentacle`](./README.md) |
| 安全标记 | `safe: false` |
| 外部依赖 | 无 |
| 入参 | 无 |
| 形态 | 一位多操作（描述中枚举：`set_theme` / `theme_install` / `dispatch` / `eval` / `plugin_`） |
| 处理器 | `omarchy_bridge` |

## 用途

**Omarchy 桥**（2026-10-15 主人拍 A 案：小土豆住进 Omarchy 当智能层）。接官方三根线：① `omarchy` CLI（含 `commands --json` 机读）；② `omarchy-shell` 的 UNIX-socket IPC（socket 名 = md5(OMARCHY_PATH/shell+WAYLAND_DISPLAY)，**现算不写死**）；③ `hyprctl` + `$XDG_RUNTIME_DIR/hypr/*.sock`（排窗/切工作区）。op=assess 现读两侧（宿主能不能接 · WSL 里装没装）· list 读命令表 · probe_wsl 探 WSL 痕迹 ·theme_list 读主题表 · **events 读窗口事件流**（$XDG_RUNTIME_DIR/hypr/<HIS>/.socket2.sock，逐行 EVENT>>DATA；**一次性读取、读完即断** —— 官方说过该 socket 同步求值，挂着会冻结）· window（activewindow）· clients（打开的窗口列表）（以上只读）；set_theme/theme_install/dispatch/eval/plugin_* 是写类。两条纪律：**没装就如实报**（ok=false + reason，绝不假装接上）；**写类 fail-closed**（不在 Omarchy 会话里就拒，并说清怎么开）。**WSL2 里跑不了 Hyprland**（无 DRM/KMS）⇒ WSL 那栏只做"装没装"的探针，不做"接上桌面"的承诺。本件不装 Omarchy、不写它的配置。

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("omarchy_bridge")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show omarchy_bridge          # 本页内容的终端版
gbt-caps show omarchy_bridge --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("omarchy_bridge", {'op': '<见描述>'})
```

## 参数

注册表**没有**为这一位登记入参契约，但它是多操作形态：实际调用要带 `op` / `action` 选择分支（描述里枚举的是 `set_theme`、`theme_install`、`dispatch`、`eval`、`plugin_`）。

这是数据源里的一处不一致——规格照实呈现，不做猜测。

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: false`：属于**要人签字的动作**。按本仓的配套做法，应先过 `consent-gate` 一类的人工授权门再调用。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。

## 出处

- 注册表：`caps_registry.py` · 域 `tentacle` · handler `omarchy_bridge`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
