# 域 `engine`

**10 位能力** · 需授权 1 · 多操作 2 · 需入参 4

| 能力位 | 安全 | 形态 | 入参 | 一句话 |
|---|---|---|---|---|
| [`sched_define`](./sched_define.md) | safe | 单动作 | name, workflow, every_seconds | 定时触发器 |
| [`sched_status`](./sched_status.md) | safe | 单动作 | — | 定时触发器 |
| [`sched_tick`](./sched_tick.md) | safe | 单动作 | — | 定时触发器 |
| [`transfer`](./transfer.md) | safe | 多操作 | — | 数据传输算子（核心传输工具） |
| [`wf_cache_clear`](./wf_cache_clear.md) | safe | 单动作 | — | 万能插 |
| [`wf_define`](./wf_define.md) | safe | 单动作 | name, nodes | 万能插执行引擎 |
| [`wf_resume`](./wf_resume.md) | safe | 单动作 | run_id | 万能插执行引擎 |
| [`wf_run`](./wf_run.md) | safe | 单动作 | name | 万能插执行引擎 |
| [`wf_status`](./wf_status.md) | safe | 单动作 | — | 万能插执行引擎 |
| [`workflow_forge`](./workflow_forge.md) | **gated** | 多操作 | — | **工作流十式**（主人令 2026-10-16 |

返回上级索引：[`caps/`](../README.md)
