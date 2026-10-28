# `browser`

| 项目 | 值 |
|---|---|
| 域 | [`automation`](./README.md) |
| 安全标记 | `safe: true` |
| 外部依赖 | 无 |
| 入参 | `url` |
| 形态 | 一位多操作（描述中枚举：`open` / `search` / `fetch` / `automate`） |
| 处理器 | `browser` |

## 用途

浏览器自动化入口（良性子集）。op=open/search/fetch/automate 走 browser_cap 三级后端；op=native（别名 deep/controller/cdp）走原生浏览器窗口 native_browser.py（Chrome DevTools Protocol，自带最小 RFC6455 客户端、零第三方依赖），动作放 action：status/list_tabs/get_title/get_url/get_text/dom_query/get_cookies/intercept_events/intercept_status 为只读免卡，launch/ensure/create_tab/close_tab/activate_tab/navigate/reload/back/forward/click_element/type_text/execute_script/inject_script/set_cookies/privacy_mode/intercept_requests/intercept_stop/pin_window 需 browser_control，screenshot 另需 filesystem_write

## 使用方式

### 1. 查规格（本仓，无需任何依赖）

```python
from gbt_caps import lookup

spec = lookup("browser")
print(spec.desc)
print(spec.params, spec.safe)
```

```bash
gbt-caps show browser          # 本页内容的终端版
gbt-caps show browser --json   # 给程序用
```

### 2. 真正调用（需要装上实现该位的框架）

本仓是**规格与契约**，不含实现。实现由上游框架提供，调用约定是统一的：

```python
from gbt_allinone import run_task

result = run_task("browser", {'op': '<见描述>', 'url': ...})
```

## 参数

| 参数 | 必填 | 说明 |
|---|---|---|
| `url` | 是 | 默认 op=open 必须要 url；只读路请写 op=native + action=status |

## 返回

统一契约：一个 dict，至少含 `ok`（布尔）与 `gbt_stamp`（框架印章：版本 / 开发者 / 归属）。业务字段由该位的实现决定，本仓**不臆造**具体返回结构——需要精确字段时读实现或先跑一次。

## 边界与注意

- 注册表把它标为 `safe: true`：调用不会越出「读 / 算 / 写自有 store」这一类。`safe` 是**声明**，不是运行时保证——真正兜底的是部署方的授权门。
- 一个名字对应多个操作：**必须给 `op` / `action`**，否则默认分支可能不是你要的那个。
- 入参缺失会被拒绝（空调用不成立），这是有意设计的契约，不是缺陷。

## 出处

- 注册表：`caps_registry.py` · 域 `automation` · handler `browser`
- 快照 schema `1` · 源文件 sha256 前 12 位 `1c85007b73b9`
- 本页由 `tools/build_atlas.py` 从快照生成，**请勿手改**；改数据源后重新生成。
