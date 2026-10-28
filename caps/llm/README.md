# 域 `llm`

**41 位能力** · 需授权 8 · 多操作 20 · 需入参 8

| 能力位 | 安全 | 形态 | 入参 | 一句话 |
|---|---|---|---|---|
| [`automation_keys`](./automation_keys.md) | safe | 多操作 | — | 自动化配置密钥口（APP 设置调它） |
| [`autopilot`](./autopilot.md) | safe | 单动作 | goal | 自主编排环 |
| [`brain_execute`](./brain_execute.md) | safe | 单动作 | kind | 大脑执行层·执行维 |
| [`brain_health`](./brain_health.md) | safe | 单动作 | — | 大脑执行层·健康维 |
| [`brain_route`](./brain_route.md) | safe | 单动作 | intent | 大脑执行层·路由维 |
| [`brain_unify`](./brain_unify.md) | safe | 单动作 | goal | 大脑执行层·五维合一 |
| [`brain_verify`](./brain_verify.md) | safe | 单动作 | — | 大脑执行层·验证维 |
| [`claude_code`](./claude_code.md) | **gated** | 单动作 | — | Claude Code CLI: official Anthropic co |
| [`cloud_llm`](./cloud_llm.md) | safe | 单动作 | — | 调用Agnes AI云端算力 |
| [`codebuddy`](./codebuddy.md) | **gated** | 单动作 | — | CodeBuddy CLI: AI coding assistant |
| [`codex_chat`](./codex_chat.md) | safe | 单动作 | message | 官方 Codex 同步对话 |
| [`codex_interrupt`](./codex_interrupt.md) | safe | 单动作 | thread_id | 官方 Codex 写操作 |
| [`codex_models`](./codex_models.md) | safe | 单动作 | — | 官方 Codex 只读 |
| [`codex_status`](./codex_status.md) | safe | 单动作 | — | 官方 Codex 只读状态 |
| [`codex_thread_new`](./codex_thread_new.md) | safe | 单动作 | — | 官方 Codex 写操作 |
| [`codex_tools`](./codex_tools.md) | safe | 单动作 | — | 官方 Codex 只读 |
| [`codex_turn_send`](./codex_turn_send.md) | safe | 单动作 | thread_id | 官方 Codex 写操作 |
| [`duty_board`](./duty_board.md) | safe | 多操作 | — | 大脑执行层·**在岗看板**（主人令 2026-10-13「大脑执行层必须确 |
| [`energy_scheduler`](./energy_scheduler.md) | safe | 多操作 | — | 能源调度面（蒸馏自 2026-09-28 主人给的周榜卡 vllm 92.7 |
| [`fact_gate`](./fact_gate.md) | safe | 多操作 | — | **机器事实直答门**（主人令 2026-10-11「拿实质性证据说话，禁止 |
| [`freellmapi`](./freellmapi.md) | safe | 多操作 | — | FreeLLMAPI（本机免费大模型池 127.0.0.1:31415，34 |
| [`genoffice_bridge`](./genoffice_bridge.md) | **gated** | 多操作 | — | GenOffice AI 线 → 统一密钥网关的**本地 OpenAI 兼容 |
| [`key_gateway`](./key_gateway.md) | **gated** | 多操作 | — | 统一密钥网关 |
| [`llm_chat`](./llm_chat.md) | safe | 单动作 | — | 操控其他AI |
| [`llm_status`](./llm_status.md) | safe | 单动作 | — | LLM网关状态 |
| [`llm_watch`](./llm_watch.md) | safe | 多操作 | — | 大脑执行层·**守望**（主人令 2026-10-13「监控触手LLM的监控 |
| [`model_key_pool`](./model_key_pool.md) | safe | 单动作 | — | 模型密钥池（只读骨架） |
| [`multimodal_port`](./multimodal_port.md) | **gated** | 多操作 | — | 多模态维度 × 触手密钥 **Y 字端口** |
| [`offload_distill`](./offload_distill.md) | safe | 多操作 | — | **内存墙蒸馏件**（Edge0 思路 → 我们的运行纪律 + **触手映射 |
| [`omni_plug`](./omni_plug.md) | **gated** | 多操作 | — | 万能插 |
| [`policy_gate`](./policy_gate.md) | safe | 多操作 | — | **权限／付款直答门**（fact_gate 同族 · 主人令「拿实质性证据 |
| [`prompt_bridge`](./prompt_bridge.md) | safe | 单动作 | — | 提示词转化挂件（只读/纯本地） |
| [`quant_plan`](./quant_plan.md) | **gated** | 多操作 | — | **压缩与直达**（主人令 2026-10-16 深度蒸馏自 Bonsai  |
| [`replan_loop`](./replan_loop.md) | safe | 多操作 | — | 大脑执行层·**回流环**（主人令 2026-10-13「遇到问题不能直接停 |
| [`ring_context`](./ring_context.md) | safe | 多操作 | — | **环形自动化上下文**（主人令 2026-10-11「设计一个圆型的自动化 |
| [`task_graph`](./task_graph.md) | safe | 多操作 | — | 大脑执行层·**任务图**（主人令 2026-10-13「每次指派任务都要有 |
| [`think_loop`](./think_loop.md) | safe | 单动作 | goal | 推演环 |
| [`train_ground`](./train_ground.md) | **gated** | 多操作 | — | **回炉训练场（她的手）**（主人令 2026-10-16 |
| [`train_recipe`](./train_recipe.md) | safe | 多操作 | — | 训练配方与就绪闸（train-llm-from-scratch #10 蒸馏 |
| [`transformer`](./transformer.md) | safe | 多操作 | — | 变压器（**核心已按成熟成品吃透后重做** 2026-09-27） |
| [`warm_switch`](./warm_switch.md) | safe | 多操作 | — | **按需常驻开关**（主人 2026-10-12「可以通过隧道，你这么跳都一 |

返回上级索引：[`caps/`](../README.md)
