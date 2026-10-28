# 域 `data`

**12 位能力** · 需授权 3 · 多操作 7 · 需入参 1

| 能力位 | 安全 | 形态 | 入参 | 一句话 |
|---|---|---|---|---|
| [`account_registry`](./account_registry.md) | safe | 单动作 | — | AI 账号登记表只读校验 |
| [`audit_query`](./audit_query.md) | safe | 单动作 | — | 只读查询统一数据后台日志 |
| [`bi_distill`](./bi_distill.md) | safe | 多操作 | — | **蒸馏件**（不是外挂） |
| [`chart_html`](./chart_html.md) | **gated** | 多操作 | — | **数据 → 自包含交互 ECharts HTML**（蒸馏自 skills |
| [`count_words`](./count_words.md) | safe | 单动作 | — | 统计文本词数 |
| [`datakit`](./datakit.md) | safe | 单动作 | — | 本地数据工具（**只读**） |
| [`db_plugin`](./db_plugin.md) | safe | 多操作 | — | 数据库插件（只读骨架） |
| [`db_probe`](./db_probe.md) | safe | 多操作 | — | 本地只读查询台（dbx 蒸馏） |
| [`echo`](./echo.md) | safe | 单动作 | — | 回显传入数据，用于联调 |
| [`humanizer`](./humanizer.md) | **gated** | 多操作 | — | **去 AI 味改写器**（蒸馏自 skills.sh humanizer- |
| [`record_grid`](./record_grid.md) | safe | 多操作 | text, path | 行式记录网格 |
| [`skill_finder`](./skill_finder.md) | **gated** | 多操作 | — | **技能检索器**（蒸馏自 skills.sh find-skills，只蒸 |

返回上级索引：[`caps/`](../README.md)
